a = int(input())
b = int(input())

num1 = b%10
num2 = (b//10)%10
num3 = b//100

print(a*num1)
print(a*num2)
print(a*num3)
print(a*b)