import nobrainer
import os

train_paths = []
for file in os.listdir('/work/data'): #your directory containing nii.gz files
    if ".nii.gz" in file: 
        train_paths.append(('/work/data/'+file, 0))

invalid = nobrainer.io.verify_features_labels(train_paths, num_parallel_calls=2)
assert not invalid

resolution_batch_size_map = {8: 1, 16: 1, 32: 1, 64: 1, 128: 1, 256: 1} # Uses just the resolution keys, batch sizes can be anything here
resolutions = sorted(list(resolution_batch_size_map.keys()))

nobrainer.tfrecord.write(
    features_labels=train_paths,
    filename_template='/work/data/data-train_shard-{shard:03d}.tfrec',  #output directory and format
    examples_per_shard=371, 
    multi_resolution=True,
    resolutions=resolutions)