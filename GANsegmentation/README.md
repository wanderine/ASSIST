Code used to synthesize brain tumor images and annotations, based on the BraTS 2020 dataset.

Based on using the progressive growing GAN by Nvidida, https://github.com/tkarras/progressive_growing_of_gans , with changes to synthesize 5 channel (4 MRI + 1 annotation) or 7 channel (4 MRI + 3 annotation) images. The python files included here include the required modifications.

First run split_volumes_to_slices.m to generate PNG files from the nifti files in the BraTS dataset.

Then run make_dataset.sh to make TFrecord datasets from the PNG files (5 or 7 channels).

Modify config.py in the PGGAN code to use your new dataset.

Change train.py to use 5 or 7 channel images (5 as default).

Run train.py, wait a couple of days...

Warning: This code does not work with too new graphics cards, like RTX 3090 from the Ampere architecture.
