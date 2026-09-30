#!/bin/bash
set -euo pipefail

echo "Bem vindo ao script para controlar o serviço do MongoDB"
echo -n "O que deseja fazer? (1)-Iniciar / (2)-Parar / (3)-Status: "
read -r resposta

case "$resposta" in
    1)
        echo "Inicializando o MongoDB..."
        sudo systemctl start mongod
        ;;
    2)
        echo "Parando o serviço do MongoDB..."
        sudo systemctl stop mongod
        ;;
    3)
        echo "Verificando o status do serviço do MongoDB..."
        sudo systemctl status mongod
        ;;
    *)
        echo "Opção inválida" >&2
        exit 1
        ;;
esac
