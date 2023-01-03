def double(x):
    return 2 *x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

from typing import Callable, List
Input = List[int]

def generate_values(how: Callable, x_table: Input) -> float:
    results = []
    print(f"{how.__name__}:")
    for x in x_table:
        results.append(how(x))
    return results


x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))
