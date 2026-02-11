# Spring Boot Dockerfile (BEST PRACTICE)
Multi-stage, small, fast, production-ready

```Dockerfile
# ---------- Build stage ----------
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /build
COPY mvnw pom.xml ./
COPY .mvn .mvn
RUN ./mvnw -B -q dependency:go-offline

COPY src src
RUN ./mvnw -B package -DskipTests

# ---------- Runtime stage ----------
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /build/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
```

## Why this is good
- Small final image
- No Maven in runtime
- Cached dependencies
- Reproducible builds

# Node.js Dockerfile (BEST PRACTICE)

```Dockerfile
# ---------- Build ----------
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# ---------- Runtime ----------
FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

## For simple apps (no build step)
```Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["npm","start"]
```

# Python Dockerfile (BEST PRACTICE)
```Dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["python","app.py"]
```

## For FastAPI / Uvicorn
```Dockerfile
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
```

# .NET Dockerfile (BEST PRACTICE)
```Dockerfile
# ---------- Build ----------
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY *.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /app/publish

# ---------- Runtime ----------
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish .
EXPOSE 8080
ENTRYPOINT ["dotnet","MyApp.dll"]
```

# Dockerfile BEST PRACTICES (USE THESE ALWAYS)

1. Use multi-stage builds
- Smaller images and No build tools in runtime

2. Use slim/alpine images
- alpine, slim, distroless

3. Copy dependency files first
- COPY package.json .
- RUN npm install
- enables Docker layer caching

4. Use .dockerignore
```Dockerfile
.git
node_modules
target
*.log
```

5. Use non-root user (advanced)
```Dockerfile
RUN addgroup app && adduser -S app -G app
USER app
```

## Don’t do this

- FROM ubuntu + install everything
- latest tag in production
- ADD instead of COPY
- Huge images

# Common Dockerfile Errors & Fixes
1. Error: COPY failed: no such file or directory  
Cause: Wrong path, File not in build context, .dockerignore excludes it  
Fix   
```bash
docker build .
ls -R
```
2. Error: exec format error  
Cause: Wrong architecture (ARM vs AMD)  
Fix  
```Dockerfile
FROM --platform=linux/amd64 node:20-alpine
```

3. Error: App works locally, fails in Docker  
Cause: Binding to localhost, Missing env vars  
Fix in bash `--host 0.0.0.0`

4. Error: Image too big  
Cause: Build tools inside runtime  
Fix: Multi-stage build

5. Error: Docker build is slow  
Cause: Poor layer caching  
Fix: Copy dependency files first and use '.dockerignore'

# How to debug Dockerfile failures
- Run interactive shell: docker run -it image sh
- Print files: RUN ls -la
- Build without cache: docker build --no-cache .