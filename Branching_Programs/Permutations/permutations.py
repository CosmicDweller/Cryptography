import numpy as np


class S5:
    def __init__(self, permutation):
        if type(permutation) == S5:
            self.permutation = np.array(permutation.permutation)
        else:
            self.permutation = np.array(permutation)

    def inverse(self):
        inverse = self.permutation.copy()
        for i in range(5):
            inverse[self.permutation[i] - 1] = i + 1
        return S5(inverse)

    @staticmethod
    def composition(b, a):
        composition = np.ones(5).astype(int)
        for i in range(5):
            composition[i] = b.permutation[a.permutation[i] - 1]
        return S5(composition)

    @staticmethod
    def from_5_cycle(cycle):
        perm = np.ones(5).astype(int)

        for i in range(5):
            perm[cycle.permutation[i] - 1] = cycle.permutation[(i + 1)%5]
        return S5(perm)

    def cycles(self):
        values = [1,2,3,4,5]
        def get_cycle(i):
            cycle = [i]
            g = i
            while self(g) != i:
                g = self(g)
                cycle.append(g)
            for j in cycle:
                values.remove(j)
            return tuple(cycle)
        cycles=[]
        while len(values) > 0:
            cycles.append(get_cycle(values[0]))
        return cycles


    @staticmethod
    def find_conjugator(sigma, tau):
        """Return phi such that phi sigma phi^-1 = tau"""
        assert type(sigma) == S5 and type(tau) == S5
        phi_inv_perm = np.ones(5).astype(int)
        tau_cycle = np.array(tau.cycles()).flatten()
        sigma_cycle = np.array(sigma.cycles()).flatten()
        
        for i in range(5):
            for j in range(5):
                if tau_cycle[j] == i + 1:
                    phi_inv_perm[i] = sigma_cycle[j]

        phi_inv = S5(phi_inv_perm)
        phi = phi_inv.inverse()

        return phi

    def __mul__(self, other):
        return S5.composition(self, other)

    def __invert__(self):
        return self.inverse()

    def __str__(self):
        return str(self.permutation)

    __repr__ = __str__

    def __call__(self, n):
        if n not in (1,2,3,4,5):
            raise ValueError("n must be 1, 2, 3, 4, or 5")
        return int(self.permutation[n-1])

# simple permutation shifting every element by one
g = S5([2, 3, 4, 5, 1])

# another more complex permutation
h = S5([3, 1, 5, 2, 4])

c = S5([3, 1, 4, 2, 5])

# print(S5.from_5_cycle(c))
#
# print(g.cycles())
# print(h.cycles())
# print(S5([1,3,5,4,2]).cycles())
#
# # finds the inverse of g
# print(g, ~g)
# # finds the inverse of h
# print(h, ~h)
#
# # finds the composition of g and h (g*h)
# print(g*h)
#
# finds phi s.t. phi*g*phi^-1 = h
phi=S5.find_conjugator(g, h)
# print(phi, phi*(g*(~phi)), h)

# print(g(h(1)), (g*h)(1))
# print(g(h(2)), (g*h)(2))
# print(g(h(3)), (g*h)(3))
# print(g(h(4)), (g*h)(4))
# print(g(h(5)), (g*h)(5))