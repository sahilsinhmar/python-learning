# List comprehension


# list 1 to 10

# [EXPRESSION for EACH_ELEMENT in SEQUENCE]


l = [x for x in range(1, 11)]

print(l)


# 1 TO 10 Square value

l1 = [x * x for x in range(1, 11)]

print(l1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


result = [x for x in l1 if x % 4 == 0]

print(result)  # [4, 16, 36, 64, 100]
