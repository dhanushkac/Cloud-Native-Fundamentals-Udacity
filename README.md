# Cloud Native Fundamentals Udacity ☁️🔧

## Dockerizing Go Hello World 🐋

This is a simple Go web application that prints a "Hello World" message.

## Run the application

This application listens on port `6111`

To run the application, use the following command:
```
go run main.go
```

Access the application on: http://127.0.0.1:6111/


## Docker commands

Creates a docker image
```bash
$ docker build -t go-helloworld .
```

Creates a container using the image
```bash
$ docker run -d -p 6111:6111 --name go-helloworld go-helloworld
```

Tags a image
```bash
$ docker tag go-helloworld  dhanushka/go-helloworld:v1.0.0
```

Creates a container using tagged image
```bash
$ docker run -d -p 6111:6111 --name go-helloworld-tagged  dhanushka/go-helloworld:v1.0.0
```

Push to docker registry
```bash
$ docker push dhanushka/go-helloworld:v1.0.0
```