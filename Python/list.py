'''#printing list index and values
l=[1,2,3]
for i in range(len(l)):
    print("index",i,"value",l[i])

#concatinating lists
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)

#adding 2 lists
l1=[1,2,3]
l2=[4,5,6]
tot=[]
for i in range(3):
    tot.append(l1[i]+l2[i])
print(tot)

#adding the list items
l = [1, 2, 3, 4]
print(sum(l))
res = 0
for a in l:
    res = res + a
print(res)

#avd of a list
avlst = [10, 20, 90, 30, 40, 50]
print('The Result = ', sum(avlst) / len(avlst))

#copying list elements
l1=['a','b','c']
l2=l1[:]
print(l2)

#creatung the list at run time
num=int(input("enter a total number of elements to be added in list:"))
l=[]
for i in range(num):
    value=int(input("enter list element"))
    l.append(value)
print(l)

#counting even and odd numbers in list
even_list=0
odd_list=0
for i in l:
    if i%2 == 0:
        even_list+=1
    else:
        odd_list+=1
print(even_list,odd_list)

#counting the elements in list
from collections import Counter
l=[1,2,2,3,4,4]
print(Counter(l))

#differences in lists
l1=[1,2,4,6,8,9]
l2=[1,3,5,7,11,9]
print(list(set(l1)-set(l2)))#converting list to set to remove duplicates and finding the differences
print(list(set(l2)-set(l1)))

#left rotate a list by n
l=[1,2,3,4]
rotate=int(input("enter a posistion"))
l1=l[rotate:]+l[:rotate]
print(l1)'''

l=[]
tar=int(input("enter a number"))
num=int(input("enter the number of elements that you want in list"))
for i in range(num):
    l1=int(input("enter some value in list"))
    l.append(l1)
print(l)
for i in l:
    if l[i]+l[i+1] == tar:
        print(l[i],l[i+1])
    else:
        print("didn't get the some")
