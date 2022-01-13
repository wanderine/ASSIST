#!/bin/bash

# Loop over all subjects

for i in /flush/common/TCGI/* ; do

    cd $i
    echo "Processing" $i
    for f in *\ *; do mv "$f" "${f// /_}"; done

    cd *
    for f in *\ *; do mv "$f" "${f// /_}"; done

    cd *T1*
    for f in *\ *; do mv "$f" "${f// /_}"; done
    cd ..

    cd *DTI*
    for f in *\ *; do mv "$f" "${f// /_}"; done

done

wait

