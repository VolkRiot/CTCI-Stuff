# Runtime for the following function
# Translated to Python

# 1
def product(a, b):
    sum = 0;
    for i in range(0, b):
        sum += a
    return sum

print(product(5, 3))

# Linear Runtime O(b)

# 2
def power(a, b):
    if b < 0:
        return 0 # Error
    elif b == 0:
        return 1
    else:
        return a * power(a, b-1)

# Linear Runtime O(b)

# 3
def mod(a, b):
    if b <= 0:
        return -1
    div = a/b
    return a - div * b

# Constant Runtime O(1)

# 4
def div(a, b):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count+=1
    return count

# Runtime O(a/b)

# 5
def sqrt(n):
    return sqrt_helper(n, 1, n)

def sqrt_helper(n, min, max):
    if max < min:
        return -1 # no square root

    guess = (min + max) / 2

    if (guess * guess) == n:
        return guess # found it!
    elif (guess * guess) < n:
        return sqrt_helper(n, guess + 1, max) # try higher
    else:
        return sqrt_helper(n, min, guess - 1) # try lower

# Runtime O(logN)

# 6
def sqrt(n):
    guess = 1

    while (guess * guess) <= n:
        if(guess * guess) == n:
            return guess
        guess+=1

    return -1

# Runtime O(sqrt(n))

# 7
# Unbalanced binary tree worst case one branch runtime is O(n)

# 8
# Find specific Value in non-binary tree O(n)

# 9
def copyArray(array):
    copy = []
    for val in array:
        copy = appendToNew(copy, val)
    return copy

def appendToNew(array, value):
    # copy all elements over to the new array
    bigger = []

    for elem in array:
        bigger.append(elem)

    # add new element
    bigger.append(value)
    return bigger

# Runtime of O(n^2)
