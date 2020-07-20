# Ch06 > Exercise 07
# Just simple code. Find the odd number which makes the total summation of odd numbers exceed 1000

ttl = 0
i = 1

while ttl < 1000:
    ttl += i
    if ttl > 1000:
        break
    i += 2

print("1과 1000 사이에 있는 홀수의 합계를 최초로 1000이 넘게 하는 숫자 : {}".format(i))