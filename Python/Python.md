# Comandos úteis Com Python - Desde o Básico 

## Primeiros comandos em python: 
    Toda variável em python é um objeto
    Toda variável é ideal que seja declarado em minúscula
    Pra ler algo do usuário -> input().


## Tipos primitivos e saída de dados:
    Principais:
    int(), float(), bool, str()
    
	Tipo do objeto:
    type()


## Operadores aritméticos:
    +, -, *, /, **, //, %
    
    ** -> potência
    // -> divisão inteira
    % -> resto da divisão
    
    Precedência (ordem) -> (), **, *, /, //, %, +, -
    Imprimir X casas após a vírgula -> {:.2f}
    Ou seja, 2 casas após a vírgula.
    
    \n -> quebra linha.
    \t -> tabulação.


## NÚMEROS AVANÇADOS:
	hex(), converte pra hexadecimal
    bin(), converte pra binário
    pow(num1, num2), elevar número 
    abs(), valor absoluto
    round(), arredonda para o número inteiro mais próximo
    round(12.123, 2), 1° parâmetro: valor real. 2° parâmetro, quantas casas após a vírtula. Nesse caso, somente 2 casas. A saída seria: 12.12


## Utilizando módulos:
    Pra incluir algo, devo importar, ou seja, import()
    Pra não importar tudo, from algo import x
    Exemplo:
    - from math import ceil

    Importando módulo ceil do pacote math.
          

     
## Manipulando texto:
     String - cadeia de texto

    Fatiamento:
        string[ inicio : fim : passos ]

     Fatiamento de string, pega sempre até o penúltimo - frase[9:13], de 9 até o 12°.
     Frase[:13], do começo até o 13° índice da string
     Frase[15:], do 15° índice até o último índice.
     Frase[9::3], do 9°, até o final, pulando de 3 em 3
     
     Análise:
          - len(), comprimento da frase
          - count('X'), conta quantas vezes X coisa aparece na string
               - count('X',0,13), começando no caractere 0, até o 13°, conta os X
          - find('ABC'), procura posição ABC. Se não encontrar, retorna -1
          - 'ABC' in frase, retorna True ou False se encontrar ou não

     Transformação:
          - replace('ABC', 'CBA'), substituição.
          - upper(), string em maisúsculo
          - lower(), string em minúsculo
          - capitalize(), primeira letra da string em maisúsculo
          - title(), primeiro letra de cada palavra da string em maisúsculo
          - strip(), remove todos os espaços em branco da direita e da esquerda da string
          - rstrip(), remove espaços em branco do lado direito da string
          - lstrip(), remove espaços em branco do lado esquerdo da string

     Divisão:
          - split(), quebra a string em determinado espaço, tendo uma lista como retorno.

     Junção:
          - '-'.join(), juntar uma coisa na outra.


### FORMATAÇÃO DE IMPRESSÃO:    
    Métodos embutidos - built-in:
        string.method()
        objeto.metodo(parâmetros)

    Estilo textual:
        print('{:>20}') -> 20 caracteres à direita
        print('{:<20}') -> 20 caracteres à esquerda
        print('{:^20}') -> 20 caracteres centralizados
        print('{:=^20}') -> 20 caracteres centralizados em volta de '='


## Condições em Python (if..else):
     Estrutura:
        if:
            faça algo
        elif:
            faça outra coisa
        else:
            senão, faça isso.

     Python não tem operador ternário.
          Similar seria: print('isso' if (condição) else 'isso aqui')
     


