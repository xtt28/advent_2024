with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

safe_lines = 0

for line in lines:
    nums = [int(n) for n in line.split()]
    bad = False
    if sorted(nums) != nums and sorted(nums)[::-1] != nums:
        bad = True
        continue
    
    for i in range(len(nums) - 1):
        dist = abs(nums[i] - nums[i+1])
        if dist < 1 or dist > 3:
            bad = True
    
    if not bad:
        safe_lines += 1

print(f"Safe reports: {safe_lines}")