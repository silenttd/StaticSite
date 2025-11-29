import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlock(unittest.TestCase):    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_HEADING(self):
        block = "### Welcome to the Dungeon"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.HEADING,
        )

    def test_block_to_block_type_CODE(self):
        block = '```    def test_block_to_block_type_HEADING(self):\n        block = "### Welcome to the Dungeon"\n        block_type = block_to_block_type(block)\n        self.assertEqual(\n            block_type,\n            BlockType.HEADING,\n        )```'
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.CODE,
        )

    def test_block_to_block_type_QUOTE(self):
        block = "> Wise words\n> from the ancient tome"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.QUOTE,
        )

    def test_block_to_block_type_UNORDERED(self):
        block = "- Wise words\n- from the ancient tome"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST,
        )

    def test_block_to_block_type_ORDERED(self):
        block = "1. Wise words\n2. from the ancient tome"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST,
        )



if __name__ == "__main__":
    unittest.main()