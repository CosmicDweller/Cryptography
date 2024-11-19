# import time
# a = int(input("Enter an integer a: "))
# b = int(input("Enter an integer b: "))
# m = int(input("Enter an integer m: "))


# def modulo(a, m):
    # j = 1

    # while (j*m) < a:
    #     j += 1

    # return a - (a//m)

# print("Calcutaing...")

# now = time.time()
# # print(pow(a%m,b))
# a % m
# print(time.time() - now)

# now = time.time()
# # print(pow(a%m,b))
# modulo(a, m)
# print(time.time() - now)

# now = time.time()
# prod = 1
# for i in range(b):
#     prod *= a
# print(time.time() - now)

def mod_exponentiate(a, b, m):
    """
    :param a: any integer
    :param b: any integer
    :param m: any integer
    :return: an integer in [0,m-1] congruent to a^b mod m
    """
    if b < 0:
        raise NotImplementedError
        # return mod_exponentiate((1 / a) % m, -b, m) % m
    elif b == 0:
        return 1
    elif b % 2 == 1:
        return ((a % m) * (mod_exponentiate((a * a) % m, (b - 1) // 2, m) % m) ) % m
    elif b % 2 == 0:
        return mod_exponentiate((a * a) % m, b // 2, m) % m

# def naive_approach(a, b, m):
#     a = a % m
#     exp = exponentiate(a, b)

#     return exp % m



# now = time.time()
# res1 = pow(a, b, m)
# end = time.time() - now
# print("\nBultin implmentation:", pow(a, b, m), "| took", end)
# now = time.time()
# # res2 = naive_approach(a, b, m)
# res2 = mod_exponentiate(a % m, b, m)
# end = time.time() - now
# print("\nMy implementation:", mod_exponentiate(a % m, b, m), "| took", end)
# print()