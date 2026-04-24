# numbers=[1,2,3,4,5]

# squars=list(map(lambda x:x**2,numbers))

# print(squars)



# words=['apple','banana','cherry']

# uppercase=list(map(lambda x:x.upper(),words))

# print(uppercase)



# numbers=[1,2,3,4,5,]

# add=list(map(lambda x:x+10 , numbers))

# print(add)



# words=['rauf','pratik','himesh']

# length=list(map(lambda x:len(x),words))

# print(length)



# celsius = [0, 20, 30, 40]

# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# print(fahrenheit)



# numbers=[1,2,3,4,5,6]

# even=list(filter(lambda x:x%2==0,numbers))

# print(even)



# numbers=[1,2,3,4,5,6,]

# odd=list(filter(lambda x:x%2!=0,numbers))

# print(odd)



# numbers=[10,20,30,40,50,60,70,]

# y=list(filter(lambda x:x>50,numbers))

# print(y)



# words=['aeroplane','elephant','ant']

# length=list(filter(lambda x:len(x)>5,words))

# print(length)



# strings = ["hello", "", "world", "", "python"]

# non_empty = list(filter(lambda x: x != "", strings))

# print(non_empty)

from functools import reduce

# numbers=[1,2,3,4,5]

# total=reduce(lambda x,y:x+y,numbers)

# print(total)



# numbers=[1,2,3,4]

# product=reduce(lambda x,y:x*y,numbers)

# print(product)



# numbers=[1,2,3,4,5]

# max=reduce(lambda x,y:x if x > y else y ,numbers)

# print(max)




# words = ["Hello", " ", "World", "!"]

# result = reduce(lambda x, y: x + y, words)

# print(result) 



# n = 5

# factorial = reduce(lambda x, y: x * y, range(1, n + 1))
                   
# print(factorial) 