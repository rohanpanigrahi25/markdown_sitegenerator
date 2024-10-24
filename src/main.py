import os
import shutil

#from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def main():
    copy_static('./static', './public')
    generate_pages_recursive('./content/', './template.html', './public/')



def copy_static(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)

        #If it's a file, copy it to the destination
        if os.path.isfile(file_path) or os.path.islink(file_path):
            shutil.copy(file_path, destination_path)

        # If it's a directory, create subdirectories in the destination
        elif os.path.isdir(file_path):
            destination_sub_dir = os.path.join(destination_path, filename)
            os.mkdir(destination_sub_dir)
            copy_static(file_path, destination_sub_dir)
        print(f"Copying {file_path} to {destination_path}")

main()