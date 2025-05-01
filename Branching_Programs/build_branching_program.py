from sympy.printing.maple import number_symbols

from Permutations.permutations import S5
from logic import *

class Program:
    def __init__(self, instructions, permutation):
        self.instructions = instructions
        self.permutation = permutation

    def conjugateProgram(self, tau):
        phi = ~S5.find_conjugator(self.permutation, tau)
        phi_inv = phi.inverse()
        new_instructions = [(i[0], phi*i[1]*phi_inv, phi*i[2]*phi_inv) for i in self.instructions]

        return Program(new_instructions, tau)

    def __str__(self):
        return f"Program({self.instructions}, {self.permutation})"

    def indexes(self):
        for instruction in self.instructions:
            print(instruction[0], end=' ')
        print()


x0 = Symbol("x0", 0)
x1 = Symbol('x1', 0)
x2 = Symbol('x2', 1)
x3 = Symbol('x3', 2)
x4 = Symbol('x4', 3)

g = S5([2, 3, 4, 5, 1])
h = S5([3, 1, 5, 2, 4])
e = S5([1, 2, 3, 4, 5])

# my_program = Program([(1, g, e)], g)
# print(my_program)
# print(my_program.conjugateProgram(h))
# # symbols = [x1, x2]

def xor(a, b): return Not(And(Not(And(Not(a), b)), Not(And(a, Not(b)))))

# xor = Not(And(Not(And(Not(x1), x2)), Not(And(x1, Not(x2)))))
# model_01 = {"x1":0, "x2":1}
# model_00 = {"x1":0, "x2":0}
# model_10 = {"x1":1, "x2":0}
# model_11 = {"x1":1, "x2":1}
# print(xor.evaluate(model_01))
# print(xor.evaluate(model_00))
# print(xor.evaluate(model_10))
# print(xor.evaluate(model_11))

not_x0 = Not(x2)

#test_reduced = test[4:-1]

#print(test_reduced)

# num_symbols = len(xor.symbols())

# print(xor.formula())
# print(xor.symbols())

def circuitToBP(circuit, num_symbols):
    if type(circuit) == Symbol:
        # instructions = []
        # while curr_index != circuit.index:
        #     print("Current index", curr_index)
        #     print("Circuit index", circuit.index)
        #     instructions.append((curr_index, e, e))
        #     curr_index = (curr_index + 1) % num_symbols
        return Program([(circuit.index, g, e)], g)
    elif type(circuit) == Not:
        inner = circuit.operand
        BP = circuitToBP(inner, num_symbols)
        sigma_inv = BP.permutation
        sigma = sigma_inv.inverse()
        index = (BP.instructions[-1][0] + 1) % num_symbols
        return Program(BP.instructions + [(index, sigma, sigma)], sigma)
    elif type(circuit) == And:
        left = circuit.conjuncts[0]
        right = circuit.conjuncts[1]
        BP_left = circuitToBP(left, num_symbols)
        BP_right = circuitToBP(right, num_symbols)
        P1 = BP_left.conjugateProgram(g)
        P2 = BP_right.conjugateProgram(h)
        P1_prime = BP_left.conjugateProgram(g.inverse())
        P2_prime = BP_right.conjugateProgram(h.inverse())
        # P1P2_pad, P2P1_prime_pad, P1_primeP2_prime_pad = [], [], []
        # P1_end = P1.instructions[-1][0]
        # P2_start = P2.instructions[0][0]
        # curr_index = (P1_end + 1) % num_symbols
        # while curr_index != P2_start:
        #     P1P2_pad.append((curr_index, e, e))
        #     curr_index = (curr_index + 1) % num_symbols
        #
        # P2_end = P2.instructions[-1][0]
        # P1_prime_start = P1_prime.instructions[0][0]
        # curr_index = (P2_end + 1) % num_symbols
        # while curr_index != P1_prime_start:
        #     P2P1_prime_pad.append((curr_index, e, e))
        #     curr_index = (curr_index + 1) % num_symbols
        #
        # P1_prime_end = P1_prime.instructions[-1][0]
        # P2_prime_start = P2_prime.instructions[0][0]
        # curr_index = (P1_prime_end + 1) % num_symbols
        # while curr_index != P2_prime_start:
        #     P1_primeP2_prime_pad.append((curr_index, e, e))
        #     curr_index = (curr_index + 1) % num_symbols

        return Program(P1.instructions + P2.instructions + P1_prime.instructions + P2_prime.instructions,
                       g*h*g.inverse()*h.inverse())
    else:
        raise ValueError("circuit must be Symbol or Not or And.")


