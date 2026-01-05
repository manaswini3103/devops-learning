Building a JAR or WAR file in Maven involves configuring the packaging type in your project's pom.xml file. The core Maven build process, primarily managed by the Apache Maven Compiler Plugin and Apache Maven JAR Plugin or Apache Maven WAR Plugin, handles the actual assembly of these artifacts during the package phase [1, 2]. 

# Building a JAR File

A JAR (Java Archive) file is typically used for general Java applications, libraries, or command-line tools. 

## Configure the pom.xml:
Set the `<packaging>` element to jar in your pom.xml. If the packaging type is not specified, it defaults to jar.
```xml
<project>
    ...
    <groupId>com.example</groupId>
    <artifactId>my-jar-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>jar</packaging> <!-- This is the default, so it can be omitted -->
    ...
</project>
```

## Build the Project:
- Open a terminal or command prompt, navigate to your project's root directory (where the pom.xml is located), and run  
```bash
mvn package
```
- This command compiles your source code, runs tests, and creates the JAR file in the target/ directory.

## For Executable JARs:
If you want to build an executable JAR (one that can be run with java -jar filename.jar), you need to configure the Apache Maven Shade Plugin or the Apache Maven Assembly Plugin to include dependencies and specify the main class.


# Building a WAR File

A WAR (Web Application Archive) file is specifically designed for deploying web applications to a servlet container or application server (like Apache Tomcat or Jetty).

# Configure the pom.xml
Set the <packaging> element to war in your pom.xml.
```xml
<project>
    ...
    <groupId>com.example</groupId>
    <artifactId>my-web-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>war</packaging>
    ...
</project>
```

## Ensure Standard Web Structure
Maven assumes a standard directory structure for web projects, with web resources (like HTML, CSS, JSPs, and WEB-INF) located in src/main/webapp.  
src/main/java  
src/main/resources  
src/main/webapp  
    └── WEB-INF  
        └── web.xml  

## Build the Project:
- In your project's root directory, run the command  
```bash
mvn package
```
- This command compiles code, copies resources, assembles the web application structure, and places the resulting WAR file in the target/ directory.
- The assembly process is handled by the Apache Maven WAR Plugin.


| Feature              | JAR                     | WAR                     |
|----------------------|-------------------------|-------------------------|
| Usage                | Standalone applications | Web applications        |
| Server needed        | No                      | Yes (Tomcat, etc.)      |
| Packaging            | `.jar`                  | `.war`                  |
| Spring Boot default  | Yes                     | No                      |
