# If this code causes you to receive brain damage then I am sorry
with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

WORDS = ["MAS", "MAS"[::-1]]
count = 0

for i in range(len(lines)):
    for j in range(140):
        try:
            if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] in WORDS and lines[i][j+2] + lines[i+1][j+1] + lines[i+2][j] in WORDS:
                count += 1
        except IndexError:
            pass
        

print(count)