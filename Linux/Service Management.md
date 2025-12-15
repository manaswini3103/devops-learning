# Services
**service** - this controls the starting and stopping of services/applications. If we install any application and if we want to start or stop the application, service is used.  
**chkconfig** - this controls which services are set to start on boot. If we want to start out services while starting our system itself.

- We can give systemctl or service we’ll get the same result.
#systemctl status http  
#service `<name of the service>` status  : to check status of the service  
#service `<name of the service>` start   : to start the service  
#service `<name of the service>` stop    : to stop the service  
#service `<name of the service>` reload  : to reload the service, reread the configuration of the service. Each service has at least one configuration.  
#service `<name of the service>` restart : to restart the service, stops the existing connections.  

#chkconfig –list            : to check availability of the service  
#chkconfig `<service>` on   : to make the service available after restart  
#chkconfig `<service>` off  : to make the service unavailable after restart  
- If we want to check service for http, first we can install it  
yum install httpd -y
service httpd status (if it’s inactive we can start the service)  
service httpd start
- We can access this http service (that we have installed and started) on the browser by giving the Public IP of the EC2 instance (IP:80). Then a default page will appear.
- Before that we need to go to security group in AWS EC2 instance, go to the ‘inbound rules’ tab and edit it by adding the HTTP and the internet IP and save the rules. which means at networking level we are allowing port number 80 to access from the browser.
- Previously we got the default page for http service in browser, because we don’t have anything in path /var/www/html. Instead of default page if we want something else then we can create an ‘index.html’ file in /var/www/html this path.
```HTML
[root@omega html]# vi index.html
<h1> Hello, welcome to Linuc classes </h1>
```
- Then we need to reload the service  
[root@omega html]# service httpd reload  
or we can restart the system and start the service  
[root@omega html]# init 6 (or) reboot  
then R to restart the session and start the service so that others can access it  
[root@omega html]# service httpd start  
- When we want to start the service by default whenever we are restarting/booting the system then we can use “chkconfig”.  
[root@omega html]# chkconfig httpd on  
[root@omega html]# reboot  
now we don’t to start the service, we can directly access it in the browser.  
