# Ch09 > Exercise 10
# Fibonacci, by using RECURSIVE FUNCTION

def fibonacci(n):
    if n <2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n = int(input("피보나치 수열 F(N)의 N값을 입력하세요 --> "))
print("F(%d) = %d"%(n, fibonacci(n)))