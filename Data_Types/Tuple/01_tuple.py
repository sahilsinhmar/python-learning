# Tuple --> list but IMMUTABLE

# tuple= (10,20,30,40)

# Duplicates are allowed


tup = (10, 20, 30, 40)

# Accessing the tuple

print(tup[0])  # 10

print(tup[-1])  # 40


print(tup[0:2])  # (10, 20)


# + operator

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2

print(t3)  # (1, 2, 3, 4)


# Methods and functions

# 1. len(tuple)

print(len(t1))  # 2


# 2. count()
print(t3.count(1))  # 1


# 3. index()

print(t3.index(1))  # 0

# 4. reversing elements

t4 = (1, 2, 3, 4, 5, 6)

r = reversed(t4)

k = tuple(r)
print(k)  # (6, 5, 4, 3, 2, 1)


# Sorting

sortt = sorted(t4)
print(tuple(sortt))  # (1, 2, 3, 4, 5, 6)


# max and min

print(max(t4))  # 6


# Packing and unpacking

a = 10
b = 20

newT = (a, b)
print(newT)  #  (10, 20)

c, d = newT

print(c, d)  # 10 20

# Comprehnsions

ctuple = (x for x in range(1, 11))

print(ctuple)  # returs a generator object

print(tuple(ctuple))  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
