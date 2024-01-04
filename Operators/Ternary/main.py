a = 10
b = 20


c = a if a < b else b

print(c)  # a

a = 25
c = 45


d = a if a < b and a < c else b if b < c else c
print(d)  # 20
