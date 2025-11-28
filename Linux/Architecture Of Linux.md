# Linux Architecture

Linux architecture is a layered structure consisting of hardware, the kernel, system libraries, the shell, and applications.

---

## 1. Hardware
The physical components of the computer, such as the CPU, RAM, hard drive, and peripherals.  
It is the foundation upon which the rest of the system is built.

---

## 2. Kernel
The core of the operating system that manages system resources and acts as the interface between hardware and software.  
It handles low-level tasks like:

- Process scheduling  
- Memory management  
- Device drivers  

### **Types of Kernels**
- **Monolithic Kernel**  
- **Hybrid Kernels**  
- **Exokernels**  
- **Microkernels**

---

## 3. Shell
A command-line interpreter that acts as a user interface to the kernel.  
It takes commands from the user and passes them to the kernel for execution.

**Examples:** Bash, Zsh

---

## 4. Application
User-level programs such as desktop environments, word processors, browsers, and other software that run in user space.

---

## 5. System Libraries
Libraries (like the GNU C Library) provide a convenient interface for applications to access kernel functions.  
They translate user commands and application requests into system calls that the kernel understands.

---

## 6. System Utilities
System utilities are essential tools provided by Linux to manage and configure the system.  
These utilities help with tasks such as:

- Installing software  
- Configuring networks  
- Monitoring performance  
- Managing users and permissions  

They simplify system administration and help maintain the system efficiently.
