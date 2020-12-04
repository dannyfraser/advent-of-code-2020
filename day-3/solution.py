import operator
from functools import reduce

with open("inputs.txt") as f:
    inputs = f.read().splitlines()

with open("test_inputs.txt") as f:
    test_inputs = f.read().splitlines()

def solve(inputs, step, down=1):
    line_length = len(inputs[0])
    position = 0
    trees = 0
    for line in inputs[down::down]:
        position = position + step
        if line[position%line_length]=="#":
            trees += 1

    return trees

assert solve(test_inputs, 3) == 7
print(solve(inputs, 3))

# (step, down) tuples
multi_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
assert list(map(lambda x: solve(test_inputs, *x), multi_slopes)) == [2, 7, 3, 4, 2]
print(reduce(operator.mul, map(lambda x: solve(inputs, *x), multi_slopes)))