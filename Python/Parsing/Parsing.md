# Parsing
Parsing refers to the process of reading, decoding, and converting data from a text format (like JSON or YAML) into data structures that a programming language can use (arrays, dictionaries, objects, etc.).

## JSON (JavaScript Object Notation)

### What is JSON?
- A lightweight data-format used widely in APIs, configuration files, and data exchange.
- Syntax is strict and based on JavaScript object structure.
- Easy for machines to read and write
**example**
```json
{
  "name": "John",
  "age": 25,
  "skills": ["Python", "Linux", "Docker"]
}
```

**JSON Rules**
- Uses {} for objects
- Uses [] for arrays
- Strings must use double quotes
- Only allows valid data types: string, number, boolean, null, object, array

### Parsing in JSON
- Python's built-in json module handles JSON data.
- We use json.loads() to convert a JSON string into a Python dictionary or list.

**example**
```python
import json
data = json.loads('{"name": "John", "age": 25}')
print(data["name"])
```
## YAML (YAML Ain't Markup Language)

### What is YAML?
- A human-friendly configuration language.
- Used in CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins), Kubernetes manifests, etc.
- More readable and flexible than JSON.
**example**
```yaml
name: John
age: 25
skills:
  - Python
  - Linux
  - Docker
  ```

### YAML Rules
- Uses indentation (spaces only, no tabs!)
- Key-value pairs separated by colon :
- Lists created with hyphens -
- Allows comments with #
- More flexible than JSON (supports complex data structures)

### Parsing in YAML
- Python does not have built-in YAML support. The PyYAML library is commonly used for this purpose.
- We mostly use yaml.safe_load() to convert a YAML string into a Python dictionary or list.

#### Methods
**1.load()**
- Loads YAML with no security restrictions.
- Can execute arbitrary Python objects, which may lead to code execution vulnerabilities if the YAML content is untrusted.
- The Loader parameter of the load() function is set to SafeLoader.
**example**
```python
import yaml
with open('geeksforgeeks.yml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)
    
# Print the values as a dictionary
print(data)
```
**2.safe_load()**
- It is recommended for security reasons when dealing with untrusted sources.
**eample**
```python
import yaml

data = yaml.safe_load("""
name: John
age: 25
""")
print(data["name"])
```
**3.full_load()**
- The yaml.full_load() function is used to parse the content of the YAML file in the form of key-value pairs.
- Then using the Python get() method, we can get specific data from the YAML file.
**example**
```python
import yaml
with open('geeksforgeeks.yml', 'r') as f:
    data = yaml.full_load(f)
    
# Print the values as a dictionary
output = {
    'UserName': data.get('UserName'),
    'Password': data.get('Password'),
    'phone': data.get('Phone'),
    'Skills': ' '.join(data.get('Skills', []))
}

print(output)
```
**4.load_all()**
-The load_all() method is used when we want to load multiple YAML documents present in a single file.
**example**
```python
import yaml

with open('multiple_documents.yml', 'r') as f:
    yaml_data = list(yaml.safe_load_all(f))
    print(yaml_data)
```

