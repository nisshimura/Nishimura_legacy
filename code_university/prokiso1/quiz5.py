target = 9
low = 0
high = 16

tmp_num = 0

while tmp_num != target:
    tmp_num = (high + low) // 2
    print('tmp_num=', tmp_num)
    if tmp_num > target:
        high = tmp_num
    else:
        low = tmp_num

print('######################')


def add(x, y):
    return x + y


def mult(x, y):
    print(x*y)


add(1, 2)
print(add(2, 3))
mult(3, 4)
print(mult(4, 5))

print('######################')


def sq(func, x):
    y = x ** 2
    return func(y)


def f(x):
    return x ** 2


calc = sq(f, 2)
print(calc)

print('######################')

x = 50


def func():
    global x
    print('x is', x)
    x = 2
    print('changed global x to', x)


func()
print('Value of c is', x)

print('######################')

# x = 3
# def a():
#     y = x + 4
#     return y
# def b(x):
#     x += 6
#     return x 
# def c():
#     x += 2
#     return x
# print('a:', a())
# print('b:', b(x))
# print('c:', c())

print('######################')

x = 3
y = 3

def f(y):
    y = x + 4
    return y
f_val = f(y)

x = 555
y = 3
print(f_val == f(y))

x = 3
y = 555
print(f_val == f(y))