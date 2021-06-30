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