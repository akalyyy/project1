import os
import json
from Validating_names import validation
from File_mover import move_file
from File_sorting import get_category, get_extension
from Report_summary import summary

with open("config.json", "r") as config_file:
    config = json.load(config_file)

for key in ["input_folder", "processed_folder", "quarantine_folder", "reports_folder", "logs_folder"]:
    os.makedirs(config[key], exist_ok=True)

input_folder = os.listdir(config["input_folder"])
log_file = open(f"{config['logs_folder']}/log.txt", "w")

processed_count = 0
quarantined_count = 0
archived_count = 0

processed_files = []
quarantined_files = []
archived_files = []

for file in input_folder:
    if validation(file) == True:
        category = get_category(file)
        extension = get_extension(file)
        destination = config["processed_folder"] + "/" + category + "/" + extension
        os.makedirs(destination, exist_ok=True)

        final_path = move_file(file, config["input_folder"], destination)

        log_file.write(f"{file} has been processed")

        processed_count+=1
        processed_files.append(f"{file} moved from {config["input_folder"]} to {final_path}.")
    else:
        final_q_path = move_file(file, config["input_folder"], config["quarantine_folder"])

        log_file.write(f"{file} has been quarantined")

        quarantined_count+=1
        quarantined_files.append(f"{file} moved from {config["input_folder"]} to {final_q_path}.")

log_file.close()
summary(config, processed_files, quarantined_files, processed_count, quarantined_count)