## Cores no Terminal:
     Padrão ANSI - escape sequence
     \033[style; text; background; m
     Exemplo: \033[0;33;44m 
     
     Style - principais são:
          0 - sem estilo
          1 - negrito
          4 - underline - sublinhado
          7 - negative

     Text:
          30 - branco
          31 - vermelho
          32 - verde
          33 - amarelo
          34 - azul
          35 - roxo
          36 - azul claro
          37 - cinza

     Background:
          40 - branco
          41 - vermelho
          42 - verde
          43 - amarelo
          44 - azul
          45 - roxo
          46 - azul claro
          47 - cinza

    Exemplo:
        print(f'\033[1;33m Texto em Amarelo e negrito. \033[m')


## Repetições em Python (for):
     Quando usar quando já sabes o limite de parada.

     for X in range(começo, final):
          faça Z...

     for X in range(começo, final, passos):
          faça Z...


## Interrompendo repetições while:
     Python tem somente for e while, diferente de outras linguagens que têm o do-while 


### Break, continue, pass:
    Podemos usar as declarações break, continue e pass em nossos loops para adicionar funcionalidades adicionais para vários casos. As três declarações são definidas por:
    Break: -> Para o loop
    Continue: -> Vai para o próximo loop           
    Pass: -> Não faz nada

    Pensando nas declarações break e continue , o formato geral do loop while se parece com isto:
        while test: 
            código if test: 
                break 
            if test: 
                continue 
            else:
                pass

## RANGE():
    Criar listas pré determinadas. Sequência: range(início, fim, passos):
               
    Exemplo, criando lista:
         lista = range(0, 10)
         print(lista) -> 'De 0 a 9.'


## COMPREENSÃO EM LISTA:
    Criar lista de forma simples
    lista = [ i for i in range(0,30) ]

    Exemplos:
    # Eleva o quadrado itens no range e o transformam em lista
    lst = [x**2 for x in range(0,11)]

    # Cria uma lista de números pares, utilizando para isso o if
    lst = [x for x in range(11) if x % 2 == 0]


## EXPRESSÕES LAMBDAS:
    Funções desenvolvidas com apenas 1 linha e tem existência temporária.
    O lambda foi projetado para codificar funções simples e def as tarefas maiores.
    
    Exemplos:
        - Retornando quadrado do número
        quadrado = lambda num: num ** 2
        quadrado(2)

        - Verificando se número é par
        eh_par = lambda num: num % 2 == 0
        eh_par(2) -> Retorna um booleano

        - Retornando primeiro caractere ou índice
        primeiro_caractere = lambda string: string[0]
        primeiro_caractere('Maroc') -> retorna 'M'


## Tuplas:
     Tupla = tuple()
     Tuplas = variáveis compostas, que podem armazenar vários valores.
          Acessados por índices
          São IMUTÁVEIS, ou seja, uma vez criado, não é possível fazer mudança.
          Posso adicionar valores à tuplas de difentes tipos: int, str...

     Alguns métodos:
          - tupla.count('x') -> conta quantos 'x' aparecem na tupla
          - tupla.index('x') -> printa em qual índice está o 'x'
          - Pra apagar a tupla -> del(nome_tupla)
     

## Listas:
     Lista = list()
     As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais (índices).
     São mutáveis, posso alterar um valor.

     Alguns métodos:
          - lista.append('x') -> adiciona um valor à lista
          - lista.insert(0, 'x') -> adiciona um valor à lista em determinado índice
          - lista.pop(indice) -> apaga um elemento da lista. Por padrão apaga o último.
          - lista.remove('valor') -> apaga um elemento da lista indicando o valor.
          - valores = list(range(0, 10)) -> cria uma lista com 10 índices
          - lista.sort() -> ordena os valores da lista em ordem crescente
               - lista.sort(reverse=True) -> ordena valores da lista em ordem decrescente  
          - len(lista) -> retorna número de elementos da lista
          - enumerate(list) -> posição e valor.
          - sum(lista) -> conta os elementos da lista

## Dicionários:
     Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
     Dicionario = {} ou dicionario = dict()
     dicionario = {"chave": "valor", "chave": "valor"}

     Métodos mais comuns:
          dicionario.values() -> retorna os valores do dicionário
          dicionario.keys() -> retonar as chaves do dicionário
          dicionario.items() -> retona chaves e valores do dicionário
          del dicionario['chave'] -> deleta valor do dicionário
          dicionario.copy() -> faz a cópia. Pois o dicionario[:] não funciona com dict's.


## SETS - CONJUNTOS E BOLEANOS:
    Set são conjuntos que dados que só permite valores únicos
    var_name = set()
    var_name.add('value')
    lista = [11,22,33,33,44,44]
    new_lista = set(lista) -> retorna um set com valores únicos da lista
          
    Booleanos:
        True, False

    None:
        Espaço reservado que não vai ser atribuído valor.




## Operadores de comparação em Python:
     1. OPERADORES DE COMPARAÇÃO:
          ==, !=, >, <, >=, <=


     2. OPERADORES DE COMPARAÇÃO EM CADEIA:
          and (todas as expressões), or (apenas 1 das expressões) e not.

     

## Funções:
     Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.

     def nome_funcao() - funções criadas de forma personalizada.
     Pra ser executada, basta chamar / invocar pelo nome da função.
     Podem ou não receber parâmetros
     

     Empacotar parâmetros: 
          def contador(* num): -> função que vai receber n parâmetros
               print(num) -> imprime tupla de cada parâmetro recebido. 


     Interactive help:
          - help() -> função interna do python
               - Basta digitar nome: print. tem a explicação de todas as funções.
          - help(print)..., no próprio arquivo .py também funciona. Além do terminal


     Docstring:
          - String de documentação
          - Serve pra ver a documentação de um determinado método criado por outro dev
          - Pra eu definir o manual da minha função, basta explicitar manual entre """ """
          - def manual():
               """ Manual da Minha Função """
          - help(manual) -> vai imprimir manual da função.


     Parâmetros opcionais:
          - Se a função deixou explícito que recebe 3 parâmetros, caso seja enviado somente 2, eu posso deixar o 3° parâmetro como opcional:
               - def somar(a, b, c=0): -> Nesse caso, parâmetro C recebe 0 por padrão.


## Módulos e pacotes:
    Nada mais é que separar funções em outro arquivo.py e importá-lo
	RECOMENDAÇÃO: importar o módulo completo, pois se tiver outro módulo com função de mesmo nome, pode confundir o python em relação a execução do mesmo. 

    - Só criar uma pasta dentro do projeto com o nome do meu pacote. De lá, importar
               from nome_pacote import nome_modulo...

    - Dentro de cada pacote tem que ter um arquivo chamado __init__.py
               - Serve pra marcar diretórios no disco como um pacote python

## Tratamento de erros:
     Python permite tratar erros e criar respostas a essas exceções com a estrutura try except.
     Pra tratar: 
          try:
               tenta fazer isso
          except:
               se levantar exceção (erro).
          else:
               se deu tudo certo, faça x
          finally:
               independente se der erro ou não, é executado.
