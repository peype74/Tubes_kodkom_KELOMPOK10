from huffman import huffman_compress

# contoh teks uji
text = "ini adalah contoh teks untuk kompresi huffman"

encoded, codes = huffman_compress(text)

print("Teks asli       :", text)
print("Teks terkompres :", encoded)
print("Kode Huffman    :", codes)
