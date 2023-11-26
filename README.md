# Systems Integration #

## Introduction ##

Welcome to the Systems Integration Development Kit! This toolkit is specially designed to facilitate the setup of your development environment and manage dependencies effortlessly for the 1st assignment (TP1) in the Systems Integration class, part of the Informatics Engineering course at IPVC/ESTG.

## Debug Project ##

1. Enter on devcontainer
2. Execute the dockerfile, only `is-db` and `is-redis` services

Run `is-db` and `is-redis` service
```sh
  docker compose up --build -d is-db is-redis
```

Add those to the same network of the debug project
```sh
  docker ps -a
  docker network create bridge_net
  docker network connect bridge_net <is-db-process-id>
  docker network connect bridge_net <is-redis-process-id>
```

Finally run them separately, on `dev` environment
```sh
  python ./src/rpc-client/main.py dev

  python ./src/rpc-server/main.py dev
```

## Execute project ##

Build the containers
```sh
  docker compose up --build -d
```

Enter on is-rpc-client container
```sh
  docker exec -it is-rpc-client python /app/main.py
```
___
#### _Informatics Engineering @ipvc/estg, 2023-2024_ ####