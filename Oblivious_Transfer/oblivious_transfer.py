import random
import sys
sys.path.insert(1, '/Users/kvberry/Cryptography')

from  ..Modular_Exponentiation.mod_exponentiate import mod_exponentiate
# n is the order of the cyclic group G which we are working in
n = 124924729789241929438904
# n = int(input("provide a large number on preferably of the order 2^2000: "))

# g is a public key visible to everyone that we will use to generate each private key
g = 65537
# g = int(input("provide a large prime less than n: "))

def modular_inverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse of a under mod m
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def oblivious_transfer(n, g):
    """
    Simulates 1-out-of-2 Oblivious Transfer using Diffie-Hellman.
    """

    # alice and bobs private keys
    alice_key = random.randint(1, n)
    bob_key = random.randint(1, n)
    print("Alice's private key:", alice_key)
    print("Bob's private key:", bob_key)
    print()

    # first Alice sends a message g^a to bob
    alice_message = mod_exponentiate(g, alice_key, n)
    print("Alice's message:", alice_message)
    print()

    # bob choose a random bit, either 0 or 1
    bob_bit = random.randint(0,1)
    print("Bob's bit:", bob_bit)

    # based on bobs bit bob does one of two computations and sends it to alice
    if bob_bit:
        bob_message = (alice_message * mod_exponentiate(g, bob_key, n)) % n
        print("Bob's message", bob_message)
        print()
    else:
        bob_message = mod_exponentiate(g, bob_key, n)
        print("Bob's message", bob_message)
        print()

    # then alice computes two key
    alice_key0 = mod_exponentiate(bob_message, alice_key, n)
    alice_key1 = mod_exponentiate((bob_message * modular_inverse(alice_message, n)), alice_key, n)
    print("Alice's key #1:", alice_key0)
    print("Alice's key #2:", alice_key1)
    print()

    # bob can only compute one of these keys
    bob_key_r = mod_exponentiate(alice_message, bob_key, n)
    print("Bob's key r:", bob_key_r)

oblivious_transfer(n, g)