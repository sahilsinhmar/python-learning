# Equality Operator

a = 10
b = 12
c = "10"
d = True
e = 1

print(a == b)  # False
print(a == c)  # False
print(d == 1)  # True
print(a == 10.0)  # True

old = "sahil"
new = old

print(new is old)  # True

print(old == new)


list1 = [10, 20, 30]
list2 = [10, 20, 30]

list3 = list1

print(list1 is list2)  # False

print(list1 == list2)  # True

print(list1 is list3)  # True
