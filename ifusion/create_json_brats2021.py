import os
import json
import random
import csv

def get_data_list(dataset_folder):
    bratsClients = {}


    bratsClients['all_subjects'] = [record for record in os.listdir(dataset_folder) if
                         record.startswith("BraTS2021_")]

    # site 2
    bratsClients['noname_2'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and 1411 <= int(record.split("0")[2]) <= 1416)]
    # site 3
    bratsClients['noname_3'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and 1426 <= int(record.split("0")[2]) <= 1440)]
    # site 4
    bratsClients['noname_4'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and ( int(record.split("00")[2]) == 561 or int(record.split("00")[2]) == 563 or int(record.split("00")[2]) == 565 or int(record.split("0")[2]) == 1151 or int(record.split("0")[2]) == 1152 or 1167 <= int(record.split("0")[2]) <= 1201 or int(record.split("0")[2]) == 1537  or 1657 <= int(record.split("0")[2]) <= 1662 )) ]

    # site 5
    bratsClients['TCGA_GBM_1'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and ( int(record.split("00")[2]) == 100 or int(record.split("00")[2]) == 102 or int(record.split("00")[2]) == 109 or int(record.split("00")[2]) == 113 or int(record.split("00")[2]) == 123 or int(record.split("00")[2]) == 139 or int(record.split("00")[2]) == 149 or int(record.split("00")[2]) == 151 or int(record.split("00")[2]) == 999 or int(record.split("0")[2]) == 1002 or int(record.split("0")[2]) == 1003 or int(record.split("0")[2]) == 1005 or int(record.split("0")[2]) == 1007 or int(record.split("0")[2]) == 1009  or 1281 <= int(record.split("0")[2]) <= 1284 or 1289 <= int(record.split("0")[2]) <= 1282 ))]   

    # site 6
    bratsClients['TCGA_GBM_2'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and ( int(record.split("00")[2]) == 105 or int(record.split("00")[2]) == 120 or int(record.split("00")[2]) == 121 or int(record.split("00")[2]) == 132 or int(record.split("00")[2]) == 133 or int(record.split("00")[2]) == 136 or int(record.split("00")[2]) == 137 or int(record.split("00")[2]) == 142  or int(record.split("00")[2]) == 143 or int(record.split("00")[2]) == 144 or int(record.split("00")[2]) == 146 or int(record.split("00")[2]) == 147 or int(record.split("00")[2]) == 831   or 1296 <= int(record.split("0")[2]) <= 1298 or int(record.split("0")[2]) == 1300 or int(record.split("0")[2]) == 1302  or int(record.split("0")[2]) == 1303  or 1441 <= int(record.split("0")[2]) <= 1455 ))]   

    # site 7
    bratsClients['TCGA_GBM_3'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and 1456 <= int(record.split("0")[2]) <= 1467)]   

    # site 8
    bratsClients['TCGA_GBM_4'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and ( int(record.split("00")[2]) == 104 or int(record.split("00")[2]) == 110 or int(record.split("00")[2]) == 112 or int(record.split("00")[2]) == 128 or int(record.split("00")[2]) == 140 or 1468 <= int(record.split("0")[2]) <= 1470 ))]   

    # site 9
    bratsClients['TCGA_GBM_5'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and ( int(record.split("00")[2]) == 116 or int(record.split("00")[2]) == 134 or int(record.split("00")[2]) == 150 or int(record.split("0")[2]) == 1471  ))]   

    # site 10
    bratsClients['TCGA_GBM_6'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS2021_") and ( int(record.split("00")[2]) == 106 or int(record.split("00")[2]) == 111 or int(record.split("00")[2]) == 117 or int(record.split("00")[2]) == 124 or int(record.split("00")[2]) == 130 or int(record.split("00")[2]) == 138 or int(record.split("0")[2]) == 1472 or int(record.split("0")[2]) == 1473  ))]   
  


    
    return bratsClients


def get_clients(client_names,datafolder):

    brats_clients = get_data_list(datafolder)
    data_list = []
    for c in client_names:
        data_list += brats_clients[c]
        
    return data_list


def create_dataset_json_onesite(root_dir, output_file, site, validation_percent=0.2):
    dataset = {"training": [], "validation": []}
    file_list = []

    brats_clients = get_data_list(root_dir)
    subject_list = brats_clients[site]
    #print(subject_list)
    subject = 0
    for s in subject_list:
        subject_list[subject] = root_dir + s
        subject += 1
    #print(subject_list)

    for this_dir in subject_list:
        for subdir, dirs, files in os.walk(this_dir):
            for file in files:
                if file.endswith("t1ce.nii"):
                    file_list.append({
                        "image": [
                            os.path.join(subdir, file),
                            os.path.join(subdir, file.replace("t1ce.nii", "t1.nii")),
                            os.path.join(subdir, file.replace("t1ce.nii", "t2.nii")),
                            os.path.join(subdir, file.replace("t1ce.nii", "flair.nii"))
                        ],
                        "label": os.path.join(subdir, file.replace("t1ce.nii", "seg.nii"))
                       })

    random.shuffle(file_list)
    num_validation = int(len(file_list) * validation_percent)
    dataset["training"] = file_list[:-num_validation]
    dataset["validation"] = file_list[-num_validation:]

    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=4)

def create_dataset_json_separatevalidationsite(root_dir, output_file, training_site, validation_site):
    dataset = {"training": [], "validation": []}
    file_list_training = []
    file_list_validation = []

    brats_clients = get_data_list(root_dir)
    
    subject_list = brats_clients[training_site]
    subject = 0
    for s in subject_list:
        subject_list[subject] = root_dir + s
        subject += 1  

    for this_dir in subject_list:
        for subdir, dirs, files in os.walk(this_dir):
            for file in files:
                if file.endswith("t1ce.nii"):
                    file_list_training.append({
                        "image": [
                            os.path.join(subdir, file),
                            os.path.join(subdir, file.replace("t1ce.nii", "t1.nii")),
                            os.path.join(subdir, file.replace("t1ce.nii", "t2.nii")),
                            os.path.join(subdir, file.replace("t1ce.nii", "flair.nii"))
                        ],
                        "label": os.path.join(subdir, file.replace("t1ce.nii", "seg.nii"))
                       })


    subject_list = brats_clients[validation_site]
    subject = 0
    for s in subject_list:
        subject_list[subject] = root_dir + s
        subject += 1

    for this_dir in subject_list:
        for subdir, dirs, files in os.walk(this_dir):
            for file in files:
                if file.endswith("t1ce.nii"):
                    file_list_validation.append({
                        "image": [
                            os.path.join(subdir, file),
                            os.path.join(subdir, file.replace("t1ce.nii", "t1.nii")),
                            os.path.join(subdir, file.replace("t1ce.nii", "t2.nii")),
                            os.path.join(subdir, file.replace("t1ce.nii", "flair.nii"))
                        ],
                        "label": os.path.join(subdir, file.replace("t1ce.nii", "seg.nii"))
                       })

                    
    dataset["training"] = file_list_training
    dataset["validation"] = file_list_validation

    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=4)
        
# Example usage
root_directory = "/proj/assist/users/x_anekl/ifusion_brats/data/BRATS_2021/"

#site = "noname_1"
#output_json_file = site + ".json"
#create_dataset_json_onesite(root_directory, output_json_file, site, validation_percent=0.2)

training_site = "noname_3"
validation_site = "noname_1"
output_json_file = root_directory + "berzelius_1.json"
create_dataset_json_separatevalidationsite(root_directory, output_json_file, training_site, validation_site)
