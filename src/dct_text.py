import numpy as np
from scipy.fftpack import dct

def dct_text_compress(text, block_size=8):
    # ubah teks ke array byte
    data = np.frombuffer(text.encode(), dtype=np.uint8)

    # padding supaya habis dibagi block
    padding = (-len(data)) % block_size
    data = np.pad(data, (0, padding), mode='constant')

    # reshape ke blok
    blocks = data.reshape(-1, block_size)

    # DCT per blok
    dct_blocks = dct(blocks, axis=1, norm='ortho')

    return dct_blocks
