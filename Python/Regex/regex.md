# Regex
- Regular expressions (regex or regexp) in Python provide a powerful way to search, match, and manipulate strings based on specific patterns.
- The **re** module in Python's standard library provides the functionality for working with regular expressions.

**Raw Strings:** - It is best practice to define regex patterns using raw strings (prefixing the string with r, e.g., r"pattern"). This prevents backslashes from being interpreted as escape sequences by Python, which is crucial as backslashes are frequently used in regex patterns for special sequences.

## Metacharacters
These are special characters with specific meanings in regex patterns. Examples include:
- .: Matches any character (except newline).
- ^: Matches the beginning of a string.
- $: Matches the end of a string.
- *: Matches zero or more occurrences of the preceding character/group.
- +: Matches one or more occurrences of the preceding character/group.
- ?: Matches zero or one occurrence of the preceding character/group.
- []: Matches any single character within the brackets.
- |: Acts as an OR operator.
- {}: Indicate the number of occurrences of a preceding regex to match.
- \: Used to drop the special meaning of character following it.
- (): Enclose a group of Regex.

## Special Sequences
These are sequences that represent common character sets. Examples include:
- \d: Matches any digit (0-9).
- \D: Matches any non-digit character.
- \w: Matches any word character (alphanumeric + underscore).
- \W: Matches any non-word character.
- \s: Matches any whitespace character.
- \S: Matches any non-whitespace character.

## Regex Functions
**1. re.search(pattern, string)**
It searches for the first occurrence of a pattern in a string. It returns a match object if found, otherwise None.
**ex**
```python
import re
s = 'A computer science portal'
match = re.search(r'portal', s)
print('Start Index:', match.start()) #prints the starting index of the matched string.
print('End Index:', match.end())     #prints the ending index of the matched string
#output: Start Index: 34, End Index: 40
```
**2. re.findall(pattern, string)**
Returns all non-overlapping matches of a pattern in the string as a list. It scans the string from left to right.
**ex**
```python
import re
    text = "apple banana apple orange"
    matches = re.findall(r"apple", text)
    print(matches) # Output: ['apple', 'apple']
```
**3. re.compile(pattern)**
Compiles a regular expression pattern into a regex object, which can be used for more efficient repeated matching.
**ex**
```python
import re
pattern = re.compile(r"\d+") # \d+ - matches sequence of digits, \d - matches single digits
text = "There are 123 numbers here."
matches = pattern.findall(text)
print(matches) # Output: ['123']
```
**4. re.split(paatern, string)**
- Splits a string wherever the pattern matches. The remaining characters are returned as list elements.
- Syntax: re.split(pattern, string, maxsplit=0, flags=0)
**pattern**: Regular expression to match split points.
**string**: The input string to split.
**maxsplit (optional)**: Limits the number of splits. Default is 0 (no limit).
**flags (optional)**: Apply regex flags like re.IGNORECASE.
**ex**
```python
import re
print(re.split('\W+', "Word's words Words, at 11:02 AM'")) #takes the nonword characters to split like apostrophie or space or colon or coma
#output: ['Words', 'words', 'Words']
```
**5. re.sub(pattern, repl, string)**
- Replaces all occurrences of a pattern in a string with a replacement string.
- Syntax: re.sub(pattern, repl, string, count=0, flags=0)
**pattern**: The regex pattern to search for.
**repl**: The string to replace matches with.
**string**: The input string to process.
**count (optional)**: Maximum number of substitutions (default is 0, which means replace all).
**flags (optional)**: Regex flags like re.IGNORECASE.
**ex**
```python
import re
# Case-insensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE)) #output: S~*ject has ~*er booked already
```
**6. re.subn(pattern, repl, string)**
- It works just like re.sub(), but instead of returning only the modified string, it returns a tuple: (new_string, number_of_substitutions)
**ex**
```python
import re
# Case-insensitive replacement of all 'ub'
print(re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
#output: ('S~*ject has ~*er booked already', 2)
```
**7. re.escape(string)**
- It adds a backslash (\) before all special characters in a string.
- This is useful when you want to match a string literally, including any characters that have special meaning in regex (like ., *, [, ], etc.).
**ex** This example shows how re.escape() treats spaces, brackets, dashes, and tabs as literal characters.
```python
import re
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))
```