#!/bin/bash

mylocation=/local/data1/andek67/fedn_brats

singularity exec --writable-tmpfs --nv --no-home --bind $mylocation/client.yaml:/app/client.yaml --bind $mylocation/data/BRATS_2020/MICCAI_BraTS2020_TrainingData:/var/data --bind $mylocation/client_settings.yaml:/var/client_settings.yaml $mylocation/fednsingularity.sif /venv/bin/fedn run client --secure=True --force-ssl -in /app/client.yaml
