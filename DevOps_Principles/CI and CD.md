# What is CI/CD?

- CI/CD stands for Continuous Integration and Continuous Delivery/Deployment. With CI/CD, we automate the integration of code changes from multiple developers into a single codebase.
- It is a software development practice where the developers commit their work frequently to the central code repository (GitHub or Stash).


# Continuous Integration 

It ensures that code changes made by developers are automatically built, tested, and integrated into the main codebase. It's goal is to Catch bugs early, reduce merge conflicts, and ensure code always works together.

- CI automatically pulls new code changes from developers
- Builds the application
- Runs automated tests (unit, integration)
- Reports errors instantly

## Example Flow

- Developer pushes code 
- CI pipeline starts
- Build + Test
- Feedback sent to developers

## This process typically involves four key stages:

1. **Source Code Management (SCM)**: Developers push their code from local machines to a remote repository such as GitHub. This allows teams to collaborate, review, and manage code versions easily.

2. **Build Process**: The source code is then compiled using tools like Maven, which packages the application into **artifacts** such as .jar, .war, or .ear files.  
**artifacts** are final products of your code before deployment. They are the packaged, compiled, or generated components that will be tested, stored, or deployed.

3. **Code Quality Check**: Tools like SonarQube analyze the code for bugs, code smells, and security issues. It generates detailed reports (HTML or PDF) to maintain code quality standards.

4. **Artifact Repository**: The generated build artifacts are stored in a repository manager like Nexus, which serves as a central storage for future deployment.

All these steps are automated using **Jenkins**, a popular CI tool that orchestrates the complete flow, from fetching code to storing the final build artifact.


# Continuous Deployment/ Continuous Delivery

## Continuous Deployment

It is the process of automatically deploying an application into the production environment when it has completed testing and the build stages. Here, we'll automate everything from obtaining the application's source code to deploying it.
 
- Every change after passes CI automatically goes to production
- No human approval needed
- Fully automated pipeline

## Continuous Delivery

It is the process of deploying an application into production servers manually when it has completed testing and the build stages. Here, we will automate the continuous integration processes, however, manual involvement is still required for deploying it to the production environment.

- Deploy automatically to staging/QA (Quality Assurance) environments
- Keep the application always ready for production

# CI/CD Automation Pipeline Stages

1. Commit Code
2. Pull Code + Build
3. Run Automated Tests
4. Security Scanning
5. Build Artifact (Docker image, JAR, etc.)
6. Deploy to Staging
7. Run Integration & Acceptance Tests
8. Deploy to Production (manual or automatic)
9. Monitor & Rollback if needed