# branching

- Branching allows you to create independent lines of development within a single repository.
- Each branch represents a separate set of changes, enabling you to work on new features, bug fixes, or experimental changes without affecting the stability of the main project by creating a new branch. 
- Branch means if many teams are working on a single project, they can get their own copy of the code/repo.
- It has the concept of tree and branches.

## commands

1. git branch (to check for the branch)
2. git branch -M main (to rename branch)
3. git checkout `<branch name>` (to navigate to different branches)
4. git checkout -b `<new branch name>` (to create new branch)
5. git branch -d `<bracnh name>` (to delete branch)

# merging

- Merging integrates changes from one branch into another.
- This process combines the commit histories of two branches, allowing you to incorporate completed work from a feature branch back into the main codebase (e.g., main or master).

## Two ways of merging

### way1

We can use this if we want to merge from Local machine

- git diff `<branch name>` (to compare commits, branches, files and more)
- git merge `<branch name>` (to merge two branches)

### way2

Get a **PR (Pull Request)**. PR lets you tell others about changes we have pushed to a branch in a GitHub repo. A senior developer can know the changes made and to tell whether those changes could be merged to main branch or not.  

## Merge Conflicts

If both branches have made changes to the same lines of code in the same file, Git cannot automatically decide which changes to keep.  
This results in a **merge conflict**, which must be resolved manually by:

1. Editing the conflicted files  
2. Choosing which changes to keep  
3. Staging the resolved files  
4. Committing the merge resolution  

---

## Types of Merges

### 1. Fast-Forward Merge
- Occurs when the target branch has **not diverged** from the source branch.  
- No new commits were added to the target branch after the source branch was created.  
- Git simply **moves the target branch pointer** to the latest commit of the source branch.  
- Results in a **linear history**.

#### Example
```bash
git checkout main
git merge feature-branch
```

### 2. Three-Way Merge (Recursive Merge)
- Occurs when **both branches have unique commits (diverged)** since their common ancestor.  
- Git combines the changes and creates a **new merge commit**.  
- The history becomes **non-linear** because of the additional merge commit.
- Git creates a merge commit to combine histories.
- Uses three commits:
    1. The two branch tips
    2. Their common ancestor

#### Example
```bash
git merge feature-branch
```

### 3. Squash Merge
- Combines all commits from a branch into one single commit.
- Useful for maintaining a clean commit history.
- Does not automatically delete the branch.

#### Example
```bash
git merge --squash feature-branch
git commit
```

### 4. Rebase and Merge
- Replays the commits of a branch on top of another branch.
- Produces a linear commit history.
- Does not create a merge commit.

#### Example
```bash
git rebase main
git checkout main
git merge feature-branch
```

### 5. No-FF (No Fast-Forward) Merge
- Forces Git to always create a merge commit, even if a fast-forward is possible.
- Preserves branch structure.

#### Example
```bash
git merge --no-ff feature-branch
```
