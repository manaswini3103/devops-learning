When people say “.git file exclusions”, they usually mean excluding files from Git tracking using .gitignore (not excluding the .git folder itself).

## .gitignore
- The .git folder must NEVER be in .gitignore
- tells Git: “Do NOT track these files or folders”
- Typical use cases:
  - Build outputs
  - Logs
  - OS files
  - IDE configs
  - Secrets
- It is a normal text file in the root of your repository
- Where .gitignore lives  
devops-learning/  
│── .git/  
│── .gitignore  
│── README.md  
│── index.html  

### Common .gitignore examples

1. Ignore OS & editor files
```bash
# Windows
Thumbs.db
desktop.ini
# VS Code
.vscode/
```
2. Ignore build & temp files
```bash
node_modules/
dist/
target/
*.log
```
3. Ignore Python
```bash
__pycache__/
*.pyc
.venv/
```

## Important rule (very common confusion)
- .gitignore does not work on files already tracked. If a file was committed earlier, Git will keep tracking it.
- Fix:  
git rm --cached filename  
git commit -m "Stop tracking filename"
- Check ignored files: git status --ignored
- Or for a specific file: git check-ignore -v filename

## Special cases (advanced)
- Ignore globally (all repos on your machine): git config --global core.excludesfile ~/.gitignore_global
- Ignore locally (not committed): .git/info/exclude
