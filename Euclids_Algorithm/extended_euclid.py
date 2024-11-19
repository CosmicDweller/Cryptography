def extended_gcd(a,b):
    """
    :param a: any integer
    :param b: any integer
    :return: a list with a tuple containing a solution to the linear diophantine equation ax + by = gcd(a, b)
            and gcd(a, b)
    """

    s = [1, 0]
    t = [0, 1]
    r = [a, b]

    while r[1] != 0:
        q = r[0] // r[1]
        r[0], r[1] = r[1], r[0] - q * r[1]
        s[0], s[1] = s[1], s[0] - q * s[1]
        t[0], t[1] = t[1], t[0] - q * t[1]
    return (s[0], t[0]), r[0]

a = 12
b = 754
result = extended_gcd(a, b)

print(f"Solution: ({a} * {result[0][0]}) + ({b} * {result[0][1]}) =  {result[1]}")
print(f"Where {result[1]} is the gcd of {a} and {b}")

