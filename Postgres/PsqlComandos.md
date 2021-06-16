# Comandos úteis para o SGBD Postgresql e PSQL via terminal

## Para entrar no psql
```bash
	psql -h host -U user -W (se tiver senha) -d database
```
# Para executar um arquivo sql no psql após entrar na Database desejada
```bash
	\i path/to/file
```
# Mover o arquivo para pastar /tmp para que seja executável pelo usuário postgres
* Para restaurar o banco
```bash	
	pg_restore -d db_name /tmp/sqlfile
```
##
para listar bancos no psql
\list
para listar usuarios 
\du
para exibir ajuda de todos os comandos
\h *