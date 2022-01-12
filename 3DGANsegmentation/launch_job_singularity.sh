#!/bin/bash

#SBATCH --gpus 8
#SBATCH -t 3-00:00:00

cp -r /proj/assist/users/andek67/nobrainer /scratch/local

cd /scratch/local/nobrainer

singularity exec --no-home --nv -B $(pwd) nobrainer_latest-gpu.sif python3.8 train_multigpu.py

cp -r /scratch/local/nobrainer/results/* /proj/assist/users/andek67/nobrainer/results/HCPT1_1113subjects_rotationaugmentation_256cubes_kiters400_latentsize256_8GPUs/







