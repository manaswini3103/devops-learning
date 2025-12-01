'''#print the ascii value of a character
char='a'
print(ord(char))

#ascii value of total characters in string
str=input("enter a string")
for i in range(len(str)):
    print("ascii value of",str[i],"is",ord(str[i]))

#concatination
str1="hello"
str2="world"
print(str1+" "+str2)

#Copy a String
str1 = input("Please Enter Your Own String : ")
str2 = str1 #both point to the same string
str3 = str1[:] #creates a new string (a duplicate)
print("The Final String : Str2  = ", str2)
print("The Final String : Str3  = ", str3)

#palindrome or not
s=input("enter a string")
if s==s[::-1]:
    print("given string is palindomr")
else:
    print("not a palindrome") 
#(or)
string=input("enter a string")
str1=""
for i in string:
    str1=i+str1
print(str1)
if string==str1:
    print("this is palindrome")
else:
    print("not a palindrom")

#anagram or not
str="triangle"
str1="integral"
if sorted(str)==sorted(str1):
    print("yes")
else:
    print("no")

#program to find first occurance of a character in a string
str=input("enter a string")
char=input("enter a character")
flag=0
for i in range(len(str)):
    if str[i] == char:
        flag=1
        break
if flag==1:
    print("found at",i)
else:
    print("not found")

#program to find last occurance of a character in a string
str=input("enter a string")
char=input("enter a character")
flag=0
for i in range(len(str)):
    if str[i] == char:
        flag=i
if flag==0:
    print("not found")
else:
    print("found at",i)'''

#to find all occurences of a string
str=input("enter a string")
char=input("enter a character")
for i in range(len(str)):
    if str[i] == char:
        print(char,"is found at",i)

# Python program to Count Alphabets Digits and Special Characters in a String
string = input("Please Enter your Own String : ")
alphabets = digits = special = 0
for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1        
print("\nTotal Number of Alphabets, digits and special characters in this String :  ", alphabets,digits,special)

#program to remove odd characters string
str1 = input("Please Enter your Own String : ")
str2 = ''
for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
print("Original String :  ", str1)
print("Final String :     ", str2)