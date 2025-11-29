from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnode(text):
    new_nodes = []
    old_nodes = [TextNode(text, TextType.TEXT)]
    bold_pass = split_nodes_delimiter(old_nodes,'**', TextType.BOLD)
    italic_pass = split_nodes_delimiter(bold_pass,'_', TextType.ITALIC)
    code_pass = split_nodes_delimiter(italic_pass,'`', TextType.CODE)
    link_pass =  split_nodes_link(code_pass)
    new_nodes = split_nodes_image(link_pass)

    return new_nodes
