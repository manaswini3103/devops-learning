# Pipeline

A pipeline is an automated sequence of steps used to build, test, and deploy software. Pipelines are widely used in CI/CD. Instead of running commands manually, pipelines ensure: Consistency, Automation, Faster feedback and Fewer human errors.

## Typical Pipeline Stages

- Build – Compile code, install dependencies
- Test – Run unit/integration tests
- Package – Create artifacts (JAR, Docker image, etc.)
- Deploy – Deploy to staging or production

## Popular Pipeline Tools

- GitHub Actions
- GitLab CI/CD
- Azure DevOps Pipelines
- Jenkins
- CircleCI

# YAML

YAML stands for YAML Ain’t Markup Language. It is a human-readable data format used to define configuration files—especially pipelines.

## Why YAML is used for Pipelines

- Easy to read and write
- Clean indentation-based structure
- Works well for defining steps and stages

## Basic YAML Syntax Rules
1. Key–Value Pairs
```YAML
key: value
name: Build Pipeline
version: 1.0
```
2. Indentation (Very Important)
- Uses spaces, not tabs and Indentation defines hierarchy
```YAML
job:
  name: build
  runs-on: ubuntu-latest
```
3. Lists (Sequences): Lists starts with dash
```YAML
languages:
  - Python
  - Java
  - Go
```
4. Dictionaries (Maps): Maps contain multiple key-value pair
```YAML
database:
  host: localhost
  port: 5432
  user: admin
```
5. Comments
# This is a comment
6. Strings
- Plain strings
```YAML
env: production
```
- Quoted strings: Use quotes when special characters exist:
```YAML
command: "echo Hello, World!"
```
- Multiline Strings
  - Literal (|) – preserves line breaks
  ```YAML
  script: |
    echo "Build started"
    mvn clean install
  ```
  - Folded (>) – joins lines
  ```YAML
  message: >
    This is a long message
    written in multiple lines
  ```
7. Numbers, Booleans, and Null
```YAML
retries: 3
enabled: true
disabled: false
timeout: null
```
8. Environment Variables Example
```YAML
env:
  JAVA_HOME: /usr/lib/jvm/java-17
  APP_ENV: prod
```

## Simple CI Pipeline Example (YAML)
GitHub Actions Example
```YAML
name: CI Pipeline

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build project
        run: mvn clean package

      - name: Run tests
        run: mvn test
```

### What this does
- Triggers on every git push
- Runs on a Linux VM
- Builds and tests a Maven project

## Common YAML mistakes 

| Error                         | Reason                   |
| ----------------------------- | ------------------------ |
| Tabs instead of spaces        | YAML does not allow tabs |
| Wrong indentation             | Breaks hierarchy         |
| Missing colon (`:`)           | Invalid syntax           |
| Mixing list & map incorrectly | Parsing error            |


## Pipeline Concepts

| Concept          | Meaning                                         |
|------------------|-------------------------------------------------|
| **Stage**        | Logical grouping (build, test, deploy)          |
| **Job**          | A set of steps executed on a runner             |
| **Step**         | Single task (command or action)                 |
| **Runner/Agent** | Machine that executes the pipeline              |
| **Artifact**     | Output files from pipeline                      |
| **Trigger**      | Event that starts pipeline (push, PR, schedule) |
