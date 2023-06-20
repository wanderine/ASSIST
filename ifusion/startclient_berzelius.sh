#!/bin/bash

#SBATCH --gpus 1
#SBATCH -t 1-00:00:00
#SBATCH -A Berzelius-2023-74

mylocation=/proj/assist/users/x_anekl/ifusion_brats

singularity exec --writable-tmpfs --nv --no-home  --bind $mylocation/data/BRATS_2020/MICCAI_BraTS2020_TrainingData:/shared1  $mylocation/ifusion.sif /shared1/berzelius_1/startup/sub_start.sh
