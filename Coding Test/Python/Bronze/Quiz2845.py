import sys
people, square = map(int, sys.stdin.readline().split())
news = list(map(int, sys.stdin.readline().split()))

total = people * square

for i in range(5):
    news[i] = news[i] - total
    print(news[i], end=" ")