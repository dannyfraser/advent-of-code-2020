from itertools import combinations
import operator
from functools import reduce

with open("inputs.txt") as f:
    inputs = list(map(int, f.readlines()))

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def solve(inputs, target, numbers):
    return list(map(prod, filter(lambda x: sum(x)==target, combinations(inputs, r=numbers))))[0]

print(solve(inputs, 2020, 2))
print(solve(inputs, 2020, 3))