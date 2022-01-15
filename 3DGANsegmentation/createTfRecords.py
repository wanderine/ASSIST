import nobrainer
import os

train_paths = []
for file in os.listdir('/local/data1/andek67/nobrainer/downloads/HCPT1_1113subjects_rotationaugmentation_256cubes'): #your directory containing nii.gz files
    if ".nii.gz" in file: 
        train_paths.append(('/local/data1/andek67/nobrainer/downloads/HCPT1_1113subjects_rotationaugmentation_256cubes/'+file, 0))

invalid = nobrainer.io.verify_features_labels(train_paths, num_parallel_calls=8)
assert not invalid

resolution_batch_size_map = {4: 1, 8: 1, 16: 1, 32: 1, 64: 1, 128: 1, 256: 1} # Uses just the resolution keys, batch sizes can be anything here
resolutions = sorted(list(resolution_batch_size_map.keys()))

nobrainer.tfrecord.write(
    features_labels=train_paths,
    filename_template='/local/data1/andek67/nobrainer/datasets/HCPT1_1113subjects_rotationaugmentation_256cubes/train_shard-{shard:03d}.tfrec',  #output directory and format
    examples_per_shard=256, 
    multi_resolution=True,
    resolutions=resolutions)
