# Runtime for the following function
# Translated to Python

def product(a, b):
    sum = 0;
    for i in range(0, b):
        sum += a
    return sum

print(product(5, 3))

# Linear Runtime O(b)

def power(a, b):
    if b < 0:
        return 0 # Error
    elif b == 0:
        return 1
    else:
        return a * power(a, b-1)

# Linear Runtime O(b)

def mod(a, b):
    if b <= 0:
        return -1
    div = a/b
    return a - div * b

# Constant Runtime O(1)

def div(a, b):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count+=1
    return count

# 
