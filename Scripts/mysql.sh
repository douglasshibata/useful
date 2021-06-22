#!/bin/bash
echo  "Bem vindo ao script para controlar o serviço do Mysql"
echo -n "O que deseja fazer? (1)-Iniciar/ (2)-Parar /(3)-Status / (4) - Reiniciar "
echo ""
read resposta
case "$resposta" in
    1)
        echo "Inicializando o mysql "
        sudo systemctl start mysql 
    ;;
    2)
        echo "Parando o serviço do mysql."
        sudo systemctl stop mysql
    ;;
    3)
        echo "Verificando o status do serviço do mysql"
        sudo systemctl status mysql 
    ;;
    4)
        echo "Restart do serviço do mysql"
	    sudo systemctl restart mysql
    ;;
    *)
        echo "Opção inválida"
    ;;
esac
