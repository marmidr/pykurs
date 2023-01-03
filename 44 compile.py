import math
import time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

for formula in formulas_list:
    print("Formula eval: ", formula)
    t = time.time()
    for x in argument_list:
        res = eval(formula)
    t = time.time() - t
    print(f"Tme taken: {t:4.1f}s")


    print("Formula compile: ", formula)
    t = time.time()
    formula_comp = compile(formula, "inline code", "eval")
    for x in argument_list:
        res = exec(formula_comp)
    t = time.time() - t
    print(f"Tme taken: {t:4.1f}s")

