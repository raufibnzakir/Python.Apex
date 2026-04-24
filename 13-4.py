import re

text = " a b c "

pattern = r"^(\w+)\s+(\w+)\s+(\w+)$"
match = re.match(pattern, text)

if match:
    first = match.group(1)
    middle = match.group(2)
    last = match.group(3)

    print("first name:", first)
    print("second name:", middle)
    print("third name:", last)








