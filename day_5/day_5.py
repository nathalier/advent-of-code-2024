from collections import defaultdict


def part_1(pairs, lines):
    cor_lines_mid = []
    for l in lines:
        good = True
        for i, v in enumerate(l):
            for j in range(i+1, len(l)):
                if l[j] not in pairs[v]:
                    good = False
                    break
            if not good:
                break
        if good:
            cor_lines_mid.append(l[len(l) // 2])
    return sum(cor_lines_mid)


def part_2(pairs, lines):
    cor_lines_mid = []
    for l in lines:
        unordered = set(l)
        in_order = put_in_order({k: v for k, v in pairs.items() if k in unordered}, l)
        if in_order == l:
            continue
        cor_lines_mid.append(in_order[len(in_order) // 2])
    return sum(cor_lines_mid)


def put_in_order(pairs, line):
    orders = defaultdict(set)
    for i in line:
        orders[i]
        for j in line:
            if i == j: 
                continue
            if j in pairs[i]:
                orders[i].add(j)
    res = sorted(orders, key=lambda k: len(orders[k]), reverse=True)
    return res
        

def read_data(filename):
    pairs = defaultdict(set)
    with open(filename) as f:
        while line := f.readline().strip():
            a, b = list(map(int, line.split('|')))
            pairs[a].add(b)

        lines = []
        while line := f.readline().strip():
            lines.append(list(map(int, line.split(','))))
    return pairs, lines


#############################
pairs, lines = read_data('input_t.txt')

assert (res := part_1(pairs, lines)) == 143, f'Actual: {res}'
assert (res := part_2(pairs, lines)) == 123, f'Actual: {res}'
#############################


pairs, lines = read_data('input.txt')

print(part_1(pairs, lines))
print(part_2(pairs, lines))