def addPadding(program, num_symbols):
    new_program = program

    for i in range(len(program.instructions) - 1, 0, -1):
        curr_bit = program.instructions[i][0]
        prev_bit = program.instructions[i-1][0]
        while curr_bit != (prev_bit + 1) % num_symbols:
            new_program.instructions.insert(i, ((curr_bit - 1) % num_symbols, e, e))
            curr_bit = (curr_bit - 1) % num_symbols

    while new_program.instructions[0][0] != 0:
        new_program.instructions.insert(0, ((new_program.instructions[0][0] - 1)  % num_symbols, e, e))
    return new_program


def evalBP(program, bit_string):
    curr_vertex = 1

    for instruction in program.instructions:
        index = instruction[0]

        bit = bit_string[index]

        if bit == 1:
            curr_vertex = instruction[1](curr_vertex)
        else:
            curr_vertex = instruction[2](curr_vertex)

    return curr_vertex

# nand = Not(And(x0, x1))
# nand_BP = circuitToBP(nand, len(nand.symbols()))
# print(nand_BP)
# print(evalBP(nand_BP, [0, 0]))
# #
# and_circuit = And(x0, x1)
# and_BP = circuitToBP(and_circuit, len(and_circuit.symbols()))
# print(and_BP)
# print(evalBP(and_BP, [1, 1]))
# #
# not_x0_circuit = circuitToBP(not_x0, 3)
# print(not_x0_circuit)
# print(evalBP(not_x0_circuit, [0]))

# Givenstest=Program([(1,e,g),(0,g,h),(1,h,e)], h)
# # print(Givenstest)
# Givenstest.indexes()
# # print(addPadding(Givenstest, 3))
# addPadding(Givenstest,4).indexes()

majority = xor(And(xor(x1, x2), And(x3, x4)), And(And(x1,x2), xor(xor(And(x3, x4), x4), x3)))

# x1 is false and x2 is false
# knowledge = And(majority, x0, x1, Not(x2), x3)
# knowledge = And(majority, Not(x0), Not(x1), Not(x2), Not(x3))

# symbols = [x0, x1, x2, x3]

model = {"x1": 0, "x2": 0, "x3": 0, "x4": 0}

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             for l in range(2):
#                 model["x1"] = i
#                 model["x2"] = j
#                 model["x3"] = k
#                 model["x4"] = l
#                 print("x1: " + str(model["x1"]))
#                 print("x2: " + str(model["x2"]))
#                 print("x3: " + str(model["x3"]))
#                 print("x4: " + str(model["x4"]))
#                 print("Majority: " + str(majority.evaluate(model)))
#                 if i + j + k + l >= 3:
#                     print("Python implementation: True")
#                 else:
#                     print("Python implementation: False")

number_symbols = len(majority.symbols())

majority_BP = addPadding(circuitToBP(majority, number_symbols), number_symbols)

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                bp_output = (evalBP(majority_BP, [i,j,k,l])) != 1
                actual_thing = (i+j+k+l >= 3)
                if bp_output != actual_thing:
                    print(i,j,k,l)



# print(knowledge.evaluate(model))

# for symbol in symbols:
#     if model_check(knowledge, symbol):
#         print(f"    {symbol}")