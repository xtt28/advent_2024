import re

with open("input.txt", "r") as f:
    global data
    data = f.read()

sum_prods = 0

for res in re.findall(r"mul\([0-9]*,[0-9]*\)", data):
    eq = res.replace("mul(", "").replace(",", "*").replace(")", "")
    sum_prods += eval(eq)

print(sum_prods)