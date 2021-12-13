close all
clear all
clc

addpath('/Users/andek67/Research_projects/nifti_matlab/');

basepath_nii = '/Users/andek67/Downloads/BRATS_2020/MICCAI_BraTS2020_TrainingData/';
basepath_png = '/Users/andek67/Downloads/BRATS_2020/MICCAI_BraTS2020_TrainingData_slices/';

subjects = dir(basepath_nii);

for subject = 4:(4+369)
    
    nii = load_nii([basepath_nii subjects(subject).name '/' subjects(subject).name '_t1.nii']);
    volume_T1 = nii.img; volume_T1 = double(volume_T1);
    nii = load_nii([basepath_nii subjects(subject).name '/' subjects(subject).name '_t2.nii']);
    volume_T2 = nii.img; volume_T2 = double(volume_T2);
    nii = load_nii([basepath_nii subjects(subject).name '/' subjects(subject).name '_t1ce.nii']);
    volume_T1ce = nii.img; volume_T1ce = double(volume_T1ce);
    nii = load_nii([basepath_nii subjects(subject).name '/' subjects(subject).name '_flair.nii']);
    volume_flair = nii.img; volume_flair = double(volume_flair);
    nii = load_nii([basepath_nii subjects(subject).name '/' subjects(subject).name '_seg.nii']);
    volume_seg = nii.img; volume_seg = int16(volume_seg);
    
    [sy sx sz] = size(volume_T1);
    
    figure(1)
    imagesc(volume_T1(:,:,100))
    subject
    
    % Normalize intensity to 0 - 62 000
    volume_T1 = volume_T1 / max(volume_T1(:)) * 62000;
    volume_T2 = volume_T2 / max(volume_T2(:)) * 62000;
    volume_T1ce = volume_T1ce / max(volume_T1ce(:)) * 62000;
    volume_flair = volume_flair / max(volume_flair(:)) * 62000;
    
    for z = 1:sz
        slice_T1 = volume_T1(:,:,z);
        slice_T2 = volume_T2(:,:,z);
        slice_T1ce = volume_T1ce(:,:,z);
        slice_flair = volume_flair(:,:,z);
        slice_seg = volume_seg(:,:,z);
        
        % Pad to 256 x 256 (for GAN training)
        temp = zeros(256,256); temp(9:end-8,9:end-8) = slice_T1; slice_T1 = temp;
        temp = zeros(256,256); temp(9:end-8,9:end-8) = slice_T2; slice_T2 = temp;
        temp = zeros(256,256); temp(9:end-8,9:end-8) = slice_T1ce; sliceT1ce = temp;
        temp = zeros(256,256); temp(9:end-8,9:end-8) = slice_flair; slice_flair = temp;
        temp = zeros(256,256); temp(9:end-8,9:end-8) = slice_seg; slice_seg = temp;
        
        
        % Ignore slices with too much black
        if sum(slice_T1(:)) > 500000 
            imwrite(uint16(slice_T1),[basepath_png 'Subject_' num2str(subject-3) '_slice_' num2str(z) '_T1.png'],'png');
            imwrite(uint16(slice_T2),[basepath_png 'Subject_' num2str(subject-3) '_slice_' num2str(z) '_T2.png'],'png');
            imwrite(uint16(slice_T1ce),[basepath_png 'Subject_' num2str(subject-3) '_slice_' num2str(z) '_T1ce.png'],'png');
            imwrite(uint16(slice_flair),[basepath_png 'Subject_' num2str(subject-3) '_slice_' num2str(z) '_flair.png'],'png');
            imwrite(uint16(slice_seg*10000),[basepath_png 'Subject_' num2str(subject-3) '_slice_' num2str(z) '_seg.png'],'png');
        end
    end
end

