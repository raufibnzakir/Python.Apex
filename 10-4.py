# import csv
# employees = ["EmployeeID", "Name", "Department", "JobTitle", "Email", "Phone", "Salary", "HireDate"],
#     [101, "John Doe", "Sales", "Sales Executive", "john.doe@example.com", "9876543210", 50000, "2022-03-15"],
#     [102, "Jane Smith", "HR", "HR Manager", "jane.smith@example.com", "9876543211", 65000, "2021-07-01"],
#     [103, "Raj Patel", "IT", "Software Engineer", "raj.patel@example.com", "9876543212", 70000, "2023-01-10"],
#     [104, "Anita Sharma", "Finance", "Accountant", "anita.sharma@example.com", "9876543213", 55000, "2020-11-20"],
#     [105, "Arjun Mehta", "Marketing", "Marketing Specialist", "arjun.mehta@example.com", "9876543214", 60000, "2022-06-05"]

# with open("employees.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(employees)






# import csv

#        with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)

#     filtered_rows = []

#     for row in reader:
#         if int(row["Age"]) > 30:
#             filtered_rows.append(row)

# for row in filtered_rows:
#     print(row)



# import json


# json_string = '''
# [
#     {"name": "Laptop", "price": 55000},
#     {"name": "Phone", "price": 20000},
#     {"name": "Headphones", "price": 3000}
# ]
# '''


# products = json.loads(json_string)

# for product in products:
#     print(f"Name: {product['name']}, Price: {product['price']}")