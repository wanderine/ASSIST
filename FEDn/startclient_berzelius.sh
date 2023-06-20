#!/bin/bash

#SBATCH --gpus 1
#SBATCH -t 1-00:00:00
#SBATCH -A Berzelius-2023-74

mylocation=/proj/assist/users/x_anekl/fedn_brats

singularity exec --writable-tmpfs --nv --no-home --bind $mylocation/client1.yaml:/app/client.yaml --bind $mylocation/data/BRATS_2020/MICCAI_BraTS2020_TrainingData:/var/data --bind $mylocation/client_settings1.yaml:/var/client_settings.yaml $mylocation/fednsingularity.sif /venv/bin/fedn run client --secure=True --force-ssl -in /app/client.yaml
