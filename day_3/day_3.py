import re


def part_1(data):
    op_pairs = re.findall('mul\((\d+),(\d+)\)', data)
    return sum((int(a) * int(b) for a, b in op_pairs))

def part_2(data):
    do, res = True, 0
    patterns = re.finditer("(do\(\))|(don\'t\(\))|(?:mul\((\d+),(\d+)\))", data)
    for found in patterns:
        if found.group(1) is not None:
            do = True
        elif found.group(2) is not None:
            do = False
        else:
            res += int(found.group(3)) * int(found.group(4)) * do
    return res

def read_data(filename):
    with open(filename) as f:
        data = f.read()
    return data

#############################
test_data = read_data('input_t.txt')
assert (res := part_1(test_data)) == 161, f'Actual: {res}'

test_data = read_data('input_t_p2.txt')
assert (res := part_2(test_data)) == 48, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(part_1(data))
print(part_2(data))
