import os
from Validating_names import validation
from File_mover import move_file
input_file = os.listdir("input")

for file in input_file:
    if validation(file) == True:
        move_file(file, "processed")
    else:
        move_file(file, "quarantine")


print("\nProcessed files:")
print(os.listdir("processed"))

print("\nQuarantined files:")
print(os.listdir("quarantine"))