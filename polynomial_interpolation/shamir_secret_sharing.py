import numpy as np
import random
import math

# D = int(input("D: "))
D = 219
# n = int(input("n: "))
n = 10
# p = int(input("p: "))
p = 35951863
# k = int(input("k: "))
k = 4

if n < (2*k - 1):
    print("n must be greater than or equal to 2*k - 1")
    k = int(input("k: "))
elif n > p or D > p:
    print("n and D must be less than p")
    p = int(input("p: "))
else:
    poly = [D]
    for i in range(1, k):
        a = random.randint(1, p)
        poly.append(a)
    shares = []
    for i in range(1, n + 1):
        share_i = 0
        for j in range(k):
            share_i += int(math.pow(i, j) * poly[j])
        shares.append((share_i % p))

    for i in range(1, n + 1):
        print(f"Key {i}: {shares[i - 1]}")


