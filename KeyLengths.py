import re
from collections import defaultdict
def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()
def kasiski_method(ciphertext):
    distances = []
    for i in range(len(ciphertext) - 3):
        pattern = ciphertext[i:i+3]
        for j in range(i + 3, len(ciphertext) - 3):
            if ciphertext[j:j+3] == pattern:
                distances.append(j - i)
    gcds = []
    for dist in distances:
        for i in range(2, dist + 1):
            if dist % i == 0:
                gcds.append(i)
    freq = defaultdict(int)
    for gcd in gcds:
        freq[gcd] += 1
    common_lengths = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return common_lengths
ciphertext = read_file('tajnopis')
key_lengths = kasiski_method(ciphertext)
print("Suggested key lengths:", key_lengths)
