class A():
    cnt = 0

a = A()
b = A()
c = A()
a.cnt = 100; b.cnt = 200; c.cnt = 300
A.cnt = 100


print(A.cnt,a.cnt,b.cnt,c.cnt)
a.cnt =400; b.cnt = 500; c.cnt = 600

print(A.cnt)
print(a.__dict__.items())
print(A.cnt,a.cnt,b.cnt,c.cnt)
