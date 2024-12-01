with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

column_1_nums = []
column_2_nums = []

for line in lines:
    line = line.replace("\n", "")
    split = [int(n) for n in line.split()]
    column_1_nums.append(split[0])
    column_2_nums.append(split[1])

column_1_nums = sorted(column_1_nums)
column_2_nums = sorted(column_2_nums)

sum_distances = 0

for i in range(len(column_1_nums)):
    sum_distances += abs(column_1_nums[i] - column_2_nums[i])

similarity_score = 0

for num in column_1_nums:
    similarity_score += num * column_2_nums.count(num)

print(f"Sum of distances: {sum_distances}")
print(f"Similarity score: {similarity_score}")