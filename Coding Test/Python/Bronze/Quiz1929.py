import sys
a, b = map(int, sys.stdin.readline().split())
temp = []
nums = []

for i in range(a, b+1):
    if i == 1:
        pass
    elif i%2 == 0:
        pass
    else:
        for j in range(1, i+1):
            if i%j == 0:
                temp.append(i)
        if len(temp) == 2:
            nums.append(i)
        temp.clear()

for i in range(len(nums)):
    print(nums[i])