# CI vs CD

| Aspect             | Continuous Integration | Continuous Delivery | Continuous Deployment |
|--------------------|------------------------|---------------------|-----------------------|
| Focus              | Code integration       | Release readiness   | Automatic releases    |
| Production deploy  | ❌ No                 | 🔘 Manual           | ✅ Automatic          |
| Automation level   | Build & test           | Build, test, stage  | End-to-end            |
| Human approval     | No                     | Yes                 | No                    |
| Risk               | Low                    | Medium              | Managed by automation |
| Release speed      | Fast feedback          | Controlled          | Very fast             |


# Continous Delivery

We have code in local machine and we wanted to build wep application. How we deploy our code to internet/server. So that it shows up in browser by navigating to any URL.

## Application/Web Server
- It is a software (like apache tomcat, etc) that we need to download from internet.
- This server is designed to run applications or to host the application.
- It can communicate and send request, responses over HTTP protocol. It has ability to connect with different nodes over internet.
- So when we place our code in these servers, then the application will be available over internet.

## Hosted Server
- These are physical machines where application/web/Databases servers are hosted.
- If we download apache Tomcat into our local machine, then our local machine is the hosted server for that application server which is Tomcat.
- To keep our Devops application running on server and access it from anywhere, we should first build the code so that the build files will be generated. The generated WAR file should be placed into Application/web server so that we can access it through internet using URL(IPadress/portnumber).
- Application server can start at any port in hosted server and can be accessed through  
HostedServerIpAddress: portnumber
- We can map that port number to any custom Domain name and access application server with that Domain name. We can buy the Domain Names from different websites like GoDaddy and can map IP address of our application to that name and access through internet by giving that name.
- Tomcat server will actually listen at port 8080 in our machine. Any machine can be uniquely identified by IP address.