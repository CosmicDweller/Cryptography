#!python
import numpy as np
import galois
import math

# from namex import export

p = 35951863
GF = galois.GF(p)

k = int(input("k: "))

points = []

for i in range(k):
    x = GF(int(input("x: ")) % p)
    y = GF(int(input("y: ")) % p)
    points.append([x, y])

a = []
# b = []

for i in range(k):
    # b.append(points[i][1])
    eqn = []
    for j in range(k):
        eqn.append(pow(points[i][0], j))
        #peval([], j)
    eqn.append(points[i][1])
    a.append(eqn)
augmented_matrix = GF(np.array(a))
# sols = GF(np.array(b))
rref_matrix =  augmented_matrix.row_reduce()
coefficients = []
for i in range(len(rref_matrix)):
    coefficients.append(rref_matrix[i][-1])

# coefficients = np.linalg.solve(augmented_matrix, sols)
print('y = ', end='')
for i in range(k):
    print(str(coefficients[k - i - 1]) + f"x^{k - i - 1} + ", end='')


# def peval(poly, a):
#     sum([pow(a,i) for i in range(len(poly))])