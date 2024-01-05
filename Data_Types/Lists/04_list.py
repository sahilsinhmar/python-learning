# Removing methods

# 1. list.remove(value)

l = [10, 20, 30, 40, 50]

l.remove(50)

print(l)  # [10, 20, 30, 40]


# To remove all occurances

l1 = [10, 20, 30, 10, 40, 10, 50, 10]

x = 10
while True:
    if x in l1:
        l1.remove(x)
    else:
        break

print(l1)  # [20, 30, 40, 50]


# 2. list.pop() --> remove the last element

list3 = [10, 20, 30, 40, 50]

print(list3.pop())  # 50


# 3. list.clear() --> empty list
list4 = [10, 20]
print(list4.clear())


# 4. list.reverse() --> list specific  || reversed() --> for all sequence

list = [50, 40, 30, 20, 10]

list.reverse()

print(list)  # [10, 20, 30, 40, 50]

newList = reversed(list)

print(newList)  # <list_reverseiterator object at 0x000001875F7DFE50>


# list.sort()

list.sort()
print(list)  # [10, 20, 30, 40, 50]
