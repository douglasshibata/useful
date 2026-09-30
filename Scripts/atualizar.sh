#!/bin/bash
set -euo pipefail

echo "Atualizando os pacotes e o sistema..."

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get autoclean -y
sudo apt-get autoremove -y

echo "Sistema atualizado com sucesso!"
