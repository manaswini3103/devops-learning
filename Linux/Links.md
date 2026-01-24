# Links in Linux

A link is a file that acts as a reference to another file.  
Links help avoid having multiple copies of the same file in different locations.  
The command used to create links is "ln"

There are two types of links

## 1. Soft Link:
- It’s not going to create a file; it just refers to the original file. 
- If original file (test.txt) is deleted, link is broken and data is lost.
- Points to a file on the disk (relative path).  
**relative** – it cannot link if the source file is not in the same path and if the file linked to the source file is not in the file system.  
ex: **ln -s sourcefile nameoflinkfile**  
    **ln -s test.txt test1.txt**  
- If we edit in test1.txt, it will be reflected in original test.txt file as well.

## 2. Hard Link:
- It is like a backup file; it creates copy of an existing file which acts as backup file.
- Points to data on the disk(inode)  
ex: **ln sourcefile nameoflinkfile**  
    **ln test.txt test2.txt**
- It is pointer to the data that the original file references.
- Hard links can be moved around the filesystem, and it doesn’t matter if the original file (test.txt) is moved/removed, because it points to the data of the file instead of the file itself.
