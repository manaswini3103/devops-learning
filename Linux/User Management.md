# User Management

## User roles and sudo
- Linux is a multi-user environment
**su** : we can switch between users (set user, switch user or substitute user).
to switch the user we must know that user password.
- User Roles:
**Normal user**: modify their own files, cannot make system changes
**Super user**: modify any file, make system changes
- **sudo**: do something as a superuser temporarily.
 - We need to know our password to login. Only, works if you are allowed in /etc/sudoers.
 - And after we are done it’s good to use ‘sudo -k’ to give up those privileges.
 - You stay yourself just the command runs as root.
- **sudo su**: Become root using your own password
 - First, sudo runs as root (using your password).
 - Then it executes su, which switches to root.
 - We become root, but don’t load roots full environment.
- **sudo su -**: Become root and load root’s full environment.
 - The dash (-) means login shell, like root logged in directly.
 - Loads root’s PATH
 - Loads root’s HOME (/root)
 - Loads root’s login files (.profile, .bashrc, etc.)
 - Behaves exactly like logging in as root

## Types of users
In linux there are 5 types of users
1. Super or root user: this user is most powerful user/administratoruser
2. System user: user created by softwares/ application
3. Normal user: normal users are users created by root user
4. Sudo User: normal user with temporary admin rights via sudo command.
5. Guest User: Temporary users with minimal privileges. Changes are not saved after logout.

## User Groups
1. Primary Groups (Default for files)
2. Secondary Group (Additional Permissions) – commonly used for team-based or system -level permissions (ex: accessing Docker, video devices, etc)

## User Creation
- home directory is created(/home/username)
- unique UID & GID are given to user
- An entry in /etc/passwd and /etc/group, all user info is stored in cat /etc/passwd
- for privilege control /etc/sudoers
- **syn**: useradd <option> <username>

## options for modifying user
u to change user id, -aG secondary group id (we use this during docker setup, we should add user to a docker group), -g to change primary group id, -d to change home directory, -c comment, -s shell
[root@omega home]# useradd john
[root@omega home]# useradd mark
[root@omega home]# id john  (to get user id, group id)
[root@omega home]# usermod -aG john mark (adds mark to the john group)
[root@omega home]# id mark
[root@omega home]# passwd john
[root@omega home]# cat /etc/passwd
[root@omega home]# usermod -u new_id username
[root@omega home]# userdel -r username (-r deletes the users home directory)

## Common issues in User Management:
1. Forgotten password: sudo passwd username
2. Account lockouts: multiple failed login attempts 
sudo usermod -U username (-U unlocks the specified user)
3. Security Vulnerability: outdated systems can be suspected to security threats.
sudo apt update && sudo apt upgrade. 
4. When we tried to login to that user it’ll ask for key instead of password. So, we’ll make some changes to ask for password in default configuration.
[root@omega home]# nano /etc/ssh/sshd_config (or) vi /etc/ssh/sshd_config
a file will be opened in editor mode, there we need to check for text “PasswordAuthentication no”.
5. We need to change that to “PasswordAuthentication yes”
When we update configurations, we need to update our services
[root@omega home]# service sshd reload
6. Then we’ll login with the new user which we created, by taking the IP from EC2 instance we created and give in new session.
