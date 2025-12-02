# File Permissions	
- rwxrwxrwx
 - user group others
 - user – represents user or owner of the group
 - group – represents the group that owns the file
 - others – represents all other users not in the that owns the file.
- rwx- Read, Write and eXecute
 - Read – can see, but can’t modify
 - Write – someone can make a change to file, but can’t read the content
 - eXecute – can run the script
- chmod – change permissions on file by modifying the file mode bits
**ex:**
chmod 755 filename
chmod 644 filename

## File Types
`-`  : normal file  
b  : block file (harddisk, floppydisk)  
c  : Character file (keyboard, mouse)  
d  : directory  
I  : Link files (short cut)  

## Two methods to represent permission
1. Octal File Permissions

| Type   | Read (4) | Write (2) | Execute (1) | Result      |
|--------|----------|-----------|-------------|-------------|
| User   | R        | w         | x           | 7 (4+2+1)   |
| Group  | R        | -         | x           | 5 (4+1)     |
| Others | R        | -         | -           | 4 (4)       | 

2. Symbolic File permissions

| Type        | Read (r) | Write (w) | Execute (x) | Result      |
|-------------|----------|-----------|-------------|-------------|
| User (u)    | +        | +         | +           | u = rwx     |
| Group (g)   | =        | -         | -           | g = r       |
| Others (o)  | -        | -         | -           | o = ---     |
| All (a)     |          |           |             |             |

**‘+’** adds permissions, **‘-‘** removes permissions, **‘=’** adds specified permission but removes others.

### Comparing Octal and Symbolic Values:  
| Octal Value | Symbolic Value              | Result      |
|-------------|------------------------------|-------------|
| 777         | a + rwx                       | rwxrwxrwx   |
| 755         | u = rwx, g = rx, o = rx       | rwxr-xr-x   |
| 644         | u = rw, g = r, o = r          | rw-r--r--   |
| 700         | u = rwx, g = ---, o = ---     | rwx------   |  

### Symbolic value changes:  
| Original     | Symbolic Value | Result      |
|--------------|----------------|-------------|
| rw-r--r--    | a + x          | rwxr-xr-x   |
| rwxrwxrwx    | g = w, o = r   | rwx-w-r--   |
| rwxr-xr-x    | o - rx         | rwxr-x---   |
| rwxrwxrwx    | a - x          | rw-rw-rw-   |

**Ex:**  
**chmod u+x,g-w,o=w filename**  
**chmod 777 filename**  
**chmod 764 /home/chennasa** (giving directory level permissions)

## chown
Changes the ownership of files and directories to a specific user and/or group.  
**syn:** chown [options] new_owner:new_group file_name  
**ex:**  
- sudo chown -c manu test.txt (c – a comment will be displayed saying that the owner ship is changed, manu – username)
- sudo chown -c :oper test.txt (:oper – changes the group of that file to ‘oper’)
- sudo chown -c sri:dev test.txt (changes the user and group of test.txt to ‘sri’ and ‘dev’ from ‘manu’ and ‘oper’)
- sudo chown -R manu:oper /home/chenna (R – recursively changes the ownership of the files and directories inside the ‘chenna’ directory)
