# def add(x, y): return x + y

# def sub(x, y): return x - y

# def mul(x, y): return x * y

# def div(x, y): return x / y

# while True:

#     print("Choose operation: +, -, *, / or 'exit'")

#     op = input("Enter operator: ")

#     if op == 'exit': break

#     x = float(input("Enter first number: "))

#     y = float(input("Enter second number: "))

#     if op == '+': print(add(x, y))

#     elif op == '-': print(sub(x, y))

#     elif op == '*': print(mul(x, y))

#     elif op == '/': print(div(x, y))

#     else: print("Invalid operation")





# contacts = {}

#     with open("contacts.txt", "r") as f:

#         for line in f:

#             name, phone = line.strip().split(',')

#             contacts[name] = phone

# except FileNotFoundError:

#     pass

# while True:

#     print("1. Add  2. Search  3. Exit")

#     choice = input("Choose option: ")

#     if choice == '1':

#         name = input("Name: ")

#         phone = input("Phone: ")

#         contacts[name] = phone

#         with open("contacts.txt", "a") as f:

#             f.write(f"{name},{phone}\n")

#     elif choice == '2':

#         name = input("Enter name to search: ")

#         print("Found:", contacts.get(name, "Not Found"))

#     elif choice == '3':

#         break

# try:

#     a=float(input("enter first number:"))
#     b=float(input("enter second number:"))

#     result=a/b
#     print("result:",result)

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# except ValueError:
#     print("Error: Please enter valid numbers.")




# try:
#     user_input = input("Enter a number: ")
#     num = int(user_input)
#     print("Converted integer:", num)

# except ValueError:
#     print("Error: Invalid input! Please enter a valid integer.")




# try:
#     num = int(input("Enter a number (1-100): "))
#     print(check_number(num))

# except Exception as e:
#     print("Error:", e)



# try:
#     file = open("sample.txt", "r")
# except FileNotFoundError:
#     print("Error: File not found!")

# else:
#     print("File content:")
#     print(file.read())

# finally:
#     try:
#         file.close()
#     except:
#         pass
#     print("Execution completed.")





# try:
    
#     num = int(input("Enter a number: "))
    
    
#     my_list = [1, 2, 3]
#     print("Element:", my_list[num])
    

#     file = open("data.txt", "r")
#     print(file.read())

# except ValueError:
#     print("Error: Invalid number input!")

# except IndexError:
#     print("Error: Index out of range!")

# except FileNotFoundError:
#     print("Error: File does not exist!")

# finally:
#     print("Program execution finished.")