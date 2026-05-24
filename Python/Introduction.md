```python
#print statement
print("Hello World")
```

# Variables
- case sensitive
- A variable is created when we assign a value to it, so we don't need to declare it.
- It includes letters, digits, underscore
- can Begin with letters and underscore
```python
#printing data assigned to variables
name="manu"
age=25
print(name,age)

#taking input at runtime
var=input("enter an input:")
var1=int(input("enter a number"))
var2=float(input("enter a floating number"))

## Taking multiple inputs
x, y=int(input("Enter 2 values:")).split()
print("Number of Boys",x)
print("Number of Girls",y)

# To check the python version
python --version
```


# Data Types
1. Numeric: int (1), float (1.0), complex (x=1j) 
2. Sequence Type: list, tuple, range
3. Mapping: dict
4. Boolean: bool (x=True, y=Flase)
5. Set: set, frozenset (x=frozenset({'a','b'}))
6. text: str
7. Binary: bytes, bytearray, memory view


# Typed Language
- A typed language is one where variables have data types, such as: int, str, float, bool. These types define what kind of data a variable can hold and what operations can be performed on it.
- Python is **implicit** and case sensitive language. In python we don't need to **declare variable**.  
1. Implicit: doesn't need to define the type of variable like int, float, string.  
```python
a="hello" # automatically detects the type of the variable as 'string'
print(type(a)) 
#output: <class 'string'>
```
2. Explicit: This is when you convert the type yourself using functions like int(), float(), str(), etc.
```python
a=5
print(float(a))
print(type(a))
# output:
# 5.0
# <class 'float'>
```
- Python is also strongly typed, means we can't mix incompatible types automatically like:  
```python
print(5 + "10")
print(5 + int("10"))
# ouput:
# error
# 15
```

## Type Casting
```python
str="abc"
print(int(str))
```

# Expression Execution

String and Numeric values can operate together with '*', it repeats those many times.

```python
A, B=2,3
txt='@'
print(2*txt*3)
# output: @@@@@@
```

string and string can operate with '+'
```python
A, B='2',3
txt='@'
print((A+txt)*B)
# output: 2@2@2@
```


# Arithmatic Operation



# Conditional Statements



# Loops



# Exception Handling

Errors could be of 3 types
1. Compile Time Errors: sytax errors
2. Logical Errors: logic is wrong
3. Runtime Errors: If everything is fine and the input given by the user is wrong

So we need to use Exception Handling for Runtime errors
```python
a=5
b=2
try:
    print("resource opened")
    print(a/b)
    k=int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Can't divide a number by zero")
# The below except block will execute if the input given was not an integer
except ValueError as e:
    print("Invalid Input", e)
except Exception as e:
    print("something went wrong")
# else block executes only when no errors were raised
else:
    print("nothing went wrong")
# finally executes whether there is an error or no error
finally:
    print("resource closed")
```


# Functions in Python

- Block Of Organized, reusable code that perform a specific tasks. It is defined suing "def" keyword.
- Uses: Code Reusability, Readability, Maintainability, Modularity
- Removes redundancy (repeated code)
- There are two types of functions  
1. Built in Functions: like print(), len(), type(), range(); we can know about it code by hovering over those functions.
2. User Defined Functions: Declared using "def" keyword

```python
# Syntax
def funcation_name(parameters):
    # statement
    return expression

# defining function without parameters
def fun():
    print("welcome")
# calling the function
fun()
#output: welcome

# defining a function with parameters
def sum(a,b):
    sum=a+b
    print("sum is", sum)
sum(1,2)
```
- A **return statement** is used to end the the execution of function call. The statements after return are not executed.  
```python
def(a,b):
    return a+b
print(add(2,3))
```
- If return statement is without any expression, the value "None" is returned.  
```python
def fun1():
    print("Hello")
a=fun1() # here the function is called "Hello" would be printed
print(a) # sinsce there is no return statement, python automatically returns None, so 'a' returns 'None' 
#output:
# Hello
# None


def fun1():
    print("Hello")
    return 10
a = fun1()
print(a)
# Output:
# Hello
# 10
```

