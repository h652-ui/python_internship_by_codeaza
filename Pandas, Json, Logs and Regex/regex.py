import re

result = re.search(r'hello', "Hello, world!")
if result:
    print("Pattern found!")
else:
    print("Pattern not found.")

result = re.match(r'\d+', "123abc")
if result:
    print("Match found!")
else:
    print("Match not found.")

result = re.findall(r'\d+', "There are 10 cats and 3 dogs.")
if result:
    print("Matches found:", result)
else:
    print("No matches found.")

result = re.sub(r'apple', 'orange', "I have an apple and an apple pie.")
print("Modified string:", result)