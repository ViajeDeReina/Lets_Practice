a = list(map(int, input().split()))

def solve (a:list):
    sum = 0
    for i in range (len(a)):
        sum += a[i]
    print(sum)

solve(a)