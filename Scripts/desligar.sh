#!/bin/bash
set -euo pipefail

echo "O que deseja fazer? (1)-Desligar / (2)-Reiniciar"
read -r resposta

case "$resposta" in
    1)
        echo "Se prepare para desligar. Tenha um ótimo dia!"
        sudo shutdown now
        ;;
    2)
        echo "O computador irá reiniciar, aguarde..."
        sudo reboot
        ;;
    *)
        echo "Opção inválida" >&2
        exit 1
        ;;
esac
