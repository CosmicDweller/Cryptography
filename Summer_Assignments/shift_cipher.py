from sys import argv

shift = int(argv[1])
code = input("Enter plain text: ")


cipher_text = ""

for char in code:
    if ord(char.upper()) in range(65, 91):
        num = (((ord(char.upper()) - 65) + shift) % 26) + 65
        cipher_text += chr(num)
        
print(cipher_text)