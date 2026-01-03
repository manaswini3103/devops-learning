# How to debug when a build fails

1. Read the FIRST Real Error (Most Important)
- Do not start from the bottom blindly
- Look for: ERROR, FAILURE, Caused by, Could not resolve and Compilation failed
- The first meaningful error is usually the root cause.

2. Re-run with More Logs
- Maven
  - mvn clean install -e
  - mvn clean install -X   # full debug
- Gradle
  - gradlew build --stacktrace
  - gradlew build --info
  - gradlew build --debug
- npm: npm install --verbose

3. Identify which type of build failure is that
- Dependecy, Compilation, version conflicts etc

4. Compare With a Working Build (Very Useful)
- If project was converted (Maven → Gradle):
- Build with Maven: mvn clean install
- Compare with Gradle build output

5. Build in Steps (Isolation)
- Maven
  - mvn clean compile
  - mvn test
  - mvn package
- Gradle
  - gradlew compileJava
  - gradlew test
  - gradlew jar
- Find which step fails.

6. Common Quick Fixes

| Problem               | Quick Fix                  |
|-----------------------|----------------------------|
| Dependency not found  | Check repository & version |
| Java mismatch         | Align JDK version          |
| Tests failing         | Fix tests or skip          |
| Permission denied     | Run as administrator       |
| Proxy issue           | Update `settings.xml`      |


# Common Types of Build Failures

1. Dependency Download Failure
- Error examples: Could not resolve dependency, Could not transfer artifact, Connection timed out
- Causes: No internet, Proxy not configured, Wrong dependency version
- Fix
  - Check internet / VPN
  - Configure proxy (settings.xml), Use correct version
  - Maven: mvn -U clean install
  - Gradle: gradle build --refresh-dependencies

2. Version Conflict (Dependency Clash)
- Error: ClassNotFoundException, NoSuchMethodError
- Causes: Multiple versions of same library, Transitive dependency conflict
- Fix: Maven: mvn dependency:tree, Gradle: gradlew dependencies
- Exclude or force version

3. Compilation Errors
- Error: Compilation failed, cannot find symbol
- Causes: Syntax errors, Wrong Java version, Missing dependency
- Fix: Fix code errors, Align Java version, Check compiler plugin

4. Test Failures
- Error: Tests failed, BUILD FAILED
- Causes: Failing unit tests, Wrong test data, Environment mismatch
- Fix: Fix tests, Skip temporarily (not recommended):
  - mvn install -DskipTests
  - gradle build -x test

5. Java Version Mismatch
- Error: Unsupported major.minor version, invalid target release
- Causes: Project compiled with higher JDK, Lower JDK used to run build
- Fix: Match JDK versions, Configure compiler settings

6. Plugin Failure
- Error: Failed to execute goal, Plugin execution failed
- Causes: Incompatible plugin version, Misconfigured plugin
- Fix: Upgrade plugin, Check plugin config, Clear local cache

7. Missing Environment Variables
- Error: JAVA_HOME not set, NODE_ENV not defined
- Causes: Env variables not configured
- Fix: Set environment variables properly

8. Permission Issues
- Error: Permission denied, Access is denied
- Causes: No write permission, Running as wrong user
- Fix: Change permissions, Run terminal as admin, Fix directory ownership

9. Corrupted Cache
- Error: Checksum failed, Invalid LOC header
- Causes: Corrupted local repository/cache
- Fix: Maven: rm -rf ~/.m2/repository, gradle: rm -rf ~/.gradle/caches and npm: npm cache clean --force

10. Wrong Build Command
- Error: Task not found, Unknown lifecycle phase
- Causes: Typo in command, Running wrong tool
- Fix: Verify command, Check available tasks