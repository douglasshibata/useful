#!/bin/bash
echo  "Bem vindo ao script para controlar o serviço do mongodb"
echo -n "O que deseja fazer? (1)-Iniciar/ (2)-Parar /(3)-Status "
echo ""
read resposta
case "$resposta" in
    1)
        echo "Inicializando o mongodb "
	sudo systemctl start mongod 
    ;;
    2)
        echo "Parando o serviço do mongodb."
	sudo systemctl stop mongod 
    ;;
    3)
        echo "Verificando o status do serviço do mongodb"
	sudo systemctl status mongod 
    ;;
    *)
        echo "Opção inválida"
    ;;
esac
