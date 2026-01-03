# Maven

Apache Maven is a build automation and dependency management tool, mainly used for Java-based projects. It helps developers build, test, package, and manage libraries in a standardized and automated way. Maven is declarative, we tell it what your project is (via the POM), and Maven knows how to build it using standard lifecycles.


## Key Concepts in Maven

### POM (Project Object Model)
- The pom.xml file is the heart of Maven. Maven reads the pom.xml file given by us to accomplish its configuration and operations.
- It contains everything Maven needs to know:
 - Identity: groupId (Company), artifactId (Project Name), version.
 - Dependencies: External libraries (log4j, junit).
 - Plugins: Tools to compile code, run tests, or create JARs.
- Example:
```XML
<groupId>com.example</groupId>
<artifactId>myapp</artifactId>
<version>1.0.0</version>
```

### Dependency Management
- Dependencies are defined in pom.xml, they are external Java libraries required for a Project, and repositories are directories of packaged JAR files.
- The local repository is just a directory on your machine's hard drive.
- If the dependencies are not found in the local Maven repository, Maven downloads them from a central Maven repository and puts them in your local repository.
- Handles transitive dependencies (dependencies of dependencies)

### Standard Project Structure
- Maven enforces a standard layout:
 ├── src/main/java - your application code
 ├── src/main/resources - config files (Properties, XML)
 ├── src/test/java - Unit tests
 ├── pom.xml
 └── target/ - Maven's output folder (where the compiled classes and JARs go)
- Easy to understand and structure is same across all projects

### Maven Build Lifecycle
- Maven works in phases, grouped into lifecycles.
- If a lifecycle is executed using a Maven command, all build phases in that lifecycle are also executed.

### Maven Repositories (Where the JARs live)
- Repositories store project dependencies and artifacts. Maven never stores libraries inside your project folder. It downloads them from the internet to a local cache.

![DevOps Tools Pipeline](../images/mavenrepo.webp)

1. **Local repository**: A local repository is a directory on the machine of developer, which has all the dependencies and Maven only needs to download them once, even if multiple projects depends on them (e.g. ODBC). By default, maven local repository is user_home/m2 directory.  
Example - C:\Users\user_home\.m2

2. **Central repository**: Maven looks in this central repository for any dependencies needed but not found in your local repository. Maven then downloads these dependencies into your local repository.  
Example: Maven downloading the JUnit library from repo.maven.apache.org.

3. **Remote repositoryv**: Remote repository is a repository on a web server from which Maven can download dependencies. It often used for hosting projects internal to the organization. Maven then downloads these dependencies into your local repository.  
Example: A company’s internal Nexus server at http://nexus.company.com/repository/maven-releases.

### Maven Plugins
- Plugins extend Maven’s functionality.
- We can add plugins to the pom.xml file. Maven offers standard plugins, and you can also implement custom plugins in Java.
- Examples: Compiler plugin, Surefire (testing), Jar / War plugin, Docker plugin


## Maven Lifecycle

- The Maven lifecycle is a sequence of well-defined phases that Maven follows to build, test, and package a project in a consistent and automated way.
- When you run a Maven command, Maven executes all lifecycle phases up to that point in order.
- Maven Has Three Built-in Lifecycles
 - Clean Lifecycle – Cleans previous build outputs
 - Default Lifecycle – Builds and packages the project
 - Site Lifecycle – Generates project documentation
- Maven Lifecycle flow: validate -> compile -> test -> package -> verify -> install -> deploy

1. Clean Lifecycle
- Remove old build files to ensure a fresh build.
- Phases:
 - pre-clean – Preparations before cleaning
 - clean – Deletes the target/ directory
 - post-clean – Tasks after cleaning
- Common Command: **mvn clean**

2. Default Lifecycle (Main Build Lifecycle)
- Compile, test, package, and deploy the application.
- Phases
 - validate: Checks if the project is correct and all necessary information is available.
 - compile: Compiles the source code (src/main/java) and Output goes to (target/classes).
 - test: Runs unit tests (src/test/java) using a suitable testing framework (JUnit, TestNG).
 - package: Takes the compiled code and packages it into a distributable format (.jar or .war).
 - verify: Runs integration tests to ensure quality criteria are met.
 - install: Installs the package into the Local Repository (.m2), for use as a dependency in other projects locally.
 - deploy: Copies the final package to the Remote Repository (Nexus/Artifactory) for sharing with other developers.
- Common Command: **mvn install**

3. Site Lifecycle
- Generate project documentation and reports.
- Phases:
 - pre-site
 - site – Generates documentation
 - post-site
 - site-deploy – Deploys documentation to a server
- Common Command: mvn site


## Transitive Dependency Management.
- Scenario: You need Spring Boot Web. You add one dependency to your POM.
- Reality: Spring Boot Web depends on Spring Core, which depends on Logging, which depends on Jackson.
- Maven's Job: It automatically discovers this entire tree and downloads all required JARs for you.


## Snapshot vs. Release
- Release (1.0.0): A stable, unchangeable version. Once released, it is frozen forever.
- Snapshot (1.0.0-SNAPSHOT): A development version. Maven checks for updates to Snapshots daily. This allows teams to share "work in progress" code without bumping version numbers constantly.


## Build Profiles
- Profiles allow you to change the build configuration based on the environment (e.g., Dev vs. Prod).
- Example: In "Dev", you might skip signing the JAR file to save time. In "Prod", signing is mandatory.
- You define profiles in the POM and activate them via the command line: **mvn package -P prod**.


## Common Commands

| Command                 | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `mvn clean`             | Deletes the `target` folder (cleans up old builds).                         |
| `mvn compile`           | Compiles source code only.                                                  |
| `mvn test`              | Compiles the code and runs unit tests.                                      |
| `mvn package`           | Creates the JAR/WAR file in the `target` directory.                         |
| `mvn install`           | Packages the project and copies the JAR to the local `~/.m2` repository.    |
| `mvn dependency:tree`   | Displays the full dependency tree (useful for debugging conflicts).         |
