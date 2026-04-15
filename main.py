import os
from Validating_names import validation
from File_mover import move_file

input_file = os.listdir("input")
log_file = open("logs/log.txt", "w")
processed_count = 0
quarantined_count = 0

for file in input_file:
    if validation(file) == True:
        move_file(file, "processed")
        log_file.write(f"{file} has been processed")
        processed_count+=1
    else:
        move_file(file, "quarantine")
        log_file.write(f"{file} has been quarantined")
        quarantined_count+=1

log_file.close()

print("\nSimple summary:")
print("\nProcessed files:")
print(os.listdir("processed"))
print(f"Total processed files: {processed_count}")

print("\nQuarantined files:")
print(os.listdir("quarantine"))
print(f"Total quarantined files: {quarantined_count}")