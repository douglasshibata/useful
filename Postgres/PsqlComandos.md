# Comandos úteis para o SGBD Postgresql e PSQL via terminal

## Para entrar no psql
```bash
	psql -h host -U user -W (se tiver senha) -d database
```
# Para executar um arquivo sql no psql após entrar na Database desejada
 Mover o arquivo para pastar /tmp para que seja executável pelo usuário postgres
```bash
	\i path/to/file
```

* Para restaurar o banco
```bash	
	pg_restore -d db_name /tmp/sqlfile
```
##
* para listar bancos no psql
```bash
\list
```
* para listar usuarios 
 ```bash
\du
```
* para exibir ajuda de todos os comandos
```bash
\h *
```
