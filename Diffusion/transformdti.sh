#!/bin/bash

# Loop over all subjects

threads=0
MaximumThreads=10  #subjects to process in parallel

for i in /flush/common/TCGI/* ; do

    cd $i
    echo "Processing" $i
    cd *

    # Transform DTI scalar maps to T1 space
    flirt -in *DTI*/fitted_FA.nii.gz -ref *T1*/T1.nii.gz -applyxfm -init registration.mat -out FA_T1.nii.gz &
    flirt -in *DTI*/fitted_MD.nii.gz -ref *T1*/T1.nii.gz -applyxfm -init registration.mat -out MD_T1.nii.gz &

    ((threads++))

    if [ "$threads" -eq "$MaximumThreads" ]; then
    	wait
        threads=0
    fi
done


