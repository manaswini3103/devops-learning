# Build Artifact
A build artifact is an output produced by the build process. Artifacts are what you run, deploy, or publish.  
Examples:  
Logs  

## Common build artifacts (Java)
1. Compiled classes
- build/classes/java/main/ or target/classes/
- Contains: .class files (compiled Java bytecode)

2. JAR (Java Archive) files
- build/libs/myapp-1.0.0.jar
- Runnable or library archive
- Contains compiled classes + resources
- Types:
  - Plain JAR – library
  - Fat/Uber JAR – includes dependencies
  - Executable JAR – has Main-Class

3. WAR files (Web apps)
- build/libs/myapp.war
- Used for servlet containers (Tomcat, Jetty)
- Contains: /WEB-INF/classes and /WEB-INF/lib/*.jar

4. Test reports
- build/reports/tests/test/index.html
- Contains: Test results, Passed/failed test details and Coverage reports (JaCoCo)

5. Generated sources
- build/generated/sources/
- Created by: Annotation processors (Lombok, MapStruct), OpenAPI / Swagger generators and Protobuf

6. Dependency cache (not project-specific)
- ~/.gradle/caches/
- ~/.m2/repository/
- Stores: Downloaded libraries and Plugin dependencies
- Never commit these to Git.

## Build lifecycle artifacts

1. Gradle

| Phase        | Artifacts        |
|--------------|------------------|
| compileJava  | `.class` files   |
| test         | Test reports     |
| jar          | `.jar` file      |
| build        | All outputs      |

2. Maven

| Phase   | Artifacts              |
|---------|------------------------|
| compile | `.class` files         |
| test    | Surefire reports       |
| package | `.jar` / `.war`        |
| install | Local repository artifact |


# Typical Java project directory structure

📁 Standard layout (Gradle & Maven)

project-root/
├── build.gradle / pom.xml  
├── settings.gradle  
├── gradlew / gradlew.bat  
├── gradle/  
│   └── wrapper/  
│  
├── src/  
│   ├── main/  
│   │   ├── java/        ← Application source code  
│   │   ├── resources/   ← Config files (application.yml, properties)  
│   │   └── webapp/      ← Web apps (JSP, HTML, CSS)  
│   │
│   └── test/  
│       ├── java/        ← Test source code  
│       └── resources/   ← Test configs  
│
├── build/ or target/    ← Generated build artifacts  
└── README.md  

Tool	Build directory  
Gradle	build/  
Maven	target/
