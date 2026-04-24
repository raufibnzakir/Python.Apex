# def greet(name):
#     return f"Hello, {name}!"




# def celsius_to_fahrenheit(celsius):

#     return (celsius * 9/5) + 32

import json
with open('sample1.json') as f:
    loaded = json.load(f)
    print(loaded['name'])
