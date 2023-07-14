# x = int(input())
# n = int(input())
# check = 0

# for i in range(n):
#     p,q = map(int,input().split())
#     check += (p * q)
    
# if  check == x :
#     print('Yes')
# else:
#     print('No')

# n = int(input())
# if n%4 == 0:
#     i = int(n /4)
#     print("long "*i+"int")

# import sys

# a = int(input())

# for i in range(a):
#     c, d = map(int,sys.stdin.readline().split())
#     print(c+d)

# t = int(input())

# for i in range(t):
#     a,b = map(int,input().split())
#     print("Case #{0}: {1} + {2} = ".format(i+1,a,b)+str(a+b))

# from datetime import datetime

# print(datetime.today().strftime("%Y-%m-%d"))

# print(datetime.today().year)

# a,b = map(int,input().split())
# c = int(input())
# if b + c < 60:
#     print(a,b+c)
# elif b+ c >= 60:
#     if a+int((b+c)/60) <24:
#         print(a+int((b+c)/60),(b+c)%60)
#     else:
#         print(a+int((b+c)/60)-24,(b+c)%60)

# a,b,c = map(int,input().split())
# d = int(input())
# if c+d < 60:
#     print(a,b,c+d)
# elif c+d >=60:
#     if c+int((c+d)/60) < 60:
#         print(a,b+c+int((c+d)/60),(c+d)%60)
#     elif b+int((c+d)/60) >= 60:
#         if a+(b+int((c+d)/60)) <24:
#             print(a+int((b+int((c+d)/60))/60),(b+int((c+d)/60))%60,(c+d)%60)
#         elif a+(b+int((c+d)/60)) >= 24:
#             print(a+int((b+int((c+d)/60))/60)-24,(b+int((c+d)/60))%60,(c+d)%60)

# a, b, c = map(int,input().split())
# d = int(input())

# sec = ((c+d) % 60)
# min = (b + ((c+d) // 60)) % 60
# hour = (a + ((b + ((c+d) // 60)) // 60))%24
    
# print(hour,min,sec)

# A, I = map(int, input().split())
# A = int(A)
# J = int(I)-1
# print((A*J)+1)
T = int(input())
for _ in range(T):
    tmp = input()
    for i in range(len(tmp)+1):
        tmp[i]*T

