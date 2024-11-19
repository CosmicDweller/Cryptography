import random
import sys
sys.path.insert(1, '/Users/kvberry/Cryptography')

from  Modular_Exponentiation.mod_exponentiate import mod_exponentiate
# n is the order of the cyclic group G which we are working in
n = 124924729789241929438904
# n = int(input("provide a large number on preferably of the order 2^2000: "))

# g is a public key visible to everyone that we will use to generate each private key
g = 65537
# g = int(input("provide a large prime less than n: "))

def diffie_hellman(n, g):
    """
    :param n: a large positive integer
    :param g: a prime less than n and not equal to 1
    :return: None (prints output of each step of Diffie Hellman Key Algorithm to terminal)
    """

    # generate private keys for both parties
    alice_key = random.randint(1, n)
    bob_key = random.randint(1, n)
    print("Alice's private key:", alice_key)
    print("Bob's private key:", bob_key)
    print()

    # compute g^x, g^y which are messages which will be sent publicly
    alice_num = mod_exponentiate(g, alice_key, n)
    bob_num = mod_exponentiate(g, bob_key, n)
    print("Alice's message:", alice_num)
    print("Bob's message:", bob_num)
    print()

    # identical keys that can be used for public communication
    alice_shared_key = mod_exponentiate(bob_num, alice_key, n)
    bob_shared_key = mod_exponentiate(alice_num, bob_key, n)
    print("Alice's version of shared key:", alice_shared_key)
    print("Bob's version of shared key:", bob_shared_key)

diffie_hellman(n, g)