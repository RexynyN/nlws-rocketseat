## Kill and Remove all containers

```sudo docker stop $(docker ps -a -q) && sudo docker rm $(docker ps -a -q)```