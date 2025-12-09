# Branching

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

# Branching strategies

Git branching strategies provide frameworks for managing code changes and collaboration within a Git repository. Different strategies suit different team sizes, project complexities, and release cycles. Here are some common types:

## Git Flow

Git Flow is a strict and organized branching model used in big projects.

**How it works**

- feature branches → each feature is built on a branch like feature/login
- develop → where developers integrate work before release
- release branches → prepared just before a release
- hotfix branches → quick fixes applied directly to the production code
- main → holds the stable code that is released to customers

**When to use**

- Big teams
- Apps with planned releases (e.g., once a month)

## GitHub Flow

A simple and lightweight process commonly used by small teams and companies deploying all the time.

**How it works**

- Work directly from main
- Create a new short-lived branch for each task/feature
- Open a pull request
- Get it reviewed and merge it into main
- After merging Deploy immediately

**When to use**

- Small teams
- Continuous deployment (many releases per day)

## GitLab Flow

GitLab Flow is a flexible model that combines GitHub Flow + some ideas from Git Flow.

**How it works**

Two common styles:

1. Environment-based branches
- main → latest code
- staging → testing environment
- production → live environment

2. Release branches
- Each release has its branch, e.g., release/2.0

**When to use**

- Teams using CI/CD pipelines
- Projects with staging/production environments

## Trunk-Based Development

A fast-moving, modern practice used by high-performing DevOps teams.

**How it works**

- Developers commit directly to main (the “trunk”)
- Feature branches exist but last only hours or 1 day
- Feature flags are used to hide unfinished features
- This minimizes merge conflicts and encourage continous integration

**When to use**

- Teams deploying multiple times a day
- Skilled teams with strong testing & automation

## Release Branching

A method where each release gets its own branch.

**How it works**

- A release branch is created from the main development branch (e.g., develop)
- when a release is imminent. Bug fixes and minor adjustments are applied to this branch until the release is ready
- After which it's merged into the main production branch (e.g., master) and often back into the development branch.

**When to use**

- Software that needs long-term support
- Multiple active versions (e.g., v1.2, v2.0)

## Feature Branching

A fundamental concept where each new feature or bug fix is developed in its own dedicated branch.

**How it works**

- main → stable code
- Create a branch for a specific task, work on it, and then merge it back into the main development branch (e.g., main or develop) upon completion. This isolates work and facilitates code reviews.
- feature/signup, feature/cart → developers work separately

**When to use**

- Most typical software teams
- Code review is important
- Features need isolation

## Forking Workflow

Often used in open-source projects for security and control.

**How it works**

- Developers create a fork (their own copy of the repo)
- Work on feature branches
- Submit a pull request to the main project

**When to use**

- Open-source projects
- Projects with many external contributors
- When you don’t want everyone to have write access

## Optimized Recursize Tree

- It is Git’s new default merge strategy starting from Git 2.34 (released in 2021), replacing the old recursive strategy.
- ORT is a merge algorithm used by Git to automatically combine changes from two branches.

### Summary in One Sentence

- Git Flow → Structured and heavy
- GitHub Flow → Simple and fast
- GitLab Flow → Flexible, good for CI/CD
- Trunk-Based → Very fast, modern DevOps
- Release Branching → Best for long-term version support
- Feature Branching → Easy and common
- Forking Workflow → Best for open-source
