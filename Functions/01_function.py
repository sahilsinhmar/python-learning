# functions are declared with def keyword

# def function_name(parameters):
# body
# return value (optional)


def sum(a, b):
    return a + b


print(sum(10, 20))  # 30


name = input("Please enter your name")


def wish(name):
    print(f"Hello {name}, Good Morning!")


wish(name)  # Hello sahil, Good Morning!


def f1():
    return "hello"


x = f1()

print(x)  # hello
