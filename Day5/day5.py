with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

befores = []
nlfound = False
filtered = []

for line in lines:
    if line == "\n":
        nlfound = True
        continue
    if not nlfound:
        s = [int(x) for x in line.split("|")]
        befores.append((s[0], s[1]))
    else:
        s = [int(x) for x in line.split(",")]
        bad = False
        for b in befores:
            try:
                if s.index(b[0]) > s.index(b[1]):
                    bad = True
            except ValueError:
                continue
        if not bad:
            filtered.append(s)

sums = sum([s[int((len(s) - 1)/2)] for s in filtered])
print(sums)