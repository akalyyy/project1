import os
import json
from Validating_names import validation
from File_mover import move_file
from File_sorting import get_category, get_extension
from Report_summary import summary

try:
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    print("config loaded successfully.")
except FileNotFoundError:
    print("Error: config.json was not found.")
    raise
except json.JSONDecodeError:
    print("Error: config.json is not valid JSON.")
    raise

for key in ["input_folder", "processed_folder", "quarantine_folder", "reports_folder", "logs_folder"]:
    value = config[key]

    if not os.path.exists(value):
        os.makedirs(value)
        print(f"Created mising folder: {value}")
    else:
        print(f"Folder {value} already exists.")

input_folder = os.listdir(config["input_folder"])
print(f"{len(input_folder)} files found in the input folder.")

log_file = open(f"{config['logs_folder']}/log.txt", "w")

processed_count = 0
quarantined_count = 0
archived_count = 0

processed_files = []
quarantined_files = []
archived_files = []

for file in input_folder:
    try:
        if validation(file) == True:
            category = get_category(file)
            extension = get_extension(file)
            destination = config["processed_folder"] + "/" + category + "/" + extension
            os.makedirs(destination, exist_ok=True)

            final_path = move_file(file, config["input_folder"], destination)

            log_file.write(f"{file} has been processed\n")

            processed_count+=1
            processed_files.append(f"{file} moved from {config['input_folder']} to {final_path}.")
        else:
            final_q_path = move_file(file, config['input_folder'], config['quarantine_folder'])

            log_file.write(f"{file} has been quarantined\n")

            quarantined_count+=1
            quarantined_files.append(f"{file} moved from {config["input_folder"]} to {final_q_path}.")
        
    except Exception as e:
        error_message = f"Error processing file {file}: {e}"
        print(error_message)
        log_file.write(error_message + "\n")

log_file.close()
summary(config, processed_files, quarantined_files, processed_count, quarantined_count)