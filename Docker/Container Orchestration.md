# Container Orchestration

We will now try to understand what container orchestration is.

So far in this course we have seen that with Docker you can run a single instance of the application

with a simple Docker run command.

In this case to run a node js based application you're on the docker run node js command.

But that's just one instance of your application on one docker host.

What happens when the number of users increase and that instance is no longer able to handle the load

you deploy additional instance of your application by running the docker run command multiple times.

So that's something you have to do yourself.

You have to keep a close watch on the load and performance of your application and deploy additional

instances yourself and not just that you have to keep a close watch on the help of these applications.

And if a container was to fail you should be able to detect that and run the docker run command again

to deploy another instance of that application.

What about the health of the docker host itself.

What if the host crashes and is inaccessible.

The containers hosted on that host become inaccessible too.

So what do you do in order to solve these issues.

You will need a dedicated engineer who can sit and monitor the state performance and health of the containers

and take necessary actions to remediate the situation.

But when you have large applications deployed with tens of thousands of containers that's that's not

a practical approach.

So you can build your own scripts and that will help you tackle these issues to some extent.

Container orchestration is just a solution for that.

It is a solution that consists of a set of tools and scripts that can help host containers in a production

environment.

Typically a container orchestration solution consist of multiple Docker hosts that can host containers

that way even if one fails.

The application is still accessible through the others a container orchestration solution easily allows

you to deploy hundreds or thousands of instances of your application with a single command.

This is a command used for Docker swarm.

We will look at the command itself in a bit some orchestration solutions can help you automatically

scale up the number of instances when users increase and scale down the number of instances when the

demand decreases.

Some solutions can even help you in automatically adding additional hosts to support the user load and

not just clustering and scaling the container orchestration solutions.

Also provide support for advanced networking between these containers across different hosts as well

as load balancing user requests across different house.

They also provide support for sharing storage between the host as well as support for configuration

management and security within the cluster.

There are multiple container orchestration solutions available today Docker has Docker swarm coordinators

from Google and MESOS from Apache while Docker swarm is really easy to setup and get started.

It lacks some of the Advanced Auto scaling features required for complex production great applications

mesos on the other hand it's quite difficult to setup and get started but supports many advanced features

kubernetes arguably the most popular of it all is a bit difficult to setup and get started but provides

a lot of options to customize deployments and has support for many different vendors credit that is

now supported on all public cloud service providers like gcp, Azure and AWS and the current project

is one of the top ranked projects on github and upcoming lectures we will take a quick look at Docker

## Docker Swarn

We will now get a quick introduction to Docker swan.

Docker Swan has a lot of concepts to cover and requires its own course.

But we will try to take a quick look at some of the basic details so you can get a brief idea on what

it is.

What Docker swan you could now combine multiple Docker machines together into a single cluster Docker

swarm.

We'll take care of distributing your services or your application instances into separate hosts for

high availability and for load balancing across different systems and hardware to set up a Docker swarm.

You must first have hosts or multiple hosts with Docker installed on them.

Then you must designate one host to be the manager or the master or it's the swarm manager as it is

called and others as slaves or workers.

Once you're done with that run the docker swarm init command on the swarm manager and that will initialize

the swarm manager.

The output will also provide the command to be run on the workers to copy the command and run it on

the worker nodes to join the manager.

After joining the swarm the workers are also referred to as nodes and you're now ready to create services

and deploy them on the swarm cluster so let's get into some more details as you already know to run

an instance of my web server.

I run the docker run command and specify the name of the image I wish to run.

This creates a new container instance of my application and serves on my web server.

Now that we have learned how to create a swarm cluster How do I utilize my cluster to run multiple instances

of my web server.

Now one way to do this would be to run the docker run command on each worker node.

But that's not ideal as I might have to log into each node and run this command and there could be hundreds

of nodes I will have to setup load balancing myself allowed to monitor the state of each instance myself

and if instances where to fail I'll have to restart them myself.

So it's going to be an impossible task and that is where Docker swarm orchestration concerning Dockers

swarm orchestrator does all of this for us.

So far we've only set up this one cluster but we haven't seen orchestration in action.

The key component of swarm orchestration is the docker service Docker services are one or more instances

of a single application or service that runs across the site.

The nodes in the swarm cluster for example, in this case, I could create a Docker service to run multiple

instances off my web server application across worker nodes in my swarm cluster.

For this I run the docker service create command on the manager node and specify my image name there

which is my web server in this case and use the option replicas to specify the number of instances of

my web server I would like to run across the cluster.

Since I specified three replicas and I get three instances of my web server distributed across the different

worker nodes remember the Dockers service command must be run on the manager node and not on the worker

node the docker service create command is similar to the docker run command.

In terms of the options past such as the -e environment variable the -p for publishing ports the

network option to attach container to a network etc. Well that's a high level introduction to Docker

swarm.

There is a lot more to know such as configuring multiple managers overlay networks etc..

As I mentioned it requires its own separate course.