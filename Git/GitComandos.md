## Comandos para o git  

### Configura as variáveis do nome e email 
```bash
	git config --global user.name "Nome"
	git config --global user.email "Email"
```
mostra a lista das configurações
```bash
	git config --list
```
Configurar um editor padrão
```bash
	git config --global core.editor "atom"
```
### Iniciar um repositório 
```bash
	git init
```
Para adicionar arquivos ao repositório
```bash
	git add .
```
o ponto(.) representa a adição de todos os arquivos modificados, caso queria adicionar arquivo por arquivo utilizar
```bash
    git add path/to/file/modificado
```
### para mostrar as alterações feitas antes do commit
```bash
	git diff
```
para ver as mudanças no arquivo
```bash
	git diff --staged
```
### para colocar uma mensagem no commit , a flag -m referência que será escrita uma mensagem
```bash
	git commit -m 'comentário'
```
### para ver os logs do git
```bash
	git log
```
para ver os commits para recents
```bash
	git log -1
```
comando para listar os log de diversas formas
```bash
	git log --pretty=
```
```bash
 git log --pretty=oneline
```
```bash
	git log --numstat
```

### para voltar e checar os arquivos do commit anterior
```bash
	git checkout HEAD~3 list.txt
```
```bash
	git checkout LOCALIZAÇÃO~POsiçãoDoCommit <arquivo>
```
para voltar para o ultimo commit 
```bash
	git checkout HEAD <arquivo>
```
    
### para refazer uma mudança que não era para ser feita antes de fazer o commit e após fazer o	git add <nomeArquivo>
```bash
	git reset <nomearquivo>
```
para refazer uma mudança que não era para ser feita após ter feito o commit
```bash
	git reset HEAD~1 --soft (remove o commit)(NÃO MUDA O ARQUIVO) 
```
```bash
	git reset HEAD~1 --mixed (remove o commit e também as mudanças feitas)
```
```bash
	git reset HEAD~1 --hard (volta um commit, removendo as mudanças feitas)
```
### para criar uma branch(ramo)
```bash
	git branch <nomeDaBranch> 
```
para listar as branch
```bash
	git branch
```
para mudar para a branch
```bash
	git checkout <nomeDaBranch>
```
para conseguir mesclar os arquivos em cada branch
	voltar para o branch master
```bash
	git checkout master
```
e em seguida mesclar com a brach criada.
```bash
	git merge <nomeDaBranch>
```
### para colocar um projeto no github que ja esteja criado na sua máquina local, porém sem repositório online
```bash
	git help remote(para ver os comandos)
```
```bash
	git remote add origin <url do repositório do github>
```
para ver se está tudo conectado
```bash
	git remote -v 
```
### para subir o seu repositório local para o remoto
```bash
	git push origin master 	
```
### Comando para saber quem é o culpado do commit 
```bash
	git blame nomedoArquivo
```
### comando para remover o lixo que pode ter sido gerado
```bash
	git gc
```

### Comando para adicionar uma tag
```bash
	git tag -a v1.0.0 -m "comentario"
```
#### Comando para ver as tags
```bash
	git tag
```
#### Comando para ver as tags específica

```bash
	git show v1.0.0
```
#### Comando para remover uma  tag específica

```bash
	git tag -d v1.0.0
```
#### Comando para subir as tags
```bash
	git push origin --tags
```
#### Comando para subir uma tag específica
```bash
	git push origin v1.0
```
#### Comando para adicionar tag específica
```bash
	git tag -a v1.0.2 hashDoCommit
```
