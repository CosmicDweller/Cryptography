from Permutations.permutations import S5
from logic import *

class Program:
    def __init__(self, instructions, permutation):
        self.instructions = instructions
        self.permutation = permutation

    def conjugateProgram(self, tau):
        phi = S5.find_conjugator(self.permutation, tau)
        phi_inv = phi.inverse()
        new_instructions = [(i[0], phi*i[1]*phi_inv, phi*i[2]*phi_inv) for i in self.instructions]

        return Program(new_instructions, tau)

    def __str__(self):
        return f"Program({self.instructions}, {self.permutation})"


x0 = Symbol("x0", 0)
x1 = Symbol('x1', 1)
x2 = Symbol('x2', 2)

g = S5([2, 3, 4, 5, 1])
h = S5([3, 1, 5, 2, 4])
e = S5([1, 2, 3, 4, 5])

my_program = Program([(1, g, h)], g)
# print(my_program)
# print(my_program.congugateProgram(h))
# symbols = [x1, x2]

xor = Not(And(Not(And(Not(x1), x2)), Not(And(x1, Not(x2)))))


not_x0 = Not(x2)

#test_reduced = test[4:-1]

#print(test_reduced)

# num_symbols = len(xor.symbols())

# print(xor.formula())
# print(xor.symbols())

def circuitToBP(circuit, num_symbols, curr_index = 0):
    if type(circuit) == Symbol:
        instructions = []
        while curr_index != circuit.index:
            print("Current index", curr_index)
            print("Circuit index", circuit.index)
            instructions.append((curr_index, e, e))
            curr_index = (curr_index + 1) % num_symbols
        return Program(instructions + [(circuit.index, g, e)], g)
    elif type(circuit) == Not:
        inner = circuit.operand
        BP = circuitToBP(inner, num_symbols, curr_index)
        sigma_inv = BP.permutation
        sigma = sigma_inv.inverse()
        index = (BP.instructions[-1][0] + 1) % num_symbols
        return Program(BP.instructions + [(index, sigma, sigma)], sigma)
    elif type(circuit) == And:
        left = circuit.conjuncts[0]
        right = circuit.conjuncts[1]
        BP_left = circuitToBP(left, num_symbols, curr_index)
        BP_right = circuitToBP(right, num_symbols, curr_index)
        P1 = BP_left.conjugateProgram(g)
        P2 = BP_right.conjugateProgram(h)
        P1_prime = BP_left.conjugateProgram(g.inverse())
        P2_prime = BP_right.conjugateProgram(h.inverse())
        P1P2_pad, P2P1_prime_pad, P1_primeP2_prime_pad = [], [], []
        P1_end = P1.instructions[-1][0]
        P2_start = P2.instructions[0][0]
        curr_index = (P1_end + 1) % num_symbols
        while curr_index != P2_start:
            P1P2_pad.append((curr_index, e, e))
            curr_index = (curr_index + 1) % num_symbols

        P2_end = P2.instructions[-1][0]
        P1_prime_start = P1_prime.instructions[0][0]
        curr_index = (P2_end + 1) % num_symbols
        while curr_index != P1_prime_start:
            P2P1_prime_pad.append((curr_index, e, e))
            curr_index = (curr_index + 1) % num_symbols

        P1_prime_end = P1_prime.instructions[-1][0]
        P2_prime_start = P2_prime.instructions[0][0]
        curr_index = (P1_prime_end + 1) % num_symbols
        while curr_index != P2_prime_start:
            P1_primeP2_prime_pad.append((curr_index, e, e))
            curr_index = (curr_index + 1) % num_symbols

        return Program(P1.instructions + P1P2_pad + P2.instructions + P2P1_prime_pad + P1_prime.instructions + P1_primeP2_prime_pad + P2_prime.instructions,
                       g*h*g.inverse()*h.inverse())
    else:
        raise ValueError("circuit must be Symbol or Not or And.")


def evalBP(program, bit_string):
    curr_vertex = 1

    for instruction in program.instructions:
        index = instruction[0]

        bit = bit_string[index % len(bit_string)]

        if bit == 1:
            curr_vertex = instruction[1](curr_vertex)
        else:
            curr_vertex = instruction[2](curr_vertex)

    return curr_vertex

nand = Not(And(x0, x1))
nand_BP = circuitToBP(nand, len(nand.symbols()))
print(nand_BP)
print(evalBP(nand_BP, [1, 1]))
# #
# not_x0_circuit = circuitToBP(not_x0, 3)
# print(not_x0_circuit)
# print(evalBP(not_x0_circuit, [0]))

