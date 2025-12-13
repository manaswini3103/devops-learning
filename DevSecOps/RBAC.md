# Role-Based Access Control (RBAC)

This is a security model that controls who can do what in a system by assigning permissions to roles, and then assigning users or services to those roles.

Instead of giving permissions directly to individuals, RBAC uses roles as an abstraction layer.


## Core Concepts of RBAC
1. Users / Identities
- People, applications, or services
- Example: Alice, CI pipeline, Kubernetes pod

2. Roles
- Named sets of permissions
- Example: Admin, Developer, ReadOnly and DB-Operator

3. Permissions
- Allowed actions
- Examples: read secrets, deploy applications, delete resources and view logs

4. Assignments
- Users are assigned to roles
- Roles define what actions are allowed

## How RBAC Works (Step-by-Step)

- A user or service authenticates (proves identity)
- The system checks which role is assigned
- The role determines what actions are allowed
- Access is granted or denied accordingly

## Example

| User        | Role      | Allowed Actions                 |
|-------------|-----------|---------------------------------|
| Alice       | Developer | Deploy app, read logs           |
| Bob         | Admin     | Create users, delete resources  |
| CI Pipeline | BuildRole | Build & deploy only             |
| Auditor     | ReadOnly  | View reports                    |

## Why RBAC Is Important
1. Enforces Least Privilege  
Users only get the permissions they need—nothing more.

2. Improves Security  
Limits damage if an account is compromised.

3. Simplifies Management  
Change a role once instead of updating permissions for many users.

4. Supports Compliance  
Required by standards like:
- ISO 27001
- SOC 2
- PCI DSS
- HIPAA