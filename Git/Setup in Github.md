# Steps in Github

- create an account in Github.
- create a repository, if we want along with readme.md, where **md** is mark down.
- Edit the **readme.md** and make the first commit (saving that we added something or some changes).
- we can even add a message about the changes that we made while commitiing.
- If we want to print something in next line we can use `<br>` or give 2 spaces to the before line.

# Setting Up Git

- We need to install Visual Studio Code
- We also need to install Git Bash in Windows.

## Configuring Git

Configuring Git primarily involves setting up user identity and other preferences, which can be done at a global, system, or local level.  
Mainly we'll use **Gloabal User Identity** and **Viewing Configurations**.

### 1. Setting Global User Identity**

This configuration applies to all repositories on your system.

#### Example
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. Setting Local User Identity

This configuration applies **only to the current repository**, overriding global settings.  
Navigate to your repository directory before running these commands.

#### Example
```bash
git config user.name "Your Name for this Repo"
git config user.email "repo.email@example.com"
```

### 3. Setting System-Wide Configuration

This configuration applies to all users and repositories on the system (requires administrative privileges).  
It is usually stored in /etc/gitconfig.

#### Example
```bash
sudo git config --system user.name "System Name"
sudo git config --system user.email "system.email@example.com"
```

### 4. Configuring the Default Branch Name

Traditionally the default branch was master. Today main is commonly used.

#### Example
```bash
git config --global init.defaultBranch main
```

### 5. Creating Aliases

Shorten frequently used Git commands for convenience.

#### Example
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

#### Use examples:
```bash
git co <branch>    # runs: git checkout <branch>
git br             # runs: git branch
git ci -m "msg"    # runs: git commit -m "msg"
git st             # runs: git status
```

### 6. Viewing Configurations

To list Git configuration settings:

#### Example
```bash
git config --list
```

To view settings for a specific scope:

#### Example
```bash
git config --global --list
git config --local --list
git config --system --list
```

### 7. Removing or Resetting Configurations
Remove a single setting from the global scope.

#### Example
```bash
git config --global --unset user.email
```

#### Unset and set a new value
```bash
git config --global user.email "new.email@example.com"
```

#### Note

After installing Git, these initial configurations ensure your commits are properly attributed and your Git environment behaves as expected.