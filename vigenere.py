from sys import argv
import os

key = argv[1].upper()
plain_text = open('plaintext.txt', 'r')

cipher_text = None

if not os.path.exists('ciphertext.txt'):
    cipher_text = open('ciphertext.txt', 'x+')
else:
    cipher_text = open('ciphertext.txt', 'w')

key_len = len(key)

lines = plain_text.readlines()

cipher_lines = []

index = 0

for line in lines:
    cipher_line = ""
    for i in range(len(line)):
        char = line[i].upper()
        if char.isalpha():
            code = ((ord(char) - 65 + ord(key[index % key_len]) - 65) % 26) + 65
            cipher_line += chr(code)
            index += 1
        else:
            cipher_line += char
    cipher_lines.append(cipher_line)
    
cipher_text.writelines(cipher_lines)
cipher_text.close()
plain_text.close()