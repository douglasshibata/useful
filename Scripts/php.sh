#!/bin/bash
echo -ne "Script Apache2
 \n O que deseja fazer?
 \n (1)- Iniciar Servidor Apache2 
 \n (2)- Parar o Servidor Apache2 
 \n (3)-Reiniciar o Servidor Apache2 
 \n"
echo ""
read resposta
case "$resposta" in
    1)
        echo "Iniciando Servidor apache2"
        sudo service apache2 start
    ;;
    2)
        echo "Parando o Servidor Apache2"
	    sudo service apache2 stop
    ;;
    3)
	    echo "Reiniciando o Servidor Apache2"
	     sudo service apache2 restart
    ;;
 
    *)
        echo "Opção inválida"
    ;;
esac
