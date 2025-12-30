from huffman import huffman_compress
from lzw import lzw_compress
from metrics import entropy
from dct_text import dct_text_compress

text = "contoh teks untuk kompresi data"

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

# ===== TOPIK 3 : VIDEO COMPRESSION =====
# from video_compress import compress_video, calculate_bitrate
# compress_video("data/input.avi", "data/output.avi")
# print("Video bitrate:", calculate_bitrate("data/output.avi"))


# ===== TOPIK 2 : IMAGE COMPRESSION =====
# from image_compress import compress_image, psnr
# img_original, img_compressed = compress_image("data/sample.jpg")
# print("PSNR Image:", psnr(img_original, img_compressed))
