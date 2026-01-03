# Change Dependency Version in Maven (pom.xml)
```XML
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>3.2.1</version>   <!-- change version here -->
</dependency>
```  
After changing run **mvn clean install**


## Using Properties (Best Practice)
Easier to update and used in real projects.  
```XML
<properties>
    <spring.boot.version>3.2.1</spring.boot.version>
</properties>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>${spring.boot.version}</version>
</dependency>
```


# Change Dependency Version in Gradle (build.gradle)
```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web:3.2.1'
}
```

## Using Variables
```groovy
ext {
    springBootVersion = '3.2.1'
}
dependencies {
    implementation "org.springframework.boot:spring-boot-starter-web:$springBootVersion"
}
```  
after changing Run **gradle build**


# Change Dependency Version in npm (package.json)
```JSON
"dependencies": {
  "express": "^4.19.0"
}
```  
After changing run **npm install**


# If Version Is Managed
Maven (Dependency Management)  
```XML
<dependencyManagement>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-dependencies</artifactId>
        <version>3.2.1</version>
        <type>pom</type>
        <scope>import</scope>
    </dependency>
</dependencyManagement>
```  
Change version here, not in individual dependencies.


# Clear Cache (If Version Doesn’t Update)
- Maven: mvn clean install -U
- Gradle: gradle build --refresh-dependencies
- npm: npm cache clean --force, npm install

