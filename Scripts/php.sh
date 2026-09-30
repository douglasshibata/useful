#!/bin/bash
set -euo pipefail

echo "Script Apache2"
echo "O que deseja fazer?"
echo "(1)- Iniciar Servidor Apache2"
echo "(2)- Parar o Servidor Apache2"
echo "(3)- Reiniciar o Servidor Apache2"
read -r resposta

case "$resposta" in
    1)
        echo "Iniciando Servidor Apache2..."
        sudo systemctl start apache2
        ;;
    2)
        echo "Parando o Servidor Apache2..."
        sudo systemctl stop apache2
        ;;
    3)
        echo "Reiniciando o Servidor Apache2..."
        sudo systemctl restart apache2
        ;;
    *)
        echo "Opção inválida" >&2
        exit 1
        ;;
esac
