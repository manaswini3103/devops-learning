# settings.xml

settings.xml is a global / user-specific configuration file in Maven. It controls how Maven behaves, not how a specific project is built (that’s what pom.xml is for). Contains credentials, repositories, proxies, profiles. Not committed to source control (contains secrets). This Applies to all Maven projects on your machine.

settings.xml is used to configure Maven environment-level settings like credentials, repositories, proxies, and profiles. It is machine-specific and should never be committed to source control.

## Location of settings.xml
1. User-specific (most common)
- ~/.m2/settings.xml
- Linux / macOS: /home/user/.m2/settings.xml
- Windows: C:\Users\username\.m2\settings.xml

2. Global (rarely used)
- MAVEN_HOME/conf/settings.xml
- User settings override global settings

| Feature            | settings.xml           | pom.xml              |
|--------------------|------------------------|----------------------|
| Purpose            | Environment config     | Project config       |
| Scope              | Machine-specific       | Project-specific     |
| Contains           | Credentials            | Dependencies         |
| Includes           | Proxies, mirrors       | Build plugins        |
| Shared in VCS      | Not shared             | Shared               |


## Structure of Settings.xml

```XML
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0">
    
    <localRepository>/path/to/local/repo</localRepository>

    <servers>
        <server>
            <id>nexus</id>
            <username>admin</username>
            <password>admin123</password>
        </server>
    </servers>

    <mirrors>
        <mirror>
            <id>central-mirror</id>
            <mirrorOf>central</mirrorOf>
            <url>https://repo.maven.apache.org/maven2</url>
        </mirror>
    </mirrors>

    <profiles>
        <profile>
            <id>dev</id>
            <properties>
                <env>development</env>
            </properties>
        </profile>
    </profiles>

    <activeProfiles>
        <activeProfile>dev</activeProfile>
    </activeProfiles>

</settings>
```

## Important Sections Explained

### <localRepository>
- Changes default local repo location.  
``<localRepository>D:/maven-repo</localRepository>`
- Default: ~/.m2/repository

### <servers> (Credentials 🔐)
- Used for: Nexus / Artifactory, Private repositories and Deployment credentials.  
```XML
<servers>
    <server>
        <id>nexus</id>
        <username>deployUser</username>
        <password>deployPass</password>
    </server>
</servers>
```
- The <id> must match the repository ID in pom.xml.

### <mirrors> (Repository Redirection)
- Redirects all repository requests to a mirror (commonly Nexus). It imporoves performance and used in corporate environments.  
```XML
<mirrors>
    <mirror>
        <id>nexus</id>
        <mirrorOf>*</mirrorOf>
        <url>http://localhost:8081/repository/maven-public/</url>
    </mirror>
</mirrors>
```

### <proxies> (Corporate Network)
Used when internet access is via proxy (Maven needs to go through a proxy server to access the internet instead of connecting directly).  
```XML
<proxies>
    <proxy>
        <id>corp-proxy</id>
        <active>true</active>
        <protocol>http</protocol>
        <host>proxy.company.com</host>
        <port>8080</port>
        <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
</proxies>
```

### <profiles> (Environment Configuration)
- Used to define environment-specific values.
- can be activated using command **mvn clean install -Pprod** Or auto-activate in settings.xml.  
```XML
<profiles>
    <profile>
        <id>prod</id>
        <properties>
            <db.url>jdbc:mysql://prod-db</db.url>
        </properties>
    </profile>
</profiles>
```

### <activeProfiles>
Profiles enabled by default.  
```XML
<activeProfiles>
    <activeProfile>prod</activeProfile>
</activeProfiles>
```