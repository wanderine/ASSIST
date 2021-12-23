#!/bin/bash

#SBATCH --gpus 4
#SBATCH -t 3-00:00:00

cp -r /proj/assist/users/andek67/MITPGAN3D /scratch/local

cd /scratch/local/MITPGAN3D

module load Anaconda/2021.05-nsc1

conda activate /proj/assist/users/x_anekl/MITPGAN3DCUDA11_env

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/proj/assist/users/x_anekl/MITPGAN3DCUDA11_env/lib

python3.9 main.py train --dataset datasets/CONTROLS_128_small_training --run_id results/CONTROLS_128_small_training_kiters800 --dimensionality 3 --latent_size 256 --kiters_per_resolution 800 --kiters_per_transition 800 --lr 1e-4 --target_resolution 128 --gpus '/gpu:0' '/gpu:1' '/gpu:2' '/gpu:3'

cp -r /scratch/local/MITPGAN3D/results/* /proj/assist/users/andek67/MITPGAN3D/results/







