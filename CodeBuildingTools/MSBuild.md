# Build configuration in Visual Studio projects

## Build Configuration
- A build configuration defines how your code is compiled and built.
- It controls things like:
  - Debug symbols
  - Compiler optimizations
  - Output paths
  - Conditional compilation flags
- Same code, different configuration → different build output.


## Common build configurations
Visual Studio projects usually have these by default:

|Configuration | Purpose                     |
| -------------| ----------------------------|
|Debug	       | For development & debugging |
|Release	     | For production deployment   |

1. Debug configuration
- Used while developing.
- Characteristics: Debug symbols (.pdb), Full variable names & stack traces and Easier debugging.
- output: bin/Debug/

2. Release configuration
- Used when shipping the app.
- Characteristics: Compiler optimizations enabled, Smaller & faster binaries and Production-ready.
- output: bin/Release/


## Build Configuration vs Platform
- Visual Studio separates Configuration and Platform:

| Setting	  | Examples           |
| ------------| -------------------|
|Configuration|	Debug, Release     |
|Platform	  | Any CPU, x86, x64  |

- Example:  Debug | Any CPU and Release | x64  
- Debug build targeting Any CPU
- Release build targeting 64-bit systems


## Build outputs (artifacts)
Depending on project type:cc  
C# / .NETcc  
bin/  
 ├── Debug/  
 │   └── net8.0/  
 │       ├── MyApp.dll  
 │       ├── MyApp.pdb  
 │  
 └── Release/  
     └── net8.0/  
         ├── MyApp.dll  
         └── MyApp.exe  

C++ projects
- Debug/
- Release/
- x64/Debug/
- x64/Release/


## Best practices
- Use Debug for development
- Use Release for deployment
- Don’t debug production builds
- Keep output paths clean
- Commit configuration files, not binaries