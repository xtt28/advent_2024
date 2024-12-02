with open("input.txt", "r") as f:
    global lines
    lines = f.readlines()

safe_lines = 0

def is_safe(nums):
    if sorted(nums) != nums and sorted(nums)[::-1] != nums:
        return False
    
    for i in range(len(nums) - 1):
        dist = abs(nums[i] - nums[i+1])
        if dist < 1 or dist > 3:
            return False
    
    return True


for line in lines:
    nums = [int(n) for n in line.split()]
    if is_safe(nums):
        safe_lines += 1
    else:
        for i in range(len(nums)):
            if is_safe(nums[0:i-1] + nums[i:]):
                safe_lines += 1
                continue
    

print(f"Safe reports: {safe_lines}")