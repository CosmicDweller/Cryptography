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

print(modular_inverse(38039825031240215963665, 124924729789241929438904))

print((38039825031240215963665 * 19356555458892007097449) % 124924729789241929438904)