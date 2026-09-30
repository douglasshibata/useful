#!/bin/bash
set -euo pipefail

echo "Bem vindo ao script para controlar o serviço do MySQL"
echo -n "O que deseja fazer? (1)-Iniciar / (2)-Parar / (3)-Status / (4)-Reiniciar: "
read -r resposta

case "$resposta" in
    1)
        echo "Inicializando o MySQL..."
        sudo systemctl start mysql 
        ;;
    2)
        echo "Parando o serviço do MySQL..."
        sudo systemctl stop mysql
        ;;
    3)
        echo "Verificando o status do serviço do MySQL..."
        sudo systemctl status mysql 
        ;;
    4)
        echo "Reiniciando o serviço do MySQL..."
        sudo systemctl restart mysql
        ;;
    *)
        echo "Opção inválida" >&2
        exit 1
        ;;
esac
