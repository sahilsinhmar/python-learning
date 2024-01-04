## String API

# to remove space

str = "  sahil   "

print(str.strip())  # sahil

print(str.lstrip())  # remove space from left side

print(str.rstrip())  # from right side


### Finding the substring

## 1.  find()  to find the index of given char in string if not return -1

s = "sahil is dejected"


print(s.find("i"))  # 3 first occurance from left to right

print(s.rfind("i"))  # 6  index from start always give +ve

print(s.find("z"))  # -1 -> **(-1 if given string is not found)

## we can also specify begin and end

print(s.find("i", 5, 8))  # 6

## Index() method --> to find the index

## The difference is it gives value error if chat is not found

#  print(s.index("z"))  # Value error

print(s.index("i"))  # 3


## to find all the occurances we have

## count() --> method

print(s.count("i"))  # 2

print(s.count("i", 5, 8))  # 1

# replace() --> to replace a substring with new string

ss = "AAABBBAAABBBB"

print(ss.replace("A", "b"))  # bbbBBBbbbBBBB

print(ss)  # AAABBBAAABBBB


strWithSpace = "sahil sinhmar"

print(strWithSpace.replace(" ", ""))  # sahilsinhmar to remove spaces


## split() and join()

strr = "sahil sinhmar"
splittedString = strr.split()  # ['sahil','sinhmar']

print(" ".join(splittedString))  # sahil sinhmar

## changing case

print(strr.upper())  # SAHIL SINHMAR
print(strr.lower())  # sahil sinhmar

# title()
print(strr.title())  # Sahil Sinhmar

# capitalize()
print(strr.capitalize())  # Sahil sinhmar


## str.isalnum() to check if it includes [a to z, 0 to 9]

valueCheck = "sahil15"
print(valueCheck.isalnum())

alphaValue = "sahil"
print(alphaValue.isnumeric())  # False
print(alphaValue.isalpha())  # True


### Reversed function

toReverseString = "sahil"

r = list(reversed(toReverseString))
print(r)

reversedString = "".join(r)
print(reversedString)  # lihas
