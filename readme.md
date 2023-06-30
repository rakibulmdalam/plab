# DevOps

To launch the API server here are the steps we need to follow:

## install docker
First, we need to install docker on our machine. To do so, we can follow the instructions on the official website: https://docs.docker.com/engine/install/

## install docker-compose
Then, we need to install docker-compose on our machine. To do so, we can follow the instructions on the official website: https://docs.docker.com/compose/install/

## clone the repository
Now, we need to clone the repository on our machine. To do so, we can run the following command:
```
git clone 

```

## launch the API server
Finally, we can launch the API server. To do so, we can run the following command:
```
docker-compose up -d

```

## test the API server

To test the API server using locust, we can run the following command:
```
locust -f locustfile.py

```

Then, we can go to http://localhost:8089/ and enter the number of users to simulate and the hatch rate. Then, we can click on "Start swarming" to start the test.

## stop the API server
To stop the API server, we can run the following command:
```
docker-compose down

```

## clean the API server
To clean the API server, we can run the following command:
```
docker-compose down -v

```

## clean the API server and remove the images

To clean the API server and remove the images, we can run the following command:
```

docker-compose down -v --rmi all

```

## clean the API server and remove the images and the volumes

To clean the API server and remove the images and the volumes, we can run the following command:
```
docker-compose down -v --rmi all --remove-orphans

```

## clean the API server and remove the images and the volumes and the networks

To clean the API server and remove the images and the volumes and the networks, we can run the following command:
```
docker-compose down -v --rmi all --remove-orphans --remove-networks

```

