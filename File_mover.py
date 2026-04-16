import os
import shutil

def move_file(filename, source, destination):
    current_destination = os.path.join(source, filename)
    moved_destination = os.path.join(destination, filename)

    counter = 1
    while os.path.exists(moved_destination):
        name, ext = os.path.splitext(filename)
        new_filename= f"{name}_{counter}{ext}"
        moved_destination = os.path.join(destination, new_filename)
        counter +=1

    shutil.move(current_destination, moved_destination)

    return moved_destination
