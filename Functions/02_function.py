# Factorial number


# Recursion function
def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


result = factorial(4)
print(result)  # 24 answer


# returning multiple values


def sum(a, b):
    summ = a + b
    sub = a - b
    return summ, sub


x, y = sum(10, 5)

print(x, y)  # 15 5


## Types of arguments

# 1. Positional argument


def add(a, b):
    print(a + b)


add(200, 100)


# 2. keyword arguments


def sub(a, b):
    print(a - b)


sub(a=200, b=100)

# 3. Default arguments


def wish(name="sahil"):
    print(f"hello {name}")


wish()


# 4. Variable length arguments


def li(*n):
    for x in n:
        print(x)


li(10, 20, 30)
