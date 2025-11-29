from textnode import TextNode, TextType
from htmlnode import LeafNode
from migrate_static import copy_directory
from generate_page import generate_page, generate_pages_recursive

def main():
    source = "static"
    destination = "public"
    copy_directory(source, destination)

    dir_path_content = "content"
    template_path = "template.html"
    dest_dir_path = "public"
    
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

main()