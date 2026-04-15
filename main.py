import os
from Validating_names import validation
from File_mover import move_file
input_file = os.listdir("input")
log_file = open("logs/log.txt", "w")

for file in input_file:
    if validation(file) == True:
        move_file(file, "processed")
        log_file.write("f{file} has been processed")
    else:
        move_file(file, "quarantine")
        log_file.write(f"{file} has been quarantined")

log_file.close()

print("\nProcessed files:")
print(os.listdir("processed"))

print("\nQuarantined files:")
print(os.listdir("quarantine"))