from logic import *

x1 = Symbol('x1', 1)
x2 = Symbol('x2',2)

symbols = [x1, x2]

xor = Not(And(Not(And(Not(x1), x2)), Not(And(x1, Not(x2)))))

# x1 is false and x2 is true
knowledge1 = And(And(x1, Not(x2)), xor)

# x1 is false and x2 is false
knowledge2 = And(And(Not(x1), Not(x2)), xor)

for symbol in symbols:
    if model_check(knowledge1, symbol):
        print(f"    {symbol}")