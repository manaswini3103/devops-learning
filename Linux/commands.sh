#help and man commands
ls --help
man ls
apropos list

#links
ln -s sourcefile nameoflinkfile #soft link
ln sourcefile nameoflinkfile    #hard link

#creating files and directories
echo "Hello World" > filename.txt
cat > filename.txt
cat >> filename
nano filename
vi filename
mkdir dirname
rmdir dirname
rm filename
rm -f filename
rm -rf filename

#reading files and directories
ls fileordir
ls -l filename
ls -lrt filename
cat filename
head filename.txt 
tail filename.txt

#managing files and directories
file filename
stat filename
cd filename/dirname
cd ..
pwd
cp /dir/filename /dir1/dir2
cp -r /dir1/dir2/* /dir/
mv /dir/filename /dir1/dir2
find [path] [options] [expression/filenames/sizes]
grep [options] pattern [files]
sed [options] 'script' [files]
awk [options] 'pattern {action}' input-file > output-file

#file permissions
chmod u+x,g-w,o=w filename
chmod 777 filename
chown [options] new_owner:new_group file_name

#user management
useradd username
id username
passwd username
usermod -u new_Userid username
userdel -r username

#process management
ps -ef
top
kill -9 PID

#system management
history
free
du -sh
df -sh
whereis ls


