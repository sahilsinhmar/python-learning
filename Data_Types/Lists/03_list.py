# List methods and functions


l = [10, 20, 30, 40]


# 1. list.append(value) --> always inserted at the end

print(l.append(200))
print(l)  # [2, 5, 10, 20, 30, 40, 200]

# 2. list.insert(postion,value)

print(l.insert(0, 5))  # return None but 5 added
print(l)  #  [5, 10, 20, 30, 40]

print(l.insert(-10000000, 2))
print(l)  # [2, 5, 10, 20, 30, 40]  added at start

print(l.insert(100, 100))
print(l)  # [2, 5, 10, 20, 30, 40, 100] at the end


# 3. list.index(value) to get the index of a value

print(l.index(200))  # 6
# print(l.index(55))  # value error if not present


# 4. Sorted function not a method --> sorted(list)

print(sorted(l))  # [2, 5, 10, 20, 30, 40, 100, 200] sorted


# 5. list.count(value) to get the number of value in a list

print(l.count(10))  # 1
print(l.count(55))  # 0 --> not present


# Manipulating the list

# list.extend(sequence)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# any sequence ->

print(l1.extend("5"))

print(l1)  # string [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '5']

l1.extend([1, 2])
print(l1)  # list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '5', 1, 2]

l1.extend((1, 3, 3))
print(l1)  #  tuple [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '5', 1, 2, 1, 3, 3]

l1.extend({1, 2})
print(l1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '5', 1, 2, 1, 3, 3, 1, 2]

l1.extend({"name": "sahil"})
print(l1)  # keys added --> dict

