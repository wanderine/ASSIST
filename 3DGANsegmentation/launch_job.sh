#!/bin/bash

#SBATCH --gpus 8
#SBATCH -t 3-00:00:00

cp -r /proj/assist/users/andek67/nobrainer /scratch/local

cd /scratch/local/nobrainer

module load Anaconda/2021.05-nsc1

conda activate /proj/assist/users/x_anekl/MITPGAN3DCUDA11_env

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/proj/assist/users/x_anekl/MITPGAN3DCUDA11_env/lib

python3.9 train_multigpu.py

cp -r /scratch/local/nobrainer/results/* /proj/assist/users/andek67/nobrainer/results/HCPT1_1113subjects_rotationaugmentation_256cubes_kiters400_latentsize256_8GPUs/







