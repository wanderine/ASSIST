#!/bin/bash

# To select graphics card
#export APPTAINERENV_CUDA_VISIBLE_DEVICES=2

mylocation=/flush/andek67/ifusion_liu

singularity exec --writable-tmpfs --nv --no-home  --bind $mylocation/data:/shared1  $mylocation/test.sif /shared1/harley/startup/start.sh
