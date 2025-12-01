# Regex
- Regexps are acronyms for regular expressions.
- Regular expressions are special characters or sets of characters that help us to search for data and match the complex pattern.
- Regexps are most commonly used with the Linux commands:- grep, sed, tr, vi.

## Basic Regular Expressions
1.  .	It is called a wild card character, It matches any one character other than the new line.
2.  ^	It matches the start of the string.
3.  $	It matches the end of the string.
4.  *	It matches up to zero or more occurrences i.e. any number of times of the character of the string.
5.  +   1 or more occurrences
6.  ?	0 or 1 occurrences
7.  \	It is used for escape following character.
8.  ()	It is used to match or search for a set of regular expressions.
9.  a   The character a
10. ab  The string ab
11. a|b a or b
12. {2} prints the string with given character which was repeated twice
13. {2,5}   prints the string with given character which was repeated between 2 to 5 times
14. {2,}    prints the string with given character which was repeated 2 or more times
15. [ab-d]  One character of: a, b, c, d
16. [^ab-d] One character except: a, b, c, d
17. [\b]    Backspace character
18. \d  One digit
19. \D  One non-digit
20. \s  One whitespace
21. \S  One non-whitespace
22. \w  One word character
23. \W  One non-word character
24. \Z  End of string, ignores m flag
25. \b  Word boundary
26. \B  Non-word boundary
27. \G  Start of match
28. \A  Start of string, ignores m flag

**Examples**
- grep -E App.e filename.txt           (finds the starting with 'App' and ending with 'e', in middle it could be anything)
- grep -E ^B filename.txt              (finds the lines starting with 'B')
- grep -E e$ filename.txt              (finds the lines starting with 'e')
- grep -E ap*le filename.txt           (finds the lines with p* - zero or more 'p' character)
- grep -E "\ " filename.txt            (finds the lines with one space)
- grep -E "(fruit)" filename.txt       (finds the lines starting with 'fruit' word)
- grep -E Ch? filename.txt             (finds the lines starting with 0 or 1 occurance of 'h')
- grep -E "r{2}" filename.txt          (finds the lines starting with 'rr' character in it)
- grep -E "\W" filename.txt            (finds the lines starting with One non-word character)
- grep -E "\w" filename.txt            (finds the lines starting with One word character)
- grep -E "\s" filename.txt            (finds the lines starting with One whitespace)
- grep -E "[^berry]" filename.txt      (finds the lines starting without word 'berry')
- grep -E "fruit|berry" filename.txt   (finds the lines starting with either 'fruit' or 'berry')

