#!/bin/bash

# Loop over all subjects

threads=0
MaximumThreads=10  #subjects to process in parallel

for i in /flush/common/TCGI/* ; do

    cd $i
    echo "Processing" $i
    cd *

    # Simple motion correction
    cd *DTI*
    eddy_correct *.nii.gz dti_corrected.nii.gz 0 &

    ((threads++))

    if [ "$threads" -eq "$MaximumThreads" ]; then
    	wait
        threads=0
    fi

done

wait