## Types Of arguments
1. Default Arguments:  
It's a parameter that assumes a defult value, if it's not provided in function call for that argument.  
```python
def cal(a,b=2): # b is default arg
    print(a*b)
cal(3) # 3 is for arg 'a'
# output: 6
```
2. Keyword Arguments:  
Values are passed explicitly specifying parameter names.  
```python
def name(a,b):
    print(a,b)
name(a=1,b='score')
#output: 1 score
```
3. Positional Arguments:  
Values are assigned to parameters based on their order in function call.  
```python
def name_age(n,a):
    print("Hi I am",n)
    print("My age is",a)
name_age("manu",20)
name_age(20,"manu")
```

# File Input/Output
- Python can be used to perform operation on a file like reading writing data. Types of files are:  
1. Text Files: .txt, .docx, .log etc.
2. Binary Files: .mp4, .mov, .png, .jpeg eyc
- These files are stored in memory in bit format like 0 and 1.  
```python
# syntax of opening, reading and closing a file
f=open("file-name","r")
data=f.read()
f.close()

# syntax of opening, reading and closing a file using with
with open("file_name","r") as f:
    data=f.read()
    print(data)

# writing to a file
f=open("file.txt","w")
f.write("this is a new line")
f.close()

# Deleting a file (using OS module, module means like code library written by another programmer that has functions that we can use)
import os
os.remove(filename)
```


# OOPS
- To map with real world scearios, we started using objects in code.
- To reduce redundancy and improve reusability

## Class & Object
- Class is collection of attributes and Methods
- we'll create class before creating object
- **class** is a blueprint for creating objects  
```python
# Class
class Student:
    name="manu"
# Object instance
s1=Student() # used for calling constructor
print(s1.name)
```

## Contructor (__init__function)
- All classes have function called __init__(), which is always executed when object is being initiated.
- There are two types of Constructors.  
1. Default Constructor: single parameter  
```python
def __init__(self):
    pass
```
2. Parameterized Constructor: motre than one parameter
```python
def __init__(self,fullname):
    self.name=fullname
``` 

```python
# Creating class
class Student:
    def __init__(self,fullname):
        self.name=fullname
# Creating Object
s1=Student("manu")
print(s1.name)
```
- **Self** parameter is reference to current instance of class and is used to access variables that belonged to class.
```python
class Student:
    name="manu" #every student name in the class will be manu
    def __init__(self):
        print(self)
        print("adding new student")
s1=Student()
print(s1) # both s1 and self values are same
print(s1.name)
# output:
# adding new student
# manu


class Student1:
    def __init__(self,fullname):
        self.name=fullname # can define multiple students in a class
        print("adding new student")
s3=Student1("karan")
print(s1.name)
s4=Student1("Arjun")
print(s1.name)
# output:
# adding new student
# karan
# adding new student
# Arjun
```
- Here "fullname" will be the value that we are assigning while creating object. In this case "fullname" was karan and Arjun. And "name" was a variable

## Class and Instance Attributes
- "self.name", "self.marks" are object/instance attributes which will be different for every single object.
- The Attribute which will be common for all the objects is "class.attr". For example, colllage name would be same for all the students in that collage. But the student names and marks would differ.  
```python
class Student:
    # class.attr
    collage_name="NNRG"
    def __init__(self,submarks):
        # obj.attr
        self.marks=submarks
s1=Student(97)
print(s1.marks)
print(Student.collage_name)
# output
# 97
# NNRG
```

## Methods
- Methods are functions that belong to object.  
```python
# creating class
class Student:
    def __init__(self,fullname):
        self.name=fullname
    # Method
    def hello(self):
        print("Hello",self.name)
# creating object
s1.Student("manu")
s1.hello()
# Output: Hello manu
```
- **Static Methods** don't use 'self' parameter, these work at class level.
- **Decorators** allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
```python
class Student:
    @static_method # decorator
    def collage():
        pritn("NNRG")
s1=Student()
s1.collage()
```


