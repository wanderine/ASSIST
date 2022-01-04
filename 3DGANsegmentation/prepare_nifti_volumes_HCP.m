close all
clear all
clc

addpath('/home/andek67/Research_projects/nifti_matlab/');

basepath_nii = '/local/data1/andek67/MITPGAN3D/rawdata/HCP_T1/';

% Get list of subjects
subjects = dir(basepath_nii);

% Remove all non-subjects
removeIndex = 1;
removeIndices = [];
for subject = 1:length(subjects)
    if not(contains(subjects(subject).name,'T1w'))
        removeIndices(removeIndex) = subject;
        removeIndex = removeIndex + 1;
    end
end
subjects(removeIndices) = [];

teststring = '';

newsize = 256; % 128 or 256
sx = newsize; sy = newsize; sz = newsize;
[xi, yi, zi] = meshgrid(-(sx-1)/2:(sx-1)/2,-(sy-1)/2:(sy-1)/2, -(sz-1)/2:(sz-1)/2);

for augmentation = 2:2

    if augmentation == 1
        useAugmentation = false;
    else
        useAugmentation = true;
    end
    
        for numberOfSubjects = [1113]

            if useAugmentation 
                dataset = ['HCPT1_' num2str(numberOfSubjects) 'subjects_rotationaugmentation_' num2str(newsize) 'cubes' teststring];
            elseif not(useAugmentation) 
                dataset = ['HCPT1_' num2str(numberOfSubjects) 'subjects_noaugmentation_' num2str(newsize) 'cubes' teststring];
            end
            
            dataset
            
            basepath_prepared = ['/local/data1/andek67/MITPGAN3D/downloads/' dataset '/'];

            for subject = 1:numberOfSubjects

                subject
                
                nii = load_nii([basepath_nii subjects(subject).name]);
                volume_T1 = nii.img; volume_T1 = double(volume_T1);
                
		% Pad to 128 x 128 x 128 or 256 x 256 x 256 (for GAN training)
                if newsize == 128
                    3
                elseif newsize == 256
                    temp = volume_T1(3:end-2,28:end-28,3:end-2); volume_T1 = temp;
		end

                % Save original volume
		newFile.hdr = nii.hdr;
                newFile.hdr.dime.datatype = 16;
                newFile.hdr.dime.bitpix = 16;
                newFile.hdr.dime.dim = [3 newsize newsize newsize 1 1 1 1];
  	        newFile.img = single(volume_T1);
                filename = [basepath_prepared 'Subject_' subjects(subject).name(1:6) '_T1.nii.gz'];	
		save_nii(newFile,filename);
		
		if useAugmentation
                            
                    for augmentation = 1:9

                        randomRotationX = 50*rand - 25; % Random rotation between -25 and 25, uniform distribution
			randomRotationY = 50*rand - 25; % Random rotation between -25 and 25, uniform distribution
			randomRotationZ = 50*rand - 25; % Random rotation between -25 and 25, uniform distribution

			R_x = [1                        0                           0;
                    		0                        cosd(randomRotationX)      -sind(randomRotationX);
                    		0                        sind(randomRotationX)      cosd(randomRotationX)];
                
                	R_y = [cosd(randomRotationY)   0                          sind(randomRotationY);
              	 		   0                        1                           0;
              		      -sind(randomRotationY)  0                           cosd(randomRotationY)];
                
                	R_z = [cosd(randomRotationZ)   -sind(randomRotationZ)     0;
                    	       sind(randomRotationZ)   cosd(randomRotationZ)      0;
                    		0                        0                           1];
                
                	Rotation_matrix = R_x * R_y * R_z;
                	Rotation_matrix = Rotation_matrix(:);
                
                	rx_r = zeros(sy,sx,sz);
                	ry_r = zeros(sy,sx,sz);
                	rz_r = zeros(sy,sx,sz);
                
                	rx_r(:) = [xi(:) yi(:) zi(:)]*Rotation_matrix(1:3);
                	ry_r(:) = [xi(:) yi(:) zi(:)]*Rotation_matrix(4:6);
                	rz_r(:) = [xi(:) yi(:) zi(:)]*Rotation_matrix(7:9);

			newVolume = interp3(xi,yi,zi,volume_T1,rx_r,ry_r,rz_r,'cubic');
                        % Remove 'not are numbers' from interpolation
                	newVolume(isnan(newVolume)) = 0;
                        
            		newFile.hdr = nii.hdr;
           		newFile.hdr.dime.datatype = 16;
                        newFile.hdr.dime.bitpix = 16;
                        newFile.hdr.dime.dim = [3 newsize newsize newsize 1 1 1 1];
             		newFile.img = single(newVolume);

                        filename = [basepath_prepared 'Subject_' subjects(subject).name(1:6) '_augmentation_' num2str(augmentation) '_T1.nii.gz'];
            		save_nii(newFile,filename);
                    end
                end
           end
    end
end


