import os
from Validating_names import validation
input_file = os.listdir("input")

for file in input_file:
    if validation(file) == True:
        print(f"{file} is valid")
    else:
        print(f"{file} is invalid")
