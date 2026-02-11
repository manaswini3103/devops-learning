# for i in s:
#     if i=='l':
#         count+=1
# print(count)

s = "hello world hello world hello world hello"
# visited = ""
# print(len(s))
# for i in range(len(s)):
#     if s[i] != " " and s[i] not in visited:
#         count = 0
# 
#         for j in range(len(s)):
#             if s[i] == s[j]:
#                 count += 1
# 
#         if count > 1:
#             print(s[i], ":", count)
# 
#         visited += s[i]
# 
word = "hello"
wordcount = 0

for i in range(len(s) - len(word) + 1):
    match = True
    for j in range(len(word)):
        if s[i + j] != word[j]:
            match = False
            break
    if match:
        wordcount += 1

print("hello count:", wordcount)

    