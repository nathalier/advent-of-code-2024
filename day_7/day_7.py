from operator import add, mul


def solve(data, operators):
    acc = 0
    for eq in data:
        items, exp_res = eq
        if eq_exists(items[0], items[1:], exp_res, operators):
            acc += exp_res
    return acc


def eq_exists(acc, items, exp_res, operators):
    if acc > exp_res:
        return False
    if len(items) == 0:
        if acc == exp_res:
            return True
        return False
    found = any([eq_exists(f(acc, items[0]), items[1:], exp_res, operators) for f in operators])
    return found


def concat(a, b):
    return int(f'{a}{b}')


def part_1(data):
    return solve(data, [add, mul])


def part_2(data):
    return solve(data, [add, mul, concat])


def read_data(filename):
    test_eq = []
    with open(filename) as f:
        for line in f.readlines():
            res, items = line.strip().split(': ')
            test_eq.append((tuple(map(int, items.split())), int(res)))
    return test_eq


#############################
test_data = read_data('input_t.txt')

assert (res := part_1(test_data)) == 3749, f'Actual: {res}'
assert (res := part_2(test_data)) == 11387, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(part_1(data))
print(part_2(data))
