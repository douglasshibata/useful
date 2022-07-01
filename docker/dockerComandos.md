- #### Exibe todos os containers em execução no momento.
```bash
    docker ps
```
- ### exibe todos os containers, independentemente de estarem em execução ou não.
```bash
    docker ps -a 
```
- ### conecta o terminal que estamos utilizando com o do container.
```bash
    docker run -it NOME_DA_IMAGEM 
```
- inicia o container com id em questão.
```bash
docker start ID_CONTAINER 
```
 - interrompe o container com id em questão.
```bash
docker stop ID_CONTAINER
```
- inicia o container com id em questão e integra 
os terminais, além de permitir interação entre ambos.
```bash
docker start -a -i ID_CONTAINER 
```
- remove o container com id em questão.
```bash
docker rm ID_CONTAINER 
```
- remove todos os containers que estão parados.
```bash
docker container prune 
```
- remove a imagem passada como parâmetro.
```bash
docker rmi NOME_DA_IMAGEM 
```
- ao executar, dá um nome ao container
```bash
docker run -d -P --name NOME dockersamples/static-site 
```
- define uma porta específica 
```bash
docker run -d -p 12345:80 dockersamples/static-site
``` 
para ser atribuída à porta 80 do container, neste caso 12345.
```bash
docker run -d -P -e AUTHOR="Fulano" dockersamples/static-site 
```

## Comandos relacionados às informações
- ### exibe a versão do docker que está instalada.
```bash
    docker version 
```
- retorna diversas informações sobre o container.
```bash
docker inspect ID_CONTAINER 
```
- exibe todos os containers em execução no momento.
```bash
docker ps 
```
- exibe todos os containers, independentemente de estarem em execução ou não.
```bash
docker ps -a 
```
#### Mostra o histórico do container
```bash
docker history <ID_container> 
```
### Listar imagens que foram baixadas
```bash
docker images
```
##### Comandos relacionados à execução
- cria um container com a respectiva imagem passada como parâmetro.
```bash
docker run NOME_DA_IMAGEM 
```
 - conecta o terminal que estamos utilizando com o do container.
```bash
docker run -it NOME_DA_IMAGEM
```
- ao executar, dá um nome ao container e define uma porta aleatória.
```bash
docker run -d -P --name NOME dockersamples/static-site 
```
- define uma porta específica para ser atribuída à porta 80 do container, neste caso 12345.
```bash
docker run -d -p 12345:80 dockersamples/static-site 
```
- cria um volume no respectivo caminho do container.
```bash
docker run -v "CAMINHO_VOLUME" NOME_DA_IMAGEM 
```
- cria um container especificando seu nome e qual rede deverá ser usada.
```bash
docker run -it --name NOME_CONTAINER --network NOME_DA_REDE NOME_IMAGEM 
```
##### Comandos relacionados à inicialização/interrupção
- inicia o container com id em questão.
```bash
docker start ID_CONTAINER
```
- inicia o container com id em questão e integra os terminais, além de permitir interação entre ambos.
```bash
docker start -a -i ID_CONTAINER 
```
- interrompe o container com id em questão.
```bash
docker stop ID_CONTAINER 
```
- Pausa o container com id em questão.
```bash
docker pause ID_CONTAINER 
```
- Para todos os containers.
```bash
docker stop $(docker container ls -q)
```
##### Comandos relacionados à remoção
- remove o container com id em questão.
```bash
docker rm ID_CONTAINER 
```
- remove todos os containers que estão parados.
```bash
docker container prune 
```
- remove a imagem passada como parâmetro.
```bash
docker rmi NOME_DA_IMAGEM 
```
##### Comandos relacionados à construção de Dockerfile
 - cria uma imagem a partir de um Dockerfile.
```bash
docker build -f Dockerfile
```
- constrói e nomeia uma imagem não-oficial.
```bash
docker build -f Dockerfile -t NOME_USUARIO/NOME_IMAGEM
```
- constrói e nomeia uma imagem não-oficial informando o caminho para o Dockerfile.
```bash
docker build -f Dockerfile -t NOME_USUARIO/NOME_IMAGEM CAMINHO_DOCKERFILE 
```
##### Comandos relacionados ao Docker Hub
- inicia o processo de login no Docker Hub.
```bash
docker login 
```
- envia a imagem criada para o Docker Hub.
```bash
docker push NOME_USUARIO/NOME_IMAGEM
```
- baixa a imagem desejada do Docker Hub.
```bash
docker pull NOME_USUARIO/NOME_IMAGEM
```
##### Comandos relacionados à rede
- mostra o ip atribuído ao container pelo docker (funciona apenas dentro do container).
```bash
hostname -i 
```
- cria uma rede especificando o driver desejado.
```bash
docker network create --driver bridge NOME_DA_REDE
```

##### Comandos relacionados ao docker-compose
- Realiza o build dos serviços relacionados ao arquivo docker-compose.yml, assim como verifica a sua sintaxe.
```bash
docker-compose build
```
- Sobe todos os containers relacionados ao docker-compose, desde que o build já tenha sido executado.
```bash
docker-compose up 
```
- Para todos os serviços em execução que estejam relacionados ao arquivo docker-compose.yml.
```bash
docker-compose down 
```


#### Teoria DockerFile
A instrução ARG carrega variáveis apenas no momento de build da imagem, enquanto a instrução ENV carrega variáveis que serão utilizadas no container


#### Utilizar um diretório da sua máquina no docker ( mount)
```bash
docker run –it --mount type=bind,source=path-local,target=/app-path-ubuntu ubuntu bash
```

#### Volume
* Listar volumes
```bash
docker volume ls
```
* Criar volume
```bash
docker create volume <name>
```
* Utilizando o volume na aplicação
```bash
docker run -it --mount source=meu-volume, target=/app ubuntu bash
```
