# Comandos Básicos do poweshell

## Pra abrir o manual de ajuda
```ps
help
Get-Help
```
### Para pesquisar uma palavra ou frase em todos os arquivos de ajuda, digite:
```ps
Get-Help <search-term>
```

### Atualizamos os tópicos de ajuda do PowerShell com o comando Update-Help
```ps
Update-Help
```
## Para ver informações sobre o disco
```ps
Get-Disk
```
## Para ver as variáveis de ambiente
```ps
$env:path
```
## Para ver o tipo da variável 
```ps
$env:path.GetType()
```
## Listar todos métodos e o tipo da variável
```ps
 $env:path | Get-Member  
```
## Mostrar os apelidos dos comandos
```ps
 Get-Alias
```
### Mostrar um comando específico na lista de apelidos
```ps
 Get-Alias -name dir
```
## Procurar um comando 
```ps
 Get-command 
```
### Procurar um comando por nome
```ps
 Get-command  -name *rename*
```

## Para saber o que o comando faz, sem executar ele
```ps
rename-item teste.txt test1.txt -Whatif
```
### Obtemos todos os scripts que atuam com Aliases, com o comando "Get-Command -noun alias"
```ps
Get-Command -noun alias
```

### O Get-Help retorna a ajuda ou a sintaxe de um comando, quando um documento de ajuda não estiver disponível
```ps
Get-Help new-alias
```

### Com new-alias podemos criar novos aliases
```ps
new-alias -Name="rename" rename-item
```

#Podemos verificar nosso alias criado com o comando abaixo
get-alias rename