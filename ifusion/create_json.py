import os
import json
import random
import glob

# This script assumes that all nifti files (for T1, T1 GD, T2 GD, T2 FLAIR, seg (annotations)) are stored in one directory for all patients, with a unique patient string per patient, e.g.

# MR_T2_FLAIR__PatientString_defaced_256.nii.gz
# MR_T1__PatientString_defaced_256.nii.gz
# MR_T1_GD_PatientString_defaced_256.nii.gz
# MR_T2_GD_PatientString_defaced_256.nii.gz
# seg_PatientString_defaced_256.nii.gz

def create_dataset_json_onesite(root_dir, output_file, validation_percent=0.2):
    dataset = {"training": [], "validation": []}
    file_list = []

    # Get one filename per subject
    subject_list = glob.glob(root_dir + 'MR_T2_FLAIR*defaced*.nii.gz')
    #print(subject_list)

    # Loop over subjects
    for file in subject_list:
        print(file)
        file_list.append({
            "image": [
                 file,
                 file.replace("T2_FLAIR", "T1"),
                 file.replace("T2_FLAIR", "T1_GD"),
                 file.replace("T2_FLAIR", "T2_GD")
            ],
            "label": file.replace("MR_T2_FLAIR", "seg")
           })

    print(file_list)

    random.shuffle(file_list)
    # Use subset as validation
    num_validation = int(len(file_list) * validation_percent)
    dataset["training"] = file_list[:-num_validation]
    dataset["validation"] = file_list[-num_validation:]

    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=4)

        
# Example usage
root_directory = "/home/andek67/Research_projects/FederatedTumor/Data_withbiascorrection/AllPatientsNifti/"

output_json_file = root_directory + "linkoping.json"
create_dataset_json_onesite(root_directory, output_json_file)
