#!/bin/bash

startDirectory=/flush2/andek67/Data/HCP/STRUCTURAL/

for i in /flush2/andek67/Data/HCP/STRUCTURAL/* ; do

    echo "This is directory " $i

    # Go to current directory
    cd $i
    # Get subject name
    Subject=${PWD##*/}
    echo "Processing" $Subject
    # Go back to original directory
    cd $startDirectory

    cp ${i}/MNINonLinear/T1w_restore_brain.nii.gz /flush2/andek67/Data/HCP/T1/${Subject}_T1w.nii.gz


done



