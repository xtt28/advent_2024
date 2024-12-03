import re

with open("input.txt", "r") as f:
    global data
    data = f.read().split("do()")

sum_prods = 0

def evaluate_all_mul(s):
    global sum_prods
    for res in re.findall(r"mul\([0-9]*,[0-9]*\)", s):
        eq = res.replace("mul(", "").replace(",", "*").replace(")", "")
        sum_prods += eval(eq)

for st in data:
    st = st.split("don't()", 1)[0]
    evaluate_all_mul(st)

print(sum_prods)