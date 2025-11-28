#getting data from a string stored in yaml format
import yaml
yaml_string = """
name: Bob
age: 25
city: London
"""
print(type(yaml_string))
data = yaml.safe_load(yaml_string)
print(data)
print(type(data))


#reading data from multiple Yaml documents
with open("Python//test.yaml","r") as f:
    data=list(yaml.safe_load_all(f))
print(data)

#writing the yaml document to a new file
yaml_s = """
name: Brett
age: 35
city: London
skills: ['Python', 'Linux', 'Docker']
"""
names = yaml.safe_load(yaml_s)
with open('Python//test1.yaml', 'w') as file:
    yaml.dump(names, file)
