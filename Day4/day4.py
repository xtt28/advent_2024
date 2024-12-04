# If this code causes you to receive brain damage then I am sorry
with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

SEARCH_WORDS = ["XMAS", "XMAS"[::-1]]
count = 0

for word in SEARCH_WORDS:
    for i in range(len(lines)):
        line = lines[i]
        count += line.count(word)

    for i in range(len(lines)):
        for j in range(140):
            try:
                if lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]  == word:
                    count += 1
            except IndexError:
                pass

    for i in range(len(lines)):
        for j in range(140):
            try:
                if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] == word:
                    count += 1
            except IndexError:
                pass

    for i in range(len(lines)):
        for j in range(140):
            try:
                if lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] == word:
                    count += 1
            except IndexError:
                pass

print(count)