x = 75
y = 105

def x_func():
    if x != y:
        v = x + y
    else:
        v = x - y
    return v

#V = x_func()
        
#print(V)


def x_func_2(x, y):
    if x != y:
        v = x + y
    else:
        v = x - y
    return v

A = x_func_2(-4, 3)
B = x_func_2(10.01, 10)

print(A)
print(B)


def my_func(food):
    for x in food:
        print(x)
        
fruits = ["apple", "banana", "cashew"]
my_func(fruits)