# Good try, but TIME OVER :(
import sys
n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))
arr_n.sort()

def compara(array, i):
    start = 0
    end = len(array) - 1
    temp = 0
    while start <= end:
        mid = (start + end) // 2
        if i == array[mid]:
            temp = 1
            return temp
        elif i > array[mid]:
            start = mid+1
        else:
            end = mid-1
    return temp

for i in arr_m:
    print(compara(arr_n, i))