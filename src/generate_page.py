import os
from markdown_to_html import markdown_to_html_node
from pathlib import Path
from main import basepath

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("No H1 header in Markdown")

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path}, using {template_path}')
    with open(from_path) as markdown:
        md_content = markdown.read()

    
    with open(template_path) as template:
        template_content = template.read()


    html = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)

    new_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dir_path = os.path.dirname(dest_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_html)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Step 1: List everything in the content directory
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        
        if os.path.isfile(src_path):
            # It's a file - check if it's markdown
            if src_path.endswith(".md"):
                # Convert .md to .html path
                html_path = dest_path.replace(".md", ".html")
                
                # Generate the HTML page
                generate_page(src_path, template_path, html_path)
                print(f"Generated page: {html_path}")
        else:
            # It's a directory - create it in dest if it doesn't exist
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            
            # Recursively process this directory
            generate_pages_recursive(src_path, template_path, dest_path)
    




    
    

