import numpy as np

txt_file = open('ciphertext.txt', 'r')

lines = txt_file.readlines()

frequencies = np.zeros(26)

length = 0

for line in lines:
    for char in line:
        if char.isalpha():
            length += 1
            frequencies[ord(char.upper()) - 65] += 1

frequencies /= length
frequencies = frequencies ** 2

freq_sum = sum(frequencies)

            
print(freq_sum)

txt_file.close()