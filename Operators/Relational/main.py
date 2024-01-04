## Relational Operator  < > <= >=

a = 10
b = 20

print(a < b)  # True
print(a > b)  # False

c = "a"
d = "z"
e = "aabcd"
f = "abcde"
print(c < d)  # True
print(c > d)  # False
print(e < f)  # False
print(e > f)  # True


print(True < False)  # False
print(True > False)  # True


print(1 < True)  # False as 1<1 not true
print(1 > False)  # True

# print(1 < "sahil")  # error , both should be of string type
