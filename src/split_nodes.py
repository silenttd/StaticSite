import re
from textnode import TextNode, TextType, extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # 1. only operate on plain text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # 2. if no delimiter, just keep as is
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # 3. invalid markdown if delimiters are not in pairs
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown, missing closing delimiter")

        # 4. rebuild nodes from parts
        for i, part in enumerate(parts):
            if part == "":
                continue  # never create empty TextNodes

            if i % 2 == 0:
                # outside delimiters
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # inside delimiters
                new_nodes.append(TextNode(part, text_type))      

    return new_nodes
                    
def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT: # Only process Plain Text. Other TextTypes pass through unaltered into new_nodes
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text) # Creates list images in format [(alt_text,url), (alt_text,url), ...]
        


        current_text = node.text

        for image in images: # Go through each image reference that are in images

            alt_text = image[0]
            url = image[1]
            before_after = current_text.split(f"![{alt_text}]({url})", 1) # Creates before/after
            before = before_after[0]
            after = before_after[1]
            current_text = after
            if before == "":
                new_nodes.append(TextNode(alt_text,TextType.IMAGE,url)) 
                
            else:
                new_nodes.append(TextNode(before,TextType.TEXT))
                new_nodes.append(TextNode(alt_text,TextType.IMAGE,url)) 
        if current_text != "":
            new_nodes.append(TextNode(current_text,TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT: # Only process Plain Text. Other TextTypes pass through unaltered into new_nodes
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text) # Creates list images in format [(alt_text,url), (alt_text,url), ...]
        


        current_text = node.text

        for link in links: # Go through each image reference that are in images

            alt_text = link[0]
            url = link[1]
            before_after = current_text.split(f"[{alt_text}]({url})", 1) # Creates before/after
            before = before_after[0]
            after = before_after[1]
            current_text = after
            if before == "":
                new_nodes.append(TextNode(alt_text,TextType.LINK,url)) 
                
            else:
                new_nodes.append(TextNode(before,TextType.TEXT))
                new_nodes.append(TextNode(alt_text,TextType.LINK,url)) 
        if current_text != "":
            new_nodes.append(TextNode(current_text,TextType.TEXT))

    return new_nodes





    
