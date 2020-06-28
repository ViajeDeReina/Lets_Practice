a = int(input())
for i in range(a):
    n, s = input().split()
    n = int(n)

    for j in range(len(s)):
        print(s[j]*n, end="")
    print()