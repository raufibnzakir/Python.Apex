# ab=lambda x:x*x

# print(ab(3))



# number=[1,2,3,4,5]

# cubes=list(map(lambda x:x**3,number))

# print(cubes)



# names=['apple','aeroplane','banana','cherry']

# short = list(filter(lambda name: name.startswith('a'), names))

# print(short)




# words=['apple','aeroplane','banana','elephant','ant','one']

# short=list(filter(lambda w:len(w)>5,words))

# print(short)





# numbers = [1, 2, 3, 4, 5]

# short = reduce( lambda a, b: a + b,
#                filter(lambda x: x % 2 == 0,
#                       map(lambda x: x ** 2, numbers)
#     )
# )

# print(short)





# numbers = [3, 7, 2, 9, 5]
# numbers.sort()
# numbers.reverse()
# print(numbers[0])

# maximum = reduce(lambda a, b: a if a > b else b, numbers)

# print(maximum)



# add=lambda a,b:a+b

# print(add(1,2))




# numbers=[2,4,6]

# squares=list(map(lambda x:x**2,numbers))

# print(squares)



# even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

# print(even_or_odd(10)) 
# print(even_or_odd(7))   



# maximum = lambda a, b: a if a > b else b

# print(maximum(10, 20)) 




# uppercase = lambda s: s.upper()

# print(uppercase("hello"))