#!/bin/bash
echo "O que deseja fazer? (1)-Desligar/ (2)-Reiniciar "
read resposta
case "$resposta" in
    1)
        echo " Se prepare para desligar , foi um ótimo dia de serviço=)"
	shutdown now
    ;;
    2)
        echo "O Computador irá Reiniciar, aguarde."
	reboot
    ;;
    *)
        echo "Opção inválida"
    ;;
esac
