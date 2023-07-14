def my_add(a, b):
    return a + b

def my_subtract(a, b):
    return a - b

def my_multiply(a, b):
    return a * b

def my_divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

calc = [my_add, my_subtract, my_multiply, my_divide]
calc_d ={0:my_add, 1:my_subtract, 2:my_multiply, 3:my_divide}

result = calc[0](10, 20)  
print(result)  

result = calc[1](10, 20) 
print(result) 

result = calc[2](10, 20)
print(result)  

result = calc[3](10, 20) 
print(result) 
print(calc[2](10,10))

print(calc_d[0](30,40))
add = calc_d[0]
sub = calc_d[1]
mul = calc_d[2]
div = calc_d[3]
print(add(100,20))
print(sub(100,20))
print(mul(100,20))
print(div(100,20))


def func():
    y = 10 + 20
    return y

a = func
a1 = func()

print(a)
print(a1)

