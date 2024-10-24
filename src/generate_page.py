import os
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if os.path.exists(from_path) and os.path.exists(template_path):
        
        # Open and read the markdown file
        with open(from_path, 'r') as file:
            md_contents = file.read()
        
        # Open and read the template file
        with open(template_path, 'r') as file:
            html_contents = file.read()

    else:
        raise Exception(f"The given from-path:{from_path} and template-path:{template_path} does not exists")
    
    md_to_html_content = markdown_to_html_node(md_contents).to_html()
    title = extract_title(md_contents)
    html_contents = html_contents.replace('{{ Title }}', title)
    html_contents = html_contents.replace('{{ Content }}', md_to_html_content)

    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(html_contents)




    
