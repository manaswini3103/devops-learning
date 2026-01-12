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

- A commit represents a specific change or set of changes made to the project's files at a particular point in time.
- Each commit is a snapshot of the entire repository at that moment.
- Commits form the linear history of a branch, and new commits are added on top of previous ones, moving the branch pointer forward.
- Every commit has a unique SHA-1 hash identifier and includes information such as the author, committer, timestamp, and a commit message describing the changes.
- Commits are mutable in the sense that they are part of a branch's active development, and the branch head moves with new commits.

```bash
git commit -m "message of the changes made"
```

## tag

- A tag is a label used to mark a specific commit in your project's history.
- Tags are mainly used
    - To mark software release versions (v1.0, v2.3.5)
    - To reference stable points in the code
    - To easily roll back to or download a specific version
    - To create GitHub release notes
- Think of a tag as a sticky note you attach to a commit so it's easy to find later.

**Tags give meaningful names:**

- v1.0   → First public release  
- v1.1   → Minor update  
- v2.0   → Major changes  

### Types of Tag

1. Lightweight Tag

A simple label (just a pointer to a commit), It doesn't have any extra metadata and they are not intended to be moved.

````bash
git tag v1.0           # creating lightweight tag
git push origin v1.0   # push to github
````

```bash
git tag -d v1.0        # to delete a tag locally
git push origin --delete v1.0 # deletes a tag at remote
git tag                # lists the tags
git show v1.0 #it'will show tagger info, message, commit detials
```

2. Annotated Tag

- These are stored as full Git objects, containing metadata like:
    - tagger's name
    - email
    - date
    - tagging message 
- These are generally preferred for releases as they provide more information

```bash
git tag -a v1.0 -m "Initial stable release"  # -a refers to annotated tag
git push origin v1.0

git tag -a v1.0 a1b2c3d4 -m "Tagging previous release" # cretaing tag for particular hash - a1b2c3d4
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

git remote -v
git remote set-url origin https://github.com/manaswini3103/MavenHelloWorld
git branch -M main
git push -u origin main

## commit vs tag

| Feature             | Commit                              | Tag                                |
|---------------------|---------------------------------------|-------------------------------------|
| What it is          | Snapshot of changes                   | Label pointing to a commit          |
| Changes over time?  | Yes, new commits are created          | No, tag stays fixed                 |
| Has message?        | Yes (commit message)                  | Yes, if it's an annotated tag       |
| Used for?           | Every change you make                 | Marking releases or milestones      |
| Identified by       | Long hash (e.g., a1b2c3...)           | Friendly name (e.g., v1.0)