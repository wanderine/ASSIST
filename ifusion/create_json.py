import os
import json
import random


def get_data_list(dataset_folder):
    bratsClients = {}


    bratsClients['all_subjects'] = [record for record in os.listdir(dataset_folder) if
                         record.startswith("BraTS20_Training")]

    bratsClients['CBICA'] = [record for record in os.listdir(dataset_folder) if
                       (record.startswith("BraTS20_Training") and int(record.split("_")[2]) <= 129)]

    bratsClients['noname_1'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 130 <= int(record.split("_")[2]) <= 149)]

    bratsClients['TMC'] = [record for record in os.listdir(dataset_folder) if
                     (record.startswith("BraTS20_Training") and (
                             150 <= int(record.split("_")[2]) <= 157 or int(record.split("_")[2]) == 270))]

    bratsClients['TCGA_02'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 158 <= int(record.split("_")[2]) <= 179)]

    bratsClients['TCGA_06'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 180 <= int(record.split("_")[2]) <= 213)]

    bratsClients['TCGA_08'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 214 <= int(record.split("_")[2]) <= 225)]

    bratsClients['TCGA_12'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 226 <= int(record.split("_")[2]) <= 233)]

    bratsClients['TCGA_14'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 234 <= int(record.split("_")[2]) <= 237)]

    bratsClients['TCGA_19'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 238 <= int(record.split("_")[2]) <= 245)]

    bratsClients['TCGA_76'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 246 <= int(record.split("_")[2]) <= 259)]

    bratsClients['noname_2'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 260 <= int(record.split("_")[2]) <= 269)]

    bratsClients['TCGA_CS'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 271 <= int(record.split("_")[2]) <= 281)]

    bratsClients['TCGA_DU'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 282 <= int(record.split("_")[2]) <= 316)]

    bratsClients['TCGA_FG'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 317 <= int(record.split("_")[2]) <= 322)]

    bratsClients['TCGA_HT'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 323 <= int(record.split("_")[2]) <= 335)]

    bratsClients['noname_3'] = [record for record in os.listdir(dataset_folder) if
                        (record.startswith("BraTS20_Training") and 336 <= int(record.split("_")[2]) <= 369)]

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
root_directory = "/proj/assist/users/x_anekl/ifusion_brats/data/BRATS_2020/MICCAI_BraTS2020_TrainingData/"

site = "CBICA"
output_json_file = site + ".json"

create_dataset_json_onesite(root_directory, output_json_file, site, validation_percent=0.2)


training_site = "noname_3"
validation_site = "TCGA_DU"
output_json_file = "myclient.json"
create_dataset_json_separatevalidationsite(root_directory, output_json_file, training_site, validation_site)


