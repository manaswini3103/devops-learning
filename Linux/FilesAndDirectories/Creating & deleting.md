# create & delete file/directory	
- touch - creates a 0 bites file. Ex: touch filename.txt
- echo "Hello World" > filename.txt (Writes Hello World content into the file, without using editor mode.)
- cat filename.txt – displays the content of file.
  - cat > filename.txt - create file and allows to write, to save the file we’ll press ctrl+D.
  - cat >> filename - appends new lines to existing file but doesn't overwrite the data.
- nano - creates a file if filename doesn't exist, almost it'll give options like text editor
- vi – editor mode - creates a file if filename doesn't exist and allows to write into the file. To save it press “Esc” key and “:wq” – to write and quit. Ex: vi filename.txt
- mkdir dirname -creates directory
- rmdir dirname- removes empty dire
- rm - removes file
  - rm -rf - removes a dir - recursively and forcibly removes the dir
  - rm -f filename -> -f - forcibly removes the file.
we need to be cautious with rm command as there won't be any recycle bin in Linux.
- tree is the command which displays the directory structure.
