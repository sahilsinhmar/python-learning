# Set data type

# Duplicates are not allowed
# no index

s = {10, 20, 10}

print(s)  # {10, 20} --> extra 10 is removed

# len(s)

print(len(s))  # 2

# To add a element in a set

# 1. set.add(value)

s.add(40)

print(s)  # {40, 10, 20}


# set.update(sequence)

s.update([1, 2])

s.update("sahil")  # {'h', 1, 2, 'a', 40, 10, 20, 's', 'i', 'l'}

s.update(
    range(1, 10)
)  # {1, 2, 3, 4, 5, 6, 7, 40, 8, 10, 'a', 'h', 9, 20, 'l', 'i', 's'}

print(s)  # {1, 2, 40, 10, 20}


# To remove elements from a set

# 1. set.remove(value)

s.remove("s")
# s.remove("z")  # error

# 2. discard(value)  --> will not throw an error if key not found

print(s.discard("z"))  # nothing removed


# 3. set.pop() --> remove random element

s.pop()


# 4. set.clear() --> clear the set

s.clear()  # set()

print(s)
