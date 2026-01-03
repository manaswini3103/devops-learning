# NPM

- NPM (Node Package Manager) is the default package manager and build tool for Node.js.
- It provides a lightweight way of installing, upgrading, configuring, and removing third-party libraries or modules that might be used in an application.
- It is more than a package manager; it is a repository that allows developers to publish their packages and share code with others.
- Its powerful command line allows npm to simplify the development process through automation across different environments.
- It helps you download libraries, manage dependencies, and run scripts for JavaScript projects.


## Why npm Is Used

JavaScript projects often depend on many external libraries. Managing them manually would be difficult and error-prone.

- Automatically installing libraries
- Managing dependency versions
- Providing a standard project structure
- Supporting build and automation tasks


## Key Components of npm

### package.json
It is considered as an important file in any npm project. It includes information about the project like name, version, description, author, license, and most importantly, the dependencies used by the project. Package.json also supports scripts that can be executed via npm.
Example:  
```JSON
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "Sample Node.js application",
  "main": "index.js",
  "scripts": {"start": "node app.js",
  "build": "webpack",
  "test": "jest"},
  "dependencies": {"express": "^4.18.2"},
  "devDependencies": {"jest": "^29.0.0"},
  "engines": {"node": ">=18.0.0"},
  "repository": {"type": "git",
  "url": "https://github.com/user/repo.git"},
  "author": "John Doe",
  "license": "MIT",
  "private": true
}
```
- main: Entry point of the application, file that runs when the package is imported.
- "express": "^4.18.2" - express is web framework for Nodr.js, ^ - Allows minor and patch updates (like: 4.18.9 or 4.19.0 but not 5.0.0). Included in production builds.
- "jest": "^29.0.0" - jest is a testing framework, not required when app is running in production.
- engines: Specifies required Node.js / npm versions.
- repository: source code location
- private: Prevents accidental publishing

### package-lock.json file
It was introduced in npm version 5 and serves as an exact snapshot of the whole dependency tree that a project uses. It guarantees identical versions of dependencies installed across all different environments by reducing the likelihood of version conflicts.

### npm CLI
This is the most important command line interface that developers use to interact with npm. It is used to run commands that normally would entail packages' install, dependency management, scripts running, and package publishing.

### Dependencies
- Dependencies are external libraries your project needs. NPM installs them automatically.
- Types:
 - dependencies → required in production
 - devDependencies → Libraries needed only during development (tests, build tools)

### NPM Registry
Central online repository of JavaScript packages, Default source for npm packages and Millions of open-source libraries are available.

### node_modules Folder
Stores all installed packages and managed automatically by npm, Should not be edited manually.

### npm Scripts
- NPM can run custom commands defined in package.json that can be run from the terminal.
- These scripts automate common tasks such as running tests, building your project, or deploying your code.
- They run inside the script section.
- Example:
```JSON
"scripts": {
  "start": "node app.js",
  "build": "webpack",
  "test": "jest"
}
```
"start": "node app.js" - Runs application using Node.js, executes file app.js, Commonly used to start a server or application.  
"build": "webpack" - Runs Webpack, a module bundler (Bundle JavaScript files and Optimize assets for production).  
"test": "jest" - Runs Jest, a JavaScript testing framework, executes test files to verify code correctness.
- Run using: **npm run build**
- Runs build tools (Webpack, Babel)


## Basic npm Commands
- npm init: Initializes a new Node.js project and creates a package.json file.
- npm init -y: If we want to bypass the interactive mode (package.json) and use defaults
- npm install [package]: Installs a package and its dependencies.
- npm update: Updates the installed packages to their latest versions.
- npm uninstall: Remove a package from the project.
- npm run: Execute a script defined in the package.json file.
- npm publish: Publish a package to the npm registry.
- npm search express: will list packages related to the name "express"
- npm cache clean --force: clears npm’s local cache forcefully, usually used to fix corrupted cache or dependency-related issues.


## npm install, build, and run

### npm install
- npm install downloads and installs all project dependencies defined in package.json.
- What happens internally:
  - Reads package.json
  - Checks package-lock.json (exact versions)
  - Downloads required packages from npm registry
  - Stores them in the **node_modules/** folder
  - Project ready to build or run
- Commands:  
  - npm install
  - npm install express (Installs a specific package called express)
  - npm install --production (Installs only production dependencies)

### npm build
- There is no default npm build command. npm build works only if a build script is defined in package.json.
- Example package.json  
```JSON
"scripts": {
  "build": "webpack"
}
```
- Command: **npm run build**
- The build step:
  - Compiles source code and Bundles files
  - Prepares code for production
  - finally we'll have Optimized production files
  - they will be in dist/ or build/ folder
- Typical build tools used: Webpack, Vite, Babel and React / Angular / Vue build tools 

### npm run
- npm run executes scripts defined in package.json.
- Example package.json  
```JSON
"scripts": {
  "start": "node app.js",
  "build": "webpack",
  "test": "jest"
}
```
- Common commands: npm run start, npm run build and npm run test
- In some Special case we can run these without run as they are built-in script names (npm start and npm test).


## Simple Flow (Real-World)
npm install → npm run build → npm start
- Install libraries
- Build application
- Run application