#!/bin/bash
    

for i in {1..369}; do
   
   if [ "$i" -lt "10" ]; then
      folder=BraTS20_Training_00$i
      #cp $folder/BraTS20_Training_00${i}_seg.nii labels/
      #gzip labels/BraTS20_Training_00${i}_seg.nii
      fslmerge -t images/BraTS20_Training_00${i}_images.nii $folder/BraTS20_Training_00${i}_t1.nii $folder/BraTS20_Training_00${i}_t1ce.nii $folder/BraTS20_Training_00${i}_t2.nii $folder/BraTS20_Training_00${i}_flair.nii
      #gzip images/BraTS20_Training_00${i}_images.nii
   elif [ "$i" -lt "100" ]; then
      folder=BraTS20_Training_0$i
      #cp $folder/BraTS20_Training_0${i}_seg.nii labels/
      #gzip labels/BraTS20_Training_0${i}_seg.nii
      fslmerge -t images/BraTS20_Training_0${i}_images.nii $folder/BraTS20_Training_0${i}_t1.nii $folder/BraTS20_Training_0${i}_t1ce.nii $folder/BraTS20_Training_0${i}_t2.nii $folder/BraTS20_Training_0${i}_flair.nii
      #gzip images/BraTS20_Training_0${i}_images.nii
   else
      folder=BraTS20_Training_$i
      #cp $folder/BraTS20_Training_${i}_seg.nii labels/
      #gzip labels/BraTS20_Training_${i}_seg.nii
      fslmerge -t images/BraTS20_Training_${i}_images.nii $folder/BraTS20_Training_${i}_t1.nii $folder/BraTS20_Training_${i}_t1ce.nii $folder/BraTS20_Training_${i}_t2.nii $folder/BraTS20_Training_${i}_flair.nii 
      #gzip images/BraTS20_Training_${i}_images.nii
   fi

   echo $folder
   
   #cp $folder/BraTS20_Training_$i_seg.nii labels/

   #cd $folder
   #gunzip *.nii.gz
   #cd ..

done
