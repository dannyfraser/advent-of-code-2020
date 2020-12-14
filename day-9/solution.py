from itertools import combinations

with open("test_inputs.txt") as f:
    test_inputs = list(map(int, f.read().splitlines()))

with open("inputs.txt") as f:
    inputs = list(map(int, f.read().splitlines()))


def find_weak_point(inputs, preamble_length):
    for i in range(preamble_length, len(inputs)):
        target = inputs[i]
        options = inputs[i - preamble_length:i]
        is_valid = any(list(map(lambda x: sum(x) == target, combinations(options, 2))))
        if not is_valid:
            return target

assert find_weak_point(test_inputs, 5) == 127
print(find_weak_point(inputs, 25))

def find_weakness_limits(inputs, target):
    
    for i in range(len(inputs)):
        result = -1
        end = 1
        while result < target:
            nums = inputs[i:i+end]
            result = sum(nums)
            if result == target:
                return min(nums) + max(nums)
            end += 1

assert find_weakness_limits(test_inputs, 127) == 62
print(find_weakness_limits(inputs, find_weak_point(inputs, 25)))

