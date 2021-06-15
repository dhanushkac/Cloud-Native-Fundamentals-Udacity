# Cloud-Native Fundamentals, Udacity ☁️🔧

## docker python-hello-world

### Commands
---

List active containers

```bash
$ docker ps
```

List all containers

```bash
$ docker ps -a
```

View available docker images
```bash
$ docker images
```

Start a container
```bash
$ docker start <container_id>
```

Stop a container
```bash
$ docker stop <container_id>
```

Remove a container
```bash
$ docker rm <container_id>
```

Remove an image
```bash
$ docker rmi <image_id>
```

Create a docker image using `Dockerfile`. Here `.` means the location where the `Dockerfile` exists.
```bash
$ docker build -t python-helloworld .
```

Runs a docker container
```bash
$ docker run -p 5000:5000 -d --name python-helloworld python-helloworld
```

Tags an image
```bash
$ docker tag python-helloworld dhanushka/python-helloworld:v1.0.0
```
Create a container using an image
```bash
docker run -d -p 5001:5000 --name dc-python-hw python-helloworld
```

Create a container using a tagged image
```bash
docker run -d -p 5001:5000 --name dc-python-hw dhanushka/python-helloworld:v1.0.0
```
