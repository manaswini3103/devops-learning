import json

#to parse JSON string into a python object(dict)
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
print(type(json_string))
data = json.loads(json_string)
print(data)
print(data["name"])
print(type(data))

#to read JSON data from a file
with open('Python//test.json', 'r') as f:
    data = json.load(f)
print(data)