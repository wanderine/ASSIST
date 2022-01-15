Code used to synthesize realistic brain volumes

Based on using the 3D progressive growing GAN by MIT, https://github.com/neuronets/nobrainer

Instructions for running trainings on Berzelius (Sweden's Nvidia Superpod with 480 graphics cards)

If necessary, make sure that all nifti volumes have a size that is a power of 2 (e.g. 128^3 or 256^3), use help script prepare_nifti_volumes.m (which can also add augmentation)

Download lates nobrainer singularity container, singularity pull docker://neuronets/nobrainer:latest-gpu

Create a TFrecord dataset from nifti files, modify createTfRecords.py, then run make_dataset_singularity.sh

Modify train_multigpu.py

Submit job on Berzelius, sbatch launch_job_singularity.sh



