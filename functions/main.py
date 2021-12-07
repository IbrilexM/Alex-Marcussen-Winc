# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# 1. 
def greet(name):
    welcom = f'Hello, {name}!'
    return welcom
print(greet('Bob'))

# 2.
def add(a, b, c):
    sum = a + b + c
    return sum
print(add(9, 9 ,9))

# 3.
def positive(number):
    plus = 0 < number
    return plus
print(positive(20))
print(positive(-2))
print(positive(0))

# 4.
def negative(number1):
    minus = 0 > number1
    return minus
print(negative(9))
print(negative(-14))
print(negative(0))