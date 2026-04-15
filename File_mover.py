import os
import shutil

def move_file(filename, destination):
    current_destination = os.path.join("input", filename)
    moved_destination = os.path.join(destination, filename)

    shutil.move(current_destination, moved_destination)
