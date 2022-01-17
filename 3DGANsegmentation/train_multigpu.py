import nobrainer
import tensorflow as tf
import os
import nibabel as nib
import numpy as np
from pathlib import Path

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0,1,2,3,4,5,6,7"

nGPUs = 8

# RESOLUTION SPECIFICATION
#resolution_batch_size_map = {4: 64, 8: 64, 16: 32, 32: 32, 64: 16, 128: 2, 256: 1} 
#resolution_batch_size_map = {8: 32, 16: 16, 32: 8, 64: 4, 128: 1, 256: 1}
resolution_batch_size_map = {8: 64, 16: 32, 32: 16, 64: 8, 128: 2, 256: 1}
for key in resolution_batch_size_map:
    resolution_batch_size_map[key] = resolution_batch_size_map[key] * nGPUs
print(resolution_batch_size_map)

resolutions = sorted(list(resolution_batch_size_map.keys()))

# SET THE HYPERPARAMETERS
latent_size = 128
g_fmap_base = 2048
d_fmap_base = 2048
num_parallel_calls = 8
kiterations = int(400) # new default
#kiters_per_resolution = kiterations
#kiters_per_transition = kiterations
#kiters_per_resolution = {4: 80, 8: 100, 16: 120, 32: 140, 64: 160, 128: 180, 256: 200} # per reso defaults (from proggan)
#kiters_per_transition = {4: 80, 8: 100, 16: 120, 32: 140, 64: 160, 128: 180, 256: 200}
kiters_per_resolution = {4: 400, 8: 400, 16: 400, 32: 400, 64: 400, 128: 400, 256: 400} # per reso defaults (from proggan)   
kiters_per_transition = {4: 400, 8: 400, 16: 400, 32: 400, 64: 400, 128: 400, 256: 400}

lr = 1e-4

# CREATE LOGGING DIRECTORIES
save_dir = '/scratch/local/nobrainer/results/'

save_dir = Path(save_dir)
generated_dir = save_dir.joinpath('generated')
model_dir = save_dir.joinpath('saved_models')
log_dir = save_dir.joinpath('logs')

save_dir.mkdir(exist_ok=True)
generated_dir.mkdir(exist_ok=True)
model_dir.mkdir(exist_ok=True)

# INSTANTIATE NEURAL NETWORK
#strategy = tf.distribute.MirroredStrategy(['/gpu:0', '/gpu:1', '/gpu:2', '/gpu:3', '/gpu:4','/gpu:5','/gpu:6', '/gpu:7'],cross_device_ops=tf.distribute.HierarchicalCopyAllReduce())
#strategy = tf.distribute.MirroredStrategy(['/gpu:0', '/gpu:1', '/gpu:2', '/gpu:3'])                 
strategy = tf.distribute.MirroredStrategy(['/gpu:0', '/gpu:1', '/gpu:2', '/gpu:3', '/gpu:4','/gpu:5','/gpu:6', '/gpu:7'])

with strategy.scope():
    generator, discriminator = nobrainer.models.progressivegan(latent_size,
                                                               g_fmap_base=g_fmap_base,
                                                               d_fmap_base=d_fmap_base)

# TRAIN THE NETWORK PROGRESSIVELY
for resolution in resolutions:
    
    # create a train dataset with features for resolution
    dataset_train = nobrainer.dataset.get_dataset(
        file_pattern="/scratch/local/nobrainer/datasets/HCPT1_1113subjects_rotationaugmentation_256cubes/*res-%03d*.tfrec"%(resolution),
        batch_size=resolution_batch_size_map[resolution],
        num_parallel_calls=num_parallel_calls,
        volume_shape=(resolution, resolution, resolution),
        n_classes=1, # dummy labels as this is unsupervised training
        scalar_label=True,
        normalizer=None
    )

    with strategy.scope():
        # grow the networks by one (2^x) resolution
        generator.add_resolution()
        discriminator.add_resolution()
        print(2**generator.current_resolution)
        # instantiate a progressive training helper
        progressive_gan_trainer = nobrainer.training.ProgressiveGANTrainer(
            generator=generator,
            discriminator=discriminator,
            gradient_penalty=True)

        # compile with optimizers and loss function of choice
        progressive_gan_trainer.compile(
            g_optimizer=tf.keras.optimizers.Adam(learning_rate=lr, beta_1=0.0, beta_2=0.99, epsilon=1e-8),
            d_optimizer=tf.keras.optimizers.Adam(learning_rate=lr, beta_1=0.0, beta_2=0.99, epsilon=1e-8),
            g_loss_fn=nobrainer.losses.wasserstein,
            d_loss_fn=nobrainer.losses.wasserstein
            )

    steps_per_epoch = kiters_per_resolution[resolution]*1000//resolution_batch_size_map[resolution]
    # save_best_only is set to False as it is an adversarial loss
    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(str(model_dir), save_weights_only=True, save_best_only=False, save_freq=10)

    # Train at resolution
    print('Resolution : {}'.format(resolution))

    print('Transition phase')
    progressive_gan_trainer.fit(
        dataset_train,
        phase='transition',
        resolution=resolution,
        steps_per_epoch=steps_per_epoch, # necessary for repeat dataset
        callbacks=[model_checkpoint_callback])

    print('Resolution phase')
    progressive_gan_trainer.fit(
        dataset_train,
        phase='resolution',
        resolution=resolution,
        steps_per_epoch=steps_per_epoch,
        callbacks=[model_checkpoint_callback])
    
    # save the final weights for this resolution
    generator.save(str(model_dir.joinpath('generator_res_{}'.format(resolution))))

    # Generate some synthetic brains for this resolution
    for synthetic in range(20):
        # Generate noise vector
        latents = tf.random.normal((1, latent_size))
        # Load generator
        temp_generator = tf.saved_model.load(str(model_dir.joinpath('generator_res_{}'.format(resolution))))
        generate = temp_generator.signatures["serving_default"]
        img = generate(latents)["generated"]
        img = np.squeeze(img)
        # Convert to nifti image
        img = nib.Nifti1Image(img.astype(np.uint8), np.eye(4))
        # Save nifti file 
        nib.save(img, str(generated_dir.joinpath('synthetic_res_{}_example_{}.nii.gz'.format(resolution,synthetic+1))))

        
