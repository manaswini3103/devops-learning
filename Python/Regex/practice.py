#re.search()
#ex1
import re
text = "The quick brown fox."
match = re.search(r"quick", text)
if match:
    print("Found",match.group(0)) #match.group(0) prints thie matched strind

#ex2
import re

m = re.search(r"(\d{3})-(\d{2})", "Phone code: 123-45")
print(m)
print("Full:", m.group(0)) #entire match "123-45" here group 123-45 is divided into 2 groups, group1 is 123, group2 is 45
print("Group 1:", m.group(1)) #first parentheses capture "123"
print("Group 2:", m.group(2)) #second parentheses capture "45"

#re.findall()
import re
string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""            
match = re.findall(r'\d+', string) #\d+ to find all sequences of one or more digits in the given string
print(match)

#re.compile()
#ex1
import re
p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))

#ex2
import re
p = re.compile('\d') #\d - to find all sequences single digits
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

#re.split()
import re
print(re.split('\W+', "Word's words Words, at 11:02 AM'")) #takes the nonword characters to split like apostrophie or space or colon or coma
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE)) # takes a-f and A-F to split given string, re.IGNORECASE ignores case
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here')) # takes a-f to split th string
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM')) #splits the string based on digits

#re.sub()
import re
# Case-insensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
# Case-sensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already'))
# Replace only the first 'ub', case-insensitive
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))
# Replace "AND" with "&", ignoring case
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

#re.escape()
import re
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))