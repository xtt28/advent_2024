# The garbage solution which takes 20 years to run
from itertools import product
from math import prod

with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

operators = {"+", "*", "||"}
s = 0

def eval_ltor(tokens):
    initial = tokens[0]
    op = tokens[1]
    for token in tokens[2:]:
        if isinstance(token, int):
            if op == "||":
                initial = int(str(initial) + str(token))
            else:
                initial = eval(f"{initial}{op}{token}")
        else:
            op = token
    return initial

for line in lines:
    target = int(line.split(": ", 1)[0])
    nums = [int(a.replace("\n", "")) for a in line.split(" ")[1:]]

    perms = list(product(operators, repeat=len(nums) - 1))
    for perm in perms:
        expr = []
        for i in range(len(nums)):
            expr.append(nums[i])
            if i < len(nums) - 1:
                expr.append(perm[i])
        evaluated = eval_ltor(expr)
        if evaluated == int(target):
            print(evaluated)
            s += evaluated
            break

print(s)