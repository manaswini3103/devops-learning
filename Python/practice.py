'''for i in "geeks":
    if i == "e":
        break
print(i)

f=open("sample.txt","w")
f.write("hello world")
f=open("sample.txt","r")
print(f.read())

string=input("enter")
str2=""
for i in string:
    str2=i+str2
print(str2)

l=[1,2]
s="hello world"
for index, item in enumerate(l):
    print(str(item)+":"+s.split()[index])

nums=[1,2,9]
target=3
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print(i,j)

s='abcab'
maxLength = 0
l = []
for i in s:
    if i in l:
        break
    l.append(i)
    maxLength = len(l) if len(l)>maxLength else maxLength
print(maxLength)

s="III"
roman = {'I':1, 'V':5, 'X':10, 'L':50,
                 'C':100, 'D':500, 'M':1000}
result = 0
for i in range(len(s)):
    curr = roman[s[i]]
    next_val = roman[s[i+1]] if i+1 < len(s) else 0
            
    if curr < next_val:
        result -= curr
    else:
        result += curr
print(result)'''

strs = ["flower","flow","flight"]
s=sorted(strs)
print(s[0],s)