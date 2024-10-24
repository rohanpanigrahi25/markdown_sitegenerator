import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, filename)

        if os.path.isfile(file_path) and file_path.endswith('.md'):
            dest_path = os.path.join(dest_dir_path, 'index.html')
            generate_page(file_path, template_path, dest_path)

        elif os.path.isdir(file_path):
            destination_sub_dir = os.path.join(dest_dir_path, filename)
            os.makedirs(destination_sub_dir, exist_ok=True)
            generate_pages_recursive(file_path, template_path, destination_sub_dir)