# Resetting and Reverting

Git offers two primary commands for undoing changes: git reset and git revert. While both achieve a form of "undo," their mechanisms and implications for commit history differ significantly.

## Git Reset

- Used to move the current branch pointer backward and optionally modify the working directory and staging area.
- Reset rewrites commit history. **Never use reset on commits that were already pushed to a shared repo**.
- Rewriting commit history means changing the existing sequence of commits in a Git repository, instead of simply adding new commits on top
(You are editing, deleting, reordering, or replacing old commits as if they never happened).
- operates at the commit level, moving the entire branch pointer.

**Example**  
A → B → C → D → E (latest)  
A → B → C' → D' → F (new commits)

### When to use:

- You want to erase commits from history (local only).
- You want to unstage or remove changes before pushing.

### Types of Reset

#### To reset staging changess

```bash
git reset <filename>
git reset # for all the staged files
```

#### To reset commited changes

1. `git reset --soft <commit-hash>`
- Moves HEAD to an earlier commit.
- Keeps staged and working directory files as is.
- Useful for: Re-doing the last commit without losing changes.

```bash
git reset --soft HEAD~1
```

2. `git reset --mixed <commit-hash>` (default)
- Moves HEAD to an earlier commit.
- Keeps working directory.
- Unstages your files.

```bash
git reset HEAD~1
```

3. `git reset --hard <commit-hash>`
- Moves HEAD to an earlier commit.
- Deletes all changes in staging and working directory.
- Dangerous — cannot easily be undone.

```bash
git reset --hard HEAD~1
```

## Git Revert

Git Revert is used to undo the changes introduced by a specific commit by creating a new commit that reverses those changes. This preserves the original commit history and is **considered a "safe" way to undo changes, especially in shared repositories**.

- Unlike reset, revert does not rewrite history; it adds a new commit.
- Targets a specific commit and creates a new commit to undo its changes.
- When to use:
    1. You want to undo changes but keep history intact.
    2. You already pushed the commit to GitHub (or any remote).

### Example

```bash
git revert <commit-hash>
git revert 3ab4c2d
```
- This opens an editor to confirm the revert message and makes a new commit reversing the changes.