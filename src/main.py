from huffman import huffman_compress
from lzw import lzw_compress
from metrics import entropy

text = "ini adalah contoh teks untuk kompresi data"

print("Entropy sumber:", entropy(text))

encoded_huff, _ = huffman_compress(text)
encoded_lzw = lzw_compress(text)

print("\n=== HUFFMAN ===")
print("Hasil encoding:", encoded_huff)

print("\n=== LZW ===")
print("Hasil encoding:", encoded_lzw)
