a = list(map(int, input().split()))
a.remove(max(a))
print(max(a))


#a,b,c = map(int, input().split())

#avg = (a+b+c)/3

#a_dif = abs(avg-a)
#b_dif = abs(avg-b)
#c_dif = abs(avg-c)

#mid = a

#if a_dif > b_dif:
#    mid = b
#if b_dif > c_dif:
#    mid = c

#print(mid)