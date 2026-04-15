import os
import json
from Validating_names import validation
from File_mover import move_file

with open("config.json", "r") as config_file:
    config = json.load(config_file)

input_folder = os.listdir(config["input_folder"])
log_file = open(f"{config['logs_folder']}/log.txt", "w")
processed_count = 0
quarantined_count = 0

for file in input_folder:
    if validation(file) == True:
        move_file(file, config["input_folder"], config["processed_folder"])
        log_file.write(f"{file} has been processed")
        processed_count+=1
    else:
        move_file(file, config["input_folder"], config["quarantine_folder"])
        log_file.write(f"{file} has been quarantined")
        quarantined_count+=1

log_file.close()

print("\nSimple summary:")
print("\nProcessed files:")
print(os.listdir(config["processed_folder"]))
print(f"Total processed files: {processed_count}")

print("\nQuarantined files:")
print(os.listdir(config["quarantine_folder"]))
print(f"Total quarantined files: {quarantined_count}")