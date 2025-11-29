
from enum import Enum

def markdown_to_blocks(markdown):
    block_texts_raw = markdown.split("\n\n")
    block_texts = []
    for raw_block in block_texts_raw:
        block_texts.append(raw_block.strip())

    blocks = []
    for block in block_texts:
        if block != "" and block != "\n":
            blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list" 

def block_to_block_type(block):
    if (
        block.startswith("# ") or
        block.startswith("## ") or
        block.startswith("### ") or
        block.startswith("#### ") or
        block.startswith("##### ") or
        block.startswith("###### ") 
    ):
        return BlockType.HEADING


    if len(block) >= 6:
        if (
            block.startswith("```") and
            block.endswith("```")
        ):
            return BlockType.CODE
        
    lines = block.split("\n")

    quote = True
    unordered = True
    ordered = True

    line_count = 0
    for line in lines:
        line_count += 1
        if len(line) > 0:
            if line.startswith(">"):
                pass
            else:
                quote = False

            if line.startswith("- "):
                pass
            else:
                unordered = False
 
            if line.startswith(f'{line_count}. ') and len(line) >= len(f'{line_count}. ') + 1:
                pass
            else:
                ordered = False
        else:
            quote = False
            unordered = False
            ordered = False

    
    if quote:
        return BlockType.QUOTE
    if unordered:
        return BlockType.UNORDERED_LIST
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH 
