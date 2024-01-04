# slice oprator in string

s = "sahil is dejected"

# s[begin,end,step]  here we will get a substring from begin to end -1


print(s[0:4])  # sahi

print(s[:])  # sahil is dejected

print(s[:-1])  # sahil is dejecte


ss = "sahil"
print(s[-2:4])  # empty string

print(ss[1:-4])  # empty string

print(ss[-4:-1])  # ahi

# with step

print(s[::2])  # shli eetd

# reverse
print(ss[::-1])  # lihas





