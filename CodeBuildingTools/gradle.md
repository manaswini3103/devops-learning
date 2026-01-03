# Gradle

Gradle is a open-source modern build automation tool used to build, test, and package software and manages dependencies, while being faster and more flexible than Maven. It is widely used for Java, Kotlin, Android, and multi-language projects.


## Why Gradle Is Used
- Gradle was designed to overcome some limitations of older build tools like Maven and Ant.
- It provides:
 - Faster builds
 - Flexible configuration
 - Less verbose (unnecessary use of words in code, documentation, or communication.) build files
 - Better support for large and complex projects


## Key Concepts in Gradle

### Build Scripts
- Gradle uses a flexible, expressive DSL (Domain-Specific Language) based on Groovy or Kotlin, rather than XML.
- This allows developers to combine declarative configuration with custom programming logic, making build scripts more readable and powerful.
- Files: build.gradle (Groovy DSL), build.gradle.kts (Kotlin DSL)
- Example:
```groovy
plugins {
    id 'java'
}
dependencies {
    implementation 'org.springframework:spring-core:6.0.0'
}
```

### Build System Integration
Supports features from Ant and Maven, including importing Ant projects and using Maven repositories.

### Dependency Management
- Dependencies are declared in the build script and Gradle automatically downloads necessary external libraries/modules from repositories. 
- It supports transitive dependencies. 
- Repositories: Maven Central, Google and Custom repositories.

### Tasks
- Taska are units of work (compile, test, jar) in Gradle.
- These tasks are organized into a Directed Acyclic Graph (DAG), ensuring they run in the correct order based on their dependencies.
- The tasks are the functions that are responsible for a specific role and for creating classes, which makes up development of the Gradle project.
- These tasks help Gradle decide what input is to be processed for a specific output. 
- These can be categorized in two different ways: 
  1. **Default Task**: These are the predefined tasks that are provided to users by Gradle. These are provided to users prior which executing when the users do not declare any task on their own. For example, init and wrap the default tasks provided to users into a Gradle project
  2. **Custom Task**: Custom tasks are the tasks that are developed by the developer to perform a user-defined task. These are developed to run a specific role in a project. Let's take a look at how to develop a Custom Task below.
- Example: Printing Welcome to Earth! with a task in Gradle.  
```groovy
build.gradle : task hello  // build.gradle files are Gradle build configuration files. By default, Gradle uses Groovy DSL. task hello: Defines a Gradle task, where task name is "hello"
{
    doLast   // action executed when the task runs, you can also have doFirst (runs before task actions)
    {
        println 'Welcome to Earth!' // Groovy print statement
    }
}
```
**Output**:
> gradle -q hello  (-q: quet mode, Suppresses: Gradle logs, Status messages and Build success text)
  Welcome to Earth!

**Execution Flow**
1. Gradle loads build.gradle
2. Registers task hello
3. You run gradle hello
4. Gradle executes the doLast block
5. Message is printed


### Incremental Builds And Caching
- Gradle only rebuilds what has changed, not everything. S0, it becomes much faster than rebuilding from scratch.
- Caching - Speeds up builds by reusing outputs from previous builds.

### Build Lifecycle
- Gradle’s lifecycle is task-based, not phase-based like Maven.
- Common lifecycle tasks:
clean  
compileJava  
test  
build  
publish  

### Multi-Project Builds
- Gradle excels at managing complex, modular codebases with multiple sub-projects, making it ideal for microservices architectures and large enterprise applications.
- Supports shared configurations and dependencies.

### Plugin Ecosystem
Gradle has a rich ecosystem of plugins (both official and third-party) that extend its functionality and provide integrations for various technologies (java, C++, etc) and tools, from Android development (where it is the official build tool) to Docker integration and code quality checks. 


# Common Gradle Commands

| Command             | Purpose                                        |
| ------------------- | -----------------------------------------------|
| gradle build        | Build project completely                       |
| gradle clean        | Remove old build files                         |
| gradle clean build  | Performs a clean build from scratch            |
| gradle test         | Run tests                                      |
| gradle assemble     | Build without tests                            |
| gradle run          | Run application (require apps plugins)         |
| gradle tasks        | List all available gradle tasks                |
| gradle check        | Runs all verification tasks                    |
| gradle dependencies | Show dependencies                              |
| gradle wrapper      | Creates Gradle Wrapper files                   |
| gradle init         | Sets up a Gradle project for you automatically |


# Maven vs Gradle

| Feature         | Maven                | Gradle                         |
|-----------------|----------------------|--------------------------------|
| Configuration   | XML                  | Groovy / Kotlin                |
| Speed           | Slower               | Faster (incremental builds)    |
| Flexibility     | Limited              | High                           |
| Learning Curve  | Easy                 | Moderate                       |
| Android Support | Limited              | Excellent                      |


