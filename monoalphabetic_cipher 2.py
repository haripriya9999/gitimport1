import sys
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

def generate_permutation(seed):
    random.seed(seed)
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    mapping = list(alphabet)
    random.shuffle(mapping)
    return mapping

def encrypt(plaintext, mapping):
    ciphertext = ''
    for char in plaintext:
        index = alphabet.index(char)
        ciphertext += mapping[index]
    return ciphertext

def decrypt(ciphertext, mapping):
    plaintext = ''
    for char in ciphertext:
        index = mapping.index(char)
        plaintext += alphabet[index]
    return plaintext

def main(inputfile, outputfile, seed, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    mapping = generate_permutation(seed)
    print("Mapping: ", end="")
    for i, j in enumerate(mapping):
        print(f"{alphabet[i]}-{j}", end=", " if i < len(alphabet) - 1 else "\n")
    with open(inputfile, 'r') as f:
        plaintext = f.read()
    if mode == 1:
        ciphertext = encrypt(plaintext, mapping)
    else:
        ciphertext = decrypt(plaintext, mapping)
    with open(outputfile, 'w') as f:
        f.write(ciphertext)

if __name__ == '__main__':
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    seed = int(sys.argv[3])
    mode = int(sys.argv[4])
    main(inputfile, outputfile, seed, mode)
