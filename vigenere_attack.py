import numpy as np
import os

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cipher_text = open('ciphertext.txt', 'r').read()

shift = None

dup_cipher_text = ''

for char in cipher_text:
    if char.isalpha():
        dup_cipher_text += char


decipher_text = None
if os.path.exists('deciphered.txt'):
    decipher_text = open('deciphered.txt', 'w')
else:
    decipher_text = open('deciphered.txt', 'x+')

q_sums = []

for t in range(2, 100):
    index = 0
    q = np.zeros(26)
    for j in range(0, len(dup_cipher_text), t):
        index += 1
        char = dup_cipher_text[j]
        if char.isalpha():
            q[ord(char) - 65] += 1

    q = (q / index) ** 2
    q_sum = sum(q)
    q_sums.append([t, q_sum])
    
delta = 0.005
i = 0
diff = abs(0.065 - q_sums[i][1])

while diff > delta:
    i += 1
    diff = abs(0.065 - q_sums[i][1])
    
shift = q_sums[i][0]

shifted_alphabets = []

for i in range(shift):
    shifted_alphabet = []
    for j in range(i, len(dup_cipher_text), shift):
        shifted_alphabet.append(dup_cipher_text[j])
    shifted_alphabets.append(shifted_alphabet)

def frequency_sum(text):
    p = [.082, .015, .028, .043, .127, .022, .02, .061, .07, .002, .008, .04, .024, .067, .015, .019, .001, .06, .063, .091, .028, .01, .024, .002, .02, .001]
    frequency = np.zeros(26)
    
    for letter in text:
        frequency[ord(letter) - 65] += 1
    
    frequency /= len(text)
    
    f_sums = []
    
    for i in range(26):
        f_sum = 0
        for j in range(26):
            f_sum += p[j] * frequency[(j + i) % 26]
        f_sums.append([i, f_sum])
        
    fshift = f_sums[0]

    for i in range(1, len(f_sums)):
        if abs(fshift[1] - 0.065) > abs(f_sums[i][1] - 0.065):
            fshift = f_sums[i]
    
    return fshift[0]
     
deciphered_alphabets = []
    
for i in range(len(shifted_alphabets)):
    deciphered_alphabet = []
    shift_num = frequency_sum(shifted_alphabets[i])
    for char in shifted_alphabets[i]:
        char_num = (ord(char) - 65 - shift_num) % 26
        
        deciphered_alphabet.append(letters[char_num])
    deciphered_alphabets.append(deciphered_alphabet)
        
completed_deciphered_alphabet = ''
    
    
for i in range(0, len(dup_cipher_text)):
    completed_deciphered_alphabet += deciphered_alphabets[i % shift][0]
    deciphered_alphabets[i % shift].pop(0)

chr_index = 0

for char in cipher_text:
    if char.isalpha():
        decipher_text.write(completed_deciphered_alphabet[chr_index])
        chr_index += 1
    else:
        decipher_text.write(char)