#!/bin/bash

# Loop over all subjects

threads=0
MaximumThreads=10  #subjects to process in parallel

for i in /flush/common/TCGI/* ; do

    cd $i
    echo "Processing" $i
    cd *

    # Extract b0 volume from corrected dataset (first volume)
    cd *DTI*
    fslroi dti_corrected.nii.gz b0.nii.gz 0 1

    # Make mask for later use with dtifit
    bet b0.nii.gz b0_brain.nii.gz -m 
    cd ..

    # Register T1 and EPI
    epi_reg --epi=*DTI*/b0.nii.gz --t1=*T1*/T1.nii.gz --t1brain=*T1*/T1_brain.nii.gz --out=registration &

    ((threads++))

    if [ "$threads" -eq "$MaximumThreads" ]; then
    	wait
        threads=0
    fi
done

wait



