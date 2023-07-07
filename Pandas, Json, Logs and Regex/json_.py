import json

# Python object to JSON string (json.dumps)
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(data)
print(json_string)  # {"name": "John", "age": 30, "city": "New York"}

# Python object to JSON file (json.dump)
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
with open('output.json', 'w') as json_file:
    json.dump(data, json_file)


# JSON string to Python object (json.loads)
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)  # {'name': 'John', 'age': 30, 'city': 'New York'}

# JSON file to Python object (json.load)
with open('output.json') as json_file:
    data = json.load(json_file)
print(data)  # Contents of the JSON file as a Python object
