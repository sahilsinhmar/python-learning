# lambda function is same like arrow function from js

# nameless, instant use

from functools import reduce

s = lambda n: n * n

# = lambda input : Express

# sum of two numbers

sum = lambda a, b: a + b

print(sum(10, 20))  # 30

biggest = lambda a, b, c: a if a > b and a > c else b if b > c else c
print(biggest(10, 5, 15))  # 15


# filter function

# filter(function,sequence)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = list(filter(lambda n: n % 2 == 0, l))  # [2, 4, 6, 8, 10]

print(l1)


# map function

l2 = list(map(lambda n: n * 2, l))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(l2)


# reduce function

l3 = reduce(lambda x, y: x + y, l)  # 55
print(l3)


