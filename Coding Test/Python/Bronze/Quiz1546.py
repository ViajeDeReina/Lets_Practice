n = int(input()) #number of subjects
array = list(map(int, input().split()))

best = max(array)
new_sum = 0

for i in range(n):
    array[i] = (array[i]/best) * 100
    new_sum += array[i]

print(new_sum/n)