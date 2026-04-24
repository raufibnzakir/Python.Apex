# # even = [x for x in range (1 , 21) if x % 2 == 0]

# # print(even)



# # cubes = [x**3 for x in range (1 , 6)]

# # print(cubes)



# # def fibonacci(n):

# # a, b = 0, 1

# # for _ in range(n):

# #  yield a

# #  a, b = b, a + b

# # for num in fibonacci(10):

# #  print(num)




# # sum_squares = sum(x**2 for x in range(1, 101) if x % 2 == 0)

# # print(sum_squares)



# # words = ["Hello", "World", "Python", "LIST"]

# # lowercase_set = {word.lower() for word in words}

# # print(lowercase_set)



# import json

# data = {
#     "name": "John",
#     "age": 25,
#     "city": "Sampleville",
#     "married": False,
#     "hobbies": ["reading", "traveling", "programming"],
#     "address": {
#         "street": "123 Main Street",
#         "city": "Sample City",
#         "postal_code": "12345"
#     }
# }

# with open("person.json", "w") as file:
#     json.dump(data, file, indent=4)



# import json 
# with open ("person.json" , "r") as file:
#     data = json.load(file)
#     print("Name:", data["name"])
#     print("Hobbies:", data ["hobbies"])






