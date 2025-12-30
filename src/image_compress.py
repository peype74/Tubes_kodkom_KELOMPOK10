import cv2
import numpy as np
import math

def compress_image(image_path):
    # baca gambar grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float32)

    # DCT
    dct_img = cv2.dct(img)

    # quantization sederhana
    quant = np.round(dct_img / 10)
    dequant = quant * 10

    # inverse DCT
    idct_img = cv2.idct(dequant)

    return img, idct_img

def psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return 100
    return 20 * math.log10(255.0 / math.sqrt(mse))
