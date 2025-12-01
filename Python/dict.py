'''#palindorme
import sys
test_string = "malayalam"
print(test_string[::-1])
for index, item in enumerate(test_string):
    if item == test_string[-index - 1]:
        continue
    else:
        print("Not a palimdrome")
        sys.exit()
print("Is it a palindrome")

#assigning 
l=[1,2,3,4]
s="hello world good morning"
for index, item in enumerate(l):
    print(str(item) + ": " + s.split()[index])

print(s.split())

#creating a dictionary at run time
key=input("enter some key:")
value=input("enter some value:")
d={}
d[key]=value
#(or)
#d.update({key:value})
print(d)

#checking whether the given key is in dict or not
d= {'name':'manu','age':25}
key=input("enter a key that you want to search:")
if key in d:
    print("the given key",key,"is present the dictionary and it's value is",d[key])
else:
    print("the given key is not present in dictionory")

#counting the words in a string
words=[]
string=input("enter a string:")
words=string.split()
print("count of words in the given string is:",len(words))

#counting the words in a string using dictionary
words=[]
d={}
s=input("enter a string:")
words=s.split()
for key in words:
    d[key]=words.count(key)
print(d)

#creating dict of keys and values are square of keys
num=int(input("enter a number"))
d={}
for i in range(1,num+1):
    d[i]=i**2
print(d)

#map 2 list into a dictionary
keys=['clg','sub']
values=['NNRG','python']
myDict = dict(zip(keys, values)) #zip() joins the two lists together, matching items by their position.
print("Dictionary Items  :  ",  myDict)

#creating a dictionary at run time
num=int(input("enter how many no. of items we want to add in dictionary"))
d={}
for i in range(num):
    key=input("enter key")
    value=input("enter value")
    d[key]=value
print(d)

#merging 2 dictionaries
d1={'name':'manu','age':25}
d2={'clg':'NNRG','sub':'python'}
d1.update(d2)
print(d1)

#program to multiply all items in dictionaries
dict={'x':10,'y':20,'z':30}
tot=1
for i in dict:
    tot=tot*dict[i]
print(tot)'''

#adding the values in dictionary
myDict = {'x': 250, 'y':500, 'z':410}
print("\nSum of Values: ", sum(myDict.values()))

#deleting a key from dict
dict={'x':10,'y':20,'z':30}
key=input("enter a key that we want to delete:")
if key in dict:
    del dict[key]
    print("found the given key and deleted")
else:
    print("key not found")


