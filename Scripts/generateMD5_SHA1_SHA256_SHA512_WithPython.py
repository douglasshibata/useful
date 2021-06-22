import hashlib
from time import sleep


def print_message():
    print('\n \033[33m """ Programa gerador de hash MD5, SHA1, SHA256 e SHA512 """ \033[m \n')


while True:
    print_message()
    try:
        string = str(input('\n \033[36mDigite um texto para gerar hash:\033[m '))
        while True:
            menu = int(input('\n \033[1;35mMENU - ESCOLHA O TIPO DE HASH: \n'
                         '1 - MD5\n'
                         '2 - SHA1\n'
                         '3 - SHA256\n'
                         '4 - SHA512\n'
                         'Digite o número de sua escolha: \033[m'))
            
            if menu == 1 or menu == 2 or menu == 3 or menu == 4:
                break
            print('\033[1;31mOpção inválida! Escolha somente entre 1 e 4!\033[m ')

    except Exception as error:
        print(f'Erro: {error.__class__}, descrição: {error}.\nTente novamente.')

    else:
        print('\nGerando HASH, aguarde 2 segundos...')
        sleep(2)

        if menu == 1:
            resultado = hashlib.md5(string.encode('utf-8'))
            print(f'\n \033[1;32m O hash MD5 da string \033[4m"{string}"\033[m é \033[m: {resultado.hexdigest()}')
            break
        elif menu == 2:
            resultado = hashlib.sha1(string.encode('utf-8'))
            print(f'\n \033[1;32m O hash SHA1 da string \033[4m"{string}"\033[m é \033[m: {resultado.hexdigest()}')
            break
        elif menu == 3:
            resultado = hashlib.sha256(string.encode('utf-8'))
            print(f'\n \033[1;32m O hash SHA256 da string \033[4m"{string}"\033[m é \033[m: {resultado.hexdigest()}')
            break
        else:
            resultado = hashlib.sha512(string.encode('utf-8'))
            print(f'\n \033[1;32m O hash SHA512 da string \033[4m"{string}"\033[m é \033[m: {resultado.hexdigest()}')
            break
