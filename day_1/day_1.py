from collections import Counter

def part_1(lines):
    l_1, l_2 = list(map(sorted, zip(*lines)))
    return sum(abs(a - b) for a, b in zip(l_1, l_2))


def part_2(lines):
    c_1, c_2 = list(map(Counter, zip(*lines)))
    return sum([a * b * c_2[a] for a, b in c_1.items()])


def read_data(filename):
    with open(filename) as f:
        lines = list(map(lambda x: list(map(int, x.strip().split())), f.readlines()))
    return lines


#############################
test_data = read_data('input_t.txt')

assert (res := part_1(test_data)) == 11, f'Actual: {res}'
assert (res := part_2(test_data)) == 31, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(part_1(data))
print(part_2(data))
