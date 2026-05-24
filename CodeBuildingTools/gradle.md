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
- Gradle only rebuilds what has changed, not everything. So, it becomes much faster than rebuilding from scratch.
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
| gradle -v           | gives the gradle version                       |
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
|.\gradlew clean build| ./ runs in windows power shell                 |

- gradlew -v : checks if gradle is installed required by the project. If not present, it automatically downloads that Gradle version. Gradle is downloaded per project, not installed system-wide. The downloaded Gradle lives in: `~/.gradle/wrapper/dists/`


# Maven vs Gradle

| Feature         | Maven                | Gradle                         |
|-----------------|----------------------|--------------------------------|
| Configuration   | XML                  | Groovy / Kotlin                |
| Speed           | Slower               | Faster (incremental builds)    |
| Flexibility     | Limited              | High                           |
| Learning Curve  | Easy                 | Moderate                       |
| Android Support | Limited              | Excellent                      |


## build.gradle structure

1. Plugins
- Defines which Gradle plugins your project uses.
- Modern Gradle prefers plugins {} over apply plugin:.
```groovy
plugins {
    id 'java'
    id 'application'
    id 'org.springframework.boot' version '3.2.1'
}
```

2. Project Metadata
- Basic information about your project.  
group = 'com.example'  
version = '1.0.0'  
description = 'Demo project'  

3. Java / Toolchain Configuration (Optional but Recommended)
```groovy
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}
```

4. Repositories
- Where Gradle downloads dependencies from.
```groovy
repositories {
    mavenCentral()
}
```
- Other examples:
```groovy
mavenLocal()
maven { url 'https://repo.spring.io/milestone' }
```

5. Dependencies
- Libraries your project depends on.
- Common configurations: implementation, api, compileOnly, runtimeOnly and testImplementation.
```groovy
dependencies {
    implementation 'org.apache.commons:commons-lang3:3.14.0'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.1'
}
```

6. Application Configuration (if using application plugin)
```groovy
application {
mainClass = 'com.example.Main'
}
```

7. Tasks Configuration
- Customizing existing tasks or defining new ones.
- Configure existing task
```groovy
tasks.test {
    useJUnitPlatform()
}
```
- Custom task
```groovy
tasks.register('hello') {
    doLast {
        println 'Hello, Gradle!'
    }
}
```

8. Source Sets (Optional)
- Change default project layout.
```groovy
sourceSets {
    main {
        java.srcDirs = ['src']
    }
}
```

9. Configurations (Advanced)
- Define custom dependency buckets.
```groovy
configurations {
    integrationTestImplementation.extendsFrom testImplementation
}
```

10. Extra Properties (ext)
- Shared constants.
```groovy
ext {
    lombokVersion = '1.18.30'
}
```
- Usage: implementation "org.projectlombok:lombok:$lombokVersion"

### Example (Java Project)
```groovy
plugins {
    id 'java'
}
group = 'com.example'
version = '1.0.0'
repositories {
    mavenCentral()
}
dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.1'
}
tasks.test {
    useJUnitPlatform()
}
```

## Multi-Module Structure (Quick View)
- settings.gradle
```groovy
rootProject.name = 'my-project'
include 'core', 'api'
```
- Each module:
```groovy
core/build.gradle
api/build.gradle
```

## how to change maven project to gradle and build it successfully by copying it from some public repos

1. Clone a Public Maven Project
- git clone https://github.com/spring-projects/spring-petclinic.git
- cd spring-petclinic
- Verify it is Maven-based: pom.xml
- Optional sanity check: mvn clean install

2. Install Gradle (or use Wrapper)
- Check the installed gradle version: gradle -v
- If not installed download from gradle.org or use package manager

3. Convert Maven → Gradle Automatically
- Run this from the project root: gradle init
- Choose these options:
  - Build system → Gradle
  - Use existing build → Maven
  - DSL → Groovy (recommended for beginners)
  - Test framework → JUnit
- Gradle will:
  - Read pom.xml
  - Generate build.gradle
  - Create settings.gradle
  - Add Gradle Wrapper (gradlew)
- New Files Created
  - build.gradle
  - settings.gradle
  - gradlew
  - gradlew.bat
  - gradle/

4. Verify Generated build.gradle
- Check: group, version, repositories, dependencies, Java version
- Example:
```groovy
plugins {
    id 'java'
}
group = 'org.springframework.samples'
version = '3.1.0'
repositories {
    mavenCentral()
}
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```

5. Fix Common Conversion Issues (Very Important)
   1. Java Version Mismatch
    If Maven used Java 17, add:
    ```groovy
    java {
      toolchain {
        languageVersion = JavaLanguageVersion.of(17)
      }
    }
    ```
   2. Dependency Management (Spring Boot)
    - Maven: `<dependencyManagement>...</dependencyManagement>`
    - Gradle equivalent:
    ```groovy
    plugins {
        id 'org.springframework.boot' version '3.1.0'
        id 'io.spring.dependency-management' version '1.1.3'
    }
    ```
   3. Maven Scope Mapping Fix
    - Maven	Gradle
    - compile	implementation
    - provided	compileOnly
    - test	testImplementation
   4. Multi-Module Project
    - Check settings.gradle:
    - rootProject.name = 'project-name'
    - include 'module-a', 'module-b'

6. Build Using Gradle Wrapper (Best Practice)
- ./gradlew clean build
- Uses correct Gradle version and avoids environment issues.

7. Fix Build Failures (Common & Fast Fixes)
 - Dependency Issues: ./gradlew build --refresh-dependencies
 - Tests Failing (Temporary): ./gradlew build -x test
 - Corrupted Cache: rm -rf ~/.gradle/caches

8. Remove Maven Files (After Success)
Only after Gradle build passes: pom.xml, .mvn/


In Terminal:

PS C:\Users\chennasa\OneDrive - CDK Global LLC\Documents\GIT\onlinebookstore> gradle init Starting a Gradle Daemon (subsequent builds will be faster) Found a Maven build. Generate a Gradle build from this? (default: yes) [yes, no]yes

Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no]no