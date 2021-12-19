#!/bin/bash

#conda activate mypgan3d

numSubjects=92

dataset1=brats2020_${numSubjects}subjects_rotationaugmentation_singlesegmentationchannel_min15percentcoverage
dataset2=brats2020_${numSubjects}subjects_noaugmentation_singlesegmentationchannel_min15percentcoverage

dataset3=brats2020_${numSubjects}subjects_rotationaugmentation_multiplesegmentationchannels_min15percentcoverage
dataset4=brats2020_${numSubjects}subjects_noaugmentation_multiplesegmentationchannels_min15percentcoverage

python3.7 dataset_tool.py create_from_brats_5channels datasets/${dataset1} downloads/${dataset1} 

python3.7 dataset_tool.py create_from_brats_5channels datasets/${dataset2} downloads/${dataset2} 

python3.7 dataset_tool.py create_from_brats_7channels datasets/${dataset3} downloads/${dataset3} 

python3.7 dataset_tool.py create_from_brats_7channels datasets/${dataset4} downloads/${dataset4} 







