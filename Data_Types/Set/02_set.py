# Set have specific methods for mathematical operations

# 1. set.union(set) --> present in both sets

s = {10, 20, 30, 40}
s1 = {30, 40, 50, 60}

s3 = s.union(s1)

print(s3)  # {40, 10, 50, 20, 60, 30}


# 2. set.interaction(set) -->return only which are present in both sets

s4 = s.intersection(s1)  # {40, 30}

print(s4)


# 3. set.difference(set1)  ==> remove elements from set , which are present in set1


s5 = s.difference(s1)

print(s5)


# Set comprehensions

newSet = {x for x in range(1, 11)}

print(newSet)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
