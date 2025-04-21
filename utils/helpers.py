# utils/helpers.py

# Bir karakteri 8-bit binary string'e dönüştür
def char_to_binary(char):
    return format(ord(char), '08b')

# 8-bitlik binary string'i karaktere dönüştür
def binary_to_char(binary):
    return chr(int(binary, 2))

# Binary string'i 3 bitlik parçalar halinde böler (RGB için)
def split_into_triplets(binary_string):
    triplets = []
    for i in range(0, len(binary_string), 3):
        triplets.append(binary_string[i:i+3].ljust(3, '0'))
    return triplets
