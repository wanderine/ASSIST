#!/bin/bash

for file in "rawdata/BRATS_2020/slices/"*T1.png ; do mv -- "$file" "downloads/brats2020_29000slices/T1" ; done

for file in "rawdata/BRATS_2020/slices/"*T2.png ; do mv -- "$file" "downloads/brats2020_29000slices/T2" ; done

for file in "rawdata/BRATS_2020/slices/"*T1ce.png ; do mv -- "$file" "downloads/brats2020_29000slices/T1CE" ; done

for file in "rawdata/BRATS_2020/slices/"*flair.png ; do mv -- "$file" "downloads/brats2020_29000slices/FLAIR" ; done

for file in "rawdata/BRATS_2020/slices/"*seg.png ; do mv -- "$file" "downloads/brats2020_29000slices/Seg" ; done



