# how to access the strings

s = "sahil"


# using Bracket operator it have both + and -ve index
print(s[0])  # s
print(s[-1])  # l

# print(s[100])  # error -> index out of range

for char in s:
    print(char)  # s a h i l


if len(s) <= 5:
    print(f"Length of the string:{s} is invalid")
else:
    print(f"Length of the string:{s} is valid")
