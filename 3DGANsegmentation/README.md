Code used to synthesize brain tumor images and annotations, based on the BraTS 2020 dataset.

Based on using the 3D progressive growing GAN by MIT, https://github.com/neuronets/nobrainer

Instructions for running trainings on Berzelius (Sweden's Nvidia Superpod with 480 graphics cards)

If necessary, make sure that all nifti volumes have a size that is a power of 2 (e.g. 128^3 or 256^3), use help script prepare_nifti_volumes.m (which can also add augmentation)

Create a new anaconda environment

conda create --name nobrainer 
conda activate nobrainer
conda install python=3.8
pip install nobrainer

Create a TFrecord dataset from nifti files, ./make_dataset.py 

Download a singularity container, singularity pull docker://neuronets/nobrainer:latest-gpu

