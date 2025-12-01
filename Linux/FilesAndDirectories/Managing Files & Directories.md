# Managing Files and Directories
- who/whoami/W similar commands
users/id
uptime
man
- file myfile.txt (determines file type)
- stat myfile.txt (display ownership, modification information etc.)
- cd – change directory (switches between directories)
“cd ..” takes back to the previous used folder
- pwd – present working directory
- cp - copy a file
  - cp /root/test.txt /home/chennasa/
  - cp -r /root/dir1/ /home/chennasa/ (recursively copies everything in dir1 to chennasa).
- mv - move a file
- find - find the files or directory's path
- grep - search for a pattern in a file
- diff - finds content diff in 2 files
- sed - search and replace particular pattern
- chmod - changes file permissions
- chown - changes own of a file

## Find Command
Find the files or directory's path. It's exactly like the find option in windows where you can search for a file.
**syn:** find [path] [options] [expression/filenames/sizes]
**Ex:**
[root@omega chennasa]# find . -type d
.
./manaswini
./unpack
[root@omega chennasa]# find . -name *.txt
./filename.txt
**options**
- name "pattern" - Searches files by name (case-sensitive).ex: find ~ -name "notes.txt"
- iname "pattern" - Case-insensitive name search.ex: find ~ -iname "notes.*"
- type f/d - Finds only files (f) or directories (d).ex: find /var/log -type f
- size +10M	- Finds files larger than 10MB.ex:	find / -size +100M
- mtime -7 - Finds files modified in the last 7 days.ex: find ~ -mtime -7
- perm 644 - Finds files with specific permissions.ex:	find ~ -perm 644
- exec - Runs commands on found files (e.g., delete).ex: find . -name "*.tmp" -exec rm {} \;
- empty - Finds empty files/directories.ex: find ~ -empty

## grep (Global regular Expression Print)
picks the required expression from file and print the output.
**syn:** grep [options] pattern [files]
**Ex:** 
[root@omega chennasa]# grep -i “manu” filename.txt (i – case insensitive)
[root@omega chennasa]# grep -w “manu” filename.txt (w – searches for the whole world)
[root@omega chennasa]# grep -n “manu” filename.txt (n – gives the line number of the matched word along with the entire line)
[root@omega chennasa]# grep -c “manu” filename.txt (gives the count of the lines, in which the word is present)
[root@omega chennasa]# grep -v “manu” filename.txt (prints the line that doesn’t match with the pattern)
[root@omega chennasa]# grep -o “manu” filename.txt (prints only the word instead of the entire line)
[root@omega manaswini]# grep –help (helps with the options of grep_
[root@omega manaswini]# grep --help | grep count (in those options we are searching for cout)
  -m, --max-count=NUM       stop after NUM matches
  -c, --count               print only a count of matching lines per FILE

## sed (stream editor)
used to search a word in file and replace it with word required to be in output.
**syn:** sed [options] 'script' [files]
**Ex:**
sed ‘s/old_text/new_text/’ file_name (s – substitute)
sed ‘s/old_text/new_text/ig’ file_name (g : globally changes the value, i:changes the value irrespective of case sensitivity) 
sed -i ‘s/old_text/new_text/g’ file_name (-i : makes the changes in the           actual file)
sed -n ‘5,10p’ file_name 
sed ’10,20d’ file_name

## awk 
awk is used for manipulating data and generating formatted reports.
**syn:** awk [options] 'pattern {action}' input-file > output-file
**Ex:**
awk ‘{print $2}’ table.txt  ( the one in the single codes is the progam and here $2 refers to the column 2 of table.txt)
awk ‘{print $2 “\t” $3}’ table.text (\t: tab, in output it give tab space b/w column 1 & 2)
awk ‘{print $2 “\t” $3}’ tale.txt | sort -n ( here sort is sorting with the ID numbers)

