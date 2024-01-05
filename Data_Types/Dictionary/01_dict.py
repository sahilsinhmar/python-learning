# Dictionay are key:value pair ,collection of elements

# Mutable, Growable,

# just like objects in js or map


d = {"name": "sahil", "rollNo": 17, "age": 25}

print(d)  # {'name': 'sahil', 'rollNo': 17, 'age': 25}


# Creation of dict

# dict() --> function
# List of tuples    Tuple of typles,  Set of tuples,
# List of list      Tuple of list     note--> XSet of lists

l = [("name", "rohit"), ("age", 25)]

print(dict(l))  # {'name': 'rohit', 'age': 25}


# How to access the dict

# dict[key]

print(d["name"])  # sahil

# print(d["namee"])  # error

# To add in a dictionary
d["skills"] = "None"
print(d)  # {'name': 'sahil', 'rollNo': 17, 'age': 25, 'skills': 'None'}

# To delete--> del

del d["skills"]  # {'name': 'sahil', 'rollNo': 17, 'age': 25}

print(d)



