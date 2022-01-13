#!/bin/bash

# Loop over all subjects

threads=0
MaximumThreads=10  #subjects to process in parallel

for i in /flush/common/TCGI/* ; do

    cd $i
    echo "Processing" $i
    cd *

    # Do a brain segmentation, required for epi_reg
    cd *T1*
    cp *T1*.nii.gz T1.nii.gz # Make a copy for easier use later
    bet T1.nii.gz T1_brain.nii.gz &

    ((threads++))

    if [ "$threads" -eq "$MaximumThreads" ]; then
    	wait
        threads=0
    fi

done

wait

