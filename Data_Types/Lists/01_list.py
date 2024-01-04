## List is like array in python , as array is not present in python

# Hetrogeneous - can store any type of data

l = ["sahil", 25, True, [10, 20], (10, 20), {"name": "sahil"}, {10, 20}]

print(l)  # ['sahil', 25, True, [10, 20], (10, 20), {'name': 'sahil'}, {10, 20}]

# Duplicates are allowed
l1 = ["sahil", "sahil"]


# Accessing the List data type

# 1. Slice

print(l[0])
print(l[:])
# print(l[100])  # error , index out of range
print(l[::2])

print(l[::-1]) # for reverse
