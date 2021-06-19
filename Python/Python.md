# Comandos úteis Com Python - Desde o Básico 

## Pra ler algo do usuário: 
```input()```


## Tipo do objeto:
```type(var_name)```


## NÚMEROS AVANÇADOS:
Converte pra hexadecimal:
```hex()```

Converte pra binário:
```bin()```

Elevar número:
```pow(num1, num2)``` 

Valor absoluto:
```abs()```

Arredonda para o número inteiro mais próximo:
```round()```

Exemplo com round():
1° parâmetro: valor real. 2° parâmetro, quantas casas após a vírtula. Nesse caso, somente 2 casas. A saída seria: 12.12
```round(12.123, 2)```
  

## Manipulando texto:
### Fatiamento:
```string[ inicio : fim : passos ]```

Do começo até o 13° índice da string:
``` string[:13]```
 
Do 15° índice até o último índice:
```string[15:]```
 
Do 9°, até o final, de 3 em 3:
```string[9::3]```
 

### Análise:
Comprimento da frase:
```len()```

Conta quantas vezes X coisa aparece na string:
```count('X')```

Começando no caractere 0, até o 13°, conta os X:
```count('X',0,13)```

Procura posição ABC. Se não encontrar, retorna -1:
```find('ABC')```

Retorna True ou False se encontrar ou não:
```'ABC' in frase```


### Transformação:
Substituição:
```replace('ABC', 'CBA')```

String em maisúsculo:
```upper()```

String em minúsculo:
```lower()```

Primeira letra da string em maisúsculo:
```capitalize()```

Primeiro letra de cada palavra da string em maisúsculo:
```title()```

Remove todos os espaços em branco da direita e da esquerda da string:
```strip()```

Remove espaços em branco do lado direito da string:
```rstrip()```

Remove espaços em branco do lado esquerdo da string:
```lstrip()```


### Divisão:
Quebra a string em determinado espaço, tendo uma lista como retorno:
```split()```


### Junção:
Juntar uma string / objeto em outro:
```''.join()```


### FORMATAÇÃO DE IMPRESSÃO - Estilo textual:
20 caracteres à direita:
```print('{:>20}')```

20 caracteres à esquerda:
```print('{:<20}')``` 

20 caracteres centralizados:
```print('{:^20}')```

20 caracteres centralizados em volta de '=':
```print('{:=^20}')```

Exemplo:
```print(f'{String comum alinhado 20 caracteres à direita:>20}')```

 
## Cores no Terminal:
Padrão ANSI - escape sequence:
```\033[style; text; background; m```

Exemplo: 
```\033[1;33;44m``` 
 
### Style - principais são:
  0 - sem estilo
  1 - negrito
  4 - underline - sublinhado
  7 - negative

### Text:
  30 - branco
  31 - vermelho
  32 - verde
  33 - amarelo
  34 - azul
  35 - roxo
  36 - azul claro
  37 - cinza

### Background:
  40 - branco
  41 - vermelho
  42 - verde
  43 - amarelo
  44 - azul
  45 - roxo
  46 - azul claro
  47 - cinza


### Exemplo:
```print(f'\033[1;33m Texto em Amarelo e negrito. \033[m')```


### Break, continue, pass:
Podemos usar as declarações break, continue e pass em nossos loops para adicionar funcionalidades adicionais para vários casos. As três declarações são definidas por:

Para o loop:
```Break```

Continua para o próximo loop:
```Continue```   

Não faz nada:
```Pass```


## RANGE():
Sequência: 
```range(início, fim, passos)```:
   
Exemplo, criando lista:
```lista = range(0, 10)```

Saída: 'De 0 a 9.'
```print(lista)```


## COMPREENSÃO EM LISTA:
Criar lista de forma simples
```lista = [ i for i in range(0,30) ]```

Saída será uma lista de 0 a 29:
```print(lista)```

## Exemplos:
### Eleva o quadrado itens no range e o transformam em lista
```lst = [x**2 for x in range(0,11)]```

### Cria uma lista de números pares, utilizando para isso o if
```lst = [x for x in range(11) if x % 2 == 0]```


## EXPRESSÕES LAMBDAS:
Funções desenvolvidas com apenas 1 linha e tem existência temporária.
O lambda foi projetado para codificar funções simples e def as tarefas maiores.

Exemplos:
### Retornando quadrado do número
```quadrado = lambda num: num ** 2```


Chamando função passando parâmetro:
```quadrado(2)```


## Tuplas - Alguns métodos:
Conta quantos 'x' aparecem na tupla:
```tupla.count('x')``` 

Printa em qual índice está o 'x':
```tupla.index('x')```

Pra apagar a tupla:
```del(nome_tupla)``` 
 

## Listas - Alguns métodos:
adiciona um valor à lista:
```lista.append('x')```

adiciona um valor à lista em determinado índice:
```lista.insert(0, 'x')``` 

apaga um elemento da lista. Por padrão apaga o último:
```lista.pop(indice)```

apaga um elemento da lista indicando o valor:
```lista.remove('valor')``` 

cria uma lista com 10 índices:
```valores = list(range(0, 10))```

ordena os valores da lista em ordem crescente:
```lista.sort()```

ordena valores da lista em ordem decrescente:
```lista.sort(reverse=True)```  

retorna número de elementos da lista:
```len(lista)``` 

posição e valor:
```enumerate(list)```

conta os elementos da lista:
```sum(lista)```


## Dicionários - Métodos mais comuns:
retorna os valores do dicionário:
```dicionario.values()```

retonar as chaves do dicionário:
```dicionario.keys()```

retona chaves e valores do dicionário:
```dicionario.items()```

deleta valor do dicionário:
```del dicionario['chave']```

Cópia:
```dicionario.copy()```


## SETS - CONJUNTOS E BOLEANOS:
Set são conjuntos que dados que só permite valores únicos.

Adicionar um valor ao conjunto:
```var_name.add('value')```
  
Booleanos:
```True, False```

None:
```Espaço reservado que não vai ser atribuído valor.```


## Operadores de comparação em Python:
###  1. OPERADORES DE COMPARAÇÃO:
  ```==, !=, >, <, >=, <=```


###  2. OPERADORES DE COMPARAÇÃO EM CADEIA:
  ```and (todas as expressões), or (apenas 1 das expressões) e not.```

 
## Funções:
funções criadas de forma personalizada:
```def nome_funcao()```


### Interactive help:
função interna do python, como o nome diz, te ajuda:
```help()```

no próprio arquivo .py também funciona. Além do terminal:
```help(print)```

Saída será uma explicação de como a função print() funciona.


## Tratamento de erros:
Python permite tratar erros e criar respostas a essas exceções com a estrutura try except.
Pra tratar: 
```
try:
   tenta fazer isso
except:
   se levantar exceção (erro).
else:
   se deu tudo certo, faça x
finally:
   independente se der erro ou não, é executado.
```
