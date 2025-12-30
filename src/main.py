from huffman import huffman_compress
from lzw import lzw_compress
from metrics import entropy
from dct_text import dct_text_compress

text = "ini adalah contoh teks untuk kompresi data"

print("Entropy sumber:", entropy(text))

# Huffman
encoded_huff, _ = huffman_compress(text)
print("\n=== HUFFMAN ===")
print(encoded_huff)

# LZW
encoded_lzw = lzw_compress(text)
print("\n=== LZW ===")
print(encoded_lzw)

# DCT
dct_result = dct_text_compress(text)
print("\n=== DCT ===")
print(dct_result)
