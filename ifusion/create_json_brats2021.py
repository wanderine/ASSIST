import os
import json
import random
import csv

def get_data_list(dataset_folder):
    bratsClients = {}


    bratsClients['all_subjects'] = [record for record in os.listdir(dataset_folder) if
                         record.startswith("BraTS2021_")]

    my_file = open("brats_2021_site1_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 1, 511 subjects
    bratsClients['noname_1'] = data_into_list

    my_file = open("brats_2021_site2_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 2, 6 subjects
    bratsClients['noname_2'] = data_into_list

    my_file = open("brats_2021_site3_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()
    
    # site 3, 15 subjects
    bratsClients['noname_3'] = data_into_list
        
    my_file = open("brats_2021_site4_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 4, 47 subjects
    bratsClients['noname_4'] = data_into_list

    my_file = open("brats_2021_site5_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()
    
    # site 5, 22 subjects
    bratsClients['TCGA_GBM_1'] = data_into_list

    my_file = open("brats_2021_site6_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 6, 34 subjects
    bratsClients['TCGA_GBM_2'] = data_into_list

    my_file = open("brats_2021_site7_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 7, 12 subjects
    bratsClients['TCGA_GBM_3'] = data_into_list

    my_file = open("brats_2021_site8_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 8, 8 subjects
    bratsClients['TCGA_GBM_4'] = data_into_list

    my_file = open("brats_2021_site9_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 9, 4 subjects
    bratsClients['TCGA_GBM_5'] = data_into_list

    my_file = open("brats_2021_site10_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 10, 8 subjects
    bratsClients['TCGA_GBM_6'] = data_into_list

    my_file = open("brats_2021_site11_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 11, 14 subjects
    bratsClients['TCGA_GBM_7'] = data_into_list

    my_file = open("brats_2021_site12_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 12, 11 subjects
    bratsClients['TCGA_LGG_1'] = data_into_list

    my_file = open("brats_2021_site13_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 13, 35 subjects
    bratsClients['TCGA_LGG_2'] = data_into_list

    my_file = open("brats_2021_site14_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 14, 6 subjects
    bratsClients['TCGA_LGG_3'] = data_into_list

    my_file = open("brats_2021_site15_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 15, 13 subjects
    bratsClients['TCGA_LGG_4'] = data_into_list

    my_file = open("brats_2021_site16_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 16, 34 subjects
    bratsClients['IvyGAP'] = data_into_list

    my_file = open("brats_2021_site17_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 17, 9 subjects
    bratsClients['noname_5'] = data_into_list
    
    my_file = open("brats_2021_site18_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 18, 382 subjects
    bratsClients['noname_6'] = data_into_list

    my_file = open("brats_2021_site19_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 19, 4 subjects
    bratsClients['ACRIN'] = data_into_list

    my_file = open("brats_2021_site20_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 20, 33 subjects
    bratsClients['CPTAC'] = data_into_list

    my_file = open("brats_2021_site21_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 21, 35 subjects
    bratsClients['noname_7'] = data_into_list

    my_file = open("brats_2021_site22_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 22, 7 subjects
    bratsClients['noname_8'] = data_into_list

    my_file = open("brats_2021_site23_subjects.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")    
    my_file.close()

    # site 23, 5 subjects
    bratsClients['noname_9'] = data_into_list
    
    
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
