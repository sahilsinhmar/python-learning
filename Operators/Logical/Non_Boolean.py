#### For non Boolean types

## And opretaor

## zero= false non-Zero= True


## So in x and y -> if x is true then result is y
## and if x is false then result is x


print(10 and 20)  # 20
print(0 and 20)  # 0

## so we can say that AND returns the first Falsy value ,otherwise return the last value


print(10 and 20 and 30)  # 30
print(10 and 0 and 30)  # 0


### Or operator
## in x and y , if x is true then it will return x
## and if x is false then it return y

print(10 or 20)  # 10
print(0 or 10)  # 10

## So we can say that the 'OR' returns the first truthy value otherwise it returns the last value

print(-10 and 20)  # 20
print(-10 or 20)  # -10  so -10 is a truthy value



