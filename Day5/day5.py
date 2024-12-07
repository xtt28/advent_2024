# attention
# this code shall cause brain damage
# read with caution
from functools import cmp_to_key

with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

befores = []
nlfound = False
filtered = []

def is_incorrectly_ordered(s):
    for b in befores:
        try:
            if s.index(b[0]) > s.index(b[1]):
                return True
        except ValueError:
            continue
    return False

def cmp(a, b):
    incord = is_incorrectly_ordered([a, b])
    if incord:
        return 1
    else:
        return -1

def order(g):
    return sorted(g, key=cmp_to_key(cmp))

for line in lines:
    if line == "\n":
        nlfound = True
        continue
    if not nlfound:
        s = [int(x) for x in line.split("|")]
        befores.append((s[0], s[1]))
    else:
        s = [int(x) for x in line.split(",")]
        if is_incorrectly_ordered(s):
            filtered.append(s)


sums = sum([order(s)[int((len(s) - 1)/2)] for s in filtered])
print(sums)