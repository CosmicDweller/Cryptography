from sys import argv
import numpy as np

cipher_txt = argv[1]

q = np.zeros(26)
p = [.082, .015, .028, .043, .127, .022, .02, .061, .07, .002, .008, .04, .024, .067, .015, .019, .001, .06, .063, .091, .028, .01, .024, .002, .02, .001]

num = 0

for n in p:
    num += n**2
    

for char in cipher_txt:
    q[ord(char.upper()) - ord('A')] += 1
    
q = q / len(cipher_txt)

total = 0

sums = []

for i in range(26):
    i_j = 0
    for j in range(26):
        i_j += p[j] * q[(j + i) % 26]
    
    sums.append([i_j, i])
    
shift = sums[0]

for i in range(1, len(sums)):
    if abs(shift[0] - num) > abs(sums[i][0] - num):
        shift = sums[i]

plaintext = ""

for char in cipher_txt:
    char_code = (((ord(char.upper()) - 65) - shift[1]) % 26) + 65
    plaintext += chr(char_code)
    
print(plaintext)