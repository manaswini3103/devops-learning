# Git Commands

Here are some of the most commonly used Git commands.

## clone

- We have two repositories in Github
    1. Remote Repository:  
    This is a version of your project hosted on a server, such as GitHub.com. Its purpose is to share code among team members, provide a backup, and facilitate collaboration. 
    2. Local Repository:  
    This is the copy of the project stored on your own computer. You make changes, commit them, and manage branches here without needing an internet connection.
- Clone means cloning a repository on our local machine from remote for the first time. It also copies Version History.
- It takes the HTTP link from the **code section** in Github.
- If it is a git repository we'll see **.git** folder, when we give `ls -a` or `ls -Hidden` which list all the hidden files.

### example
```bash
git clone <-some link->
```

## status

Displays the state of the code.

- If we change something in code from Visual Studio Code, and if we want to check for the status of those files, we can give:  
```bash
git status
```
- we have 4 types status.
1. **untracked**: These are the new files that git doesn't yet track.
2. **modified**: when we change something in the existing files.
3. **staged**: When we add the changes of the file and it's ready to be commitied.
4. **unmodified**: whne nothing is changed.

## add

Adds new or changed/modified files in your working directory to Git staging area

```bash
git add <file name> #adds the changes of the particular file
git add . #adds all the changes 
```

## commit

It is the record of the change

```bash
git commit -m "message of the changes made"
```

## push

To upload the local repository content/changes/additions to the remote repository.

```bash
git push origin main
```

### origin
This is the default name (or "shortname") Git gives to the remote repository you originally cloned a project from. It is a convention, not a requirement, but it is used very commonly

### main
It is the branch name.

If we want to push something to rempote repository, we can create shortcut

```bash
git push -u origin main
```

where **-u** creates shortcut. so when we want to push something from next we can give:  
```bash
git push
```

## init

This is used to create a new Git repository in Local machine.
1. git init
2. git remote add origin `<link>`
3. git remote -v (to verify remote)

- We can creat a directory in VS code terminal using `mkdir dirname`.
- If we list that directory we'll not get **.get** folder. so we'll give the following command to create the **.git** folder.  
```bash
git init
```
- In the same way we'll manually add some files in that directory, then we'll **add** and **commit** those files.
- For this directory to get reflected in Remote repository, we'll go to Remote repo and create a new repo with same name as given local machine.
- Then we'll give the following command in VS code before pushing it to Git repo.  
```bash
git remote add origin <link> #get the link from the code section of the new remote repo which we created
```
- Then we use **push** command to push the changes to Remote repo.

## pull

It's used to fetch and download content/changes made in Remote repo and update them in Local repo to match both the contents.  
Updates and existing Local repo with the changes made in Remote repo.

```bash
git pull origin main
```
