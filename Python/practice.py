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

'''strs = ["flower","flow","flight"]
s=sorted(strs)
print(s[0],s)

# valid-parentheses Problem
class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                a.append(s[i])
            else:
                if not a: # means that if a is empty
                    return False
                top=a.pop() # The stack does not remember old values once popped. it will always be one element at a time
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(a)==0
sol = Solution()
print(sol.isValid("(([]{}"))


# Search Insert Position (two pointer concept)
class Solution(object):
    def searchInsert(self, nums, target):
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]>=target:
                j=mid-1
            else:
                i=mid+1
        return i
n=[1,3,4]
t=5
sol = Solution()
print(sol.searchInsert(n,t))

# Plus One
class Solution:
    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits
sol = Solution()
print(sol.plusOne([1,2,3,9]))'''

# longest common prefix
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # taking the first word
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Compare with all other strings
            for word in strs:
                if i >= len(word) or word[i] != char: #if we keep the word[i]!=char condition first then it would throw index out of bound issue
                    return strs[0][:i]

        return strs[0]
sol = Solution()
print(sol.longestCommonPrefix(["flows", "flow", "flowsi", "flowig"]))

