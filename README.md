# Systems Integration #

## Introduction ##

Neste trabalho prático de Integração de Sistemas de Informação, temos o objetivo de ``criar um sistema robusto baseado num código base fornecido pelos professores`` e ``configurado via Docker Compose``. Tivemos de escolher um dataset do ``Kaggle``, atendendo aos critérios necessários, converter esse dataset, em CSV, para um ficheiro XML e por fim criar um ``XML Schema para validação do XML criado``.
O sistema inclui um servidor ``XMLRPC em Python``, que permite a ``conversão de dados de CSV`` para XML e a adição de informações de ``localização através das coordenadas GPS, utilizando uma API externa, a Nomination``. Foi criada a interação com um banco de dados ``PostgreSQL, onde são armazenados os XMLs`` fornecidos pelos clientes e onde serão executadas as queries.
As queries permitem ao cliente executar consultas avançadas nas colunas XML, abrangendo pesquisa em texto, aplicação de filtros, agrupamento, ordenação e intercâmbio de informações entre diferentes níveis do documento XML.

## Debug Project ##

1. Enter on devcontainer
2. Execute the dockerfile, only `db` and `redis` services

Run `is-db` and `is-redis` service
```sh
  docker compose up --build -d db redis
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
```
```sh
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