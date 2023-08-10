#!/bin/bash

mylocation=/flush/andek67/liu_brats

singularity exec --writable-tmpfs --nv --no-home  --bind $mylocation/data/BRATS_2021:/shared1  $mylocation/ifusion.sif /shared1/admin@liu.se/startup/fl_admin.sh
