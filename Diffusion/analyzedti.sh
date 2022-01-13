#!/bin/bash

# Loop over all subjects

threads=0
MaximumThreads=10  #subjects to process in parallel

for i in /flush/common/TCGI/* ; do

    cd $i
    echo "Processing" $i
    cd *

    cd *DTI*

    # Do DTI fitting
    dtifit -k dti_corrected.nii.gz -o fitted -m b0_brain_mask.nii.gz -r *.bvec -b *.bval &

    ((threads++))

    if [ "$threads" -eq "$MaximumThreads" ]; then
    	wait
        threads=0
    fi
done

wait


