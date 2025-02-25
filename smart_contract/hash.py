from hashlib import sha256
passwords = ["123notme", "verysecurepassword", "funnypassword1", "unguessable983", "dilapidated463", "123456789", "31415926535"]

sha256 = sha256()

hashes = []

for password in passwords:
    byte_stream = password.encode('utf-8')
    sha256.update(byte_stream)
    hash = sha256.hexdigest()
    hashes.append(hash)

print(hashes)
