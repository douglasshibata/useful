## Comandos e configurações Apache

### Instalar 
```bash
sudo apt install apache2
```

#### Para verificar se o apache está configurado
```bash
apachectl -M
```
### se você tiver um firewall ufw configurado, abra as portas http e https:
```bash
sudo ufw allow "Apache Full"
```
#### Instalar o mod_ssl:
```bash
yum install mod_ssl openssl
or
apt install mod_ssl openssl
```
#### Habilitando o mod SSL
```bash
sudo a2enmod ssl
```
#### Gerar private Key:
```bash
sudo openssl genrsa -out ca.key 2048
```

#### Gerar o arquivo CSR: 
```bash
sudo openssl req -new -key ca.key -out ca.csr
```

#### Gerar Self Signed Key: 
```bash
sudo openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
```

#### Copiar os arquivos gerados para a localização correta: 
```bash
sudo cp ca.crt /etc/pki/tls/certs/
sudo cp ca.key /etc/pki/tls/private/
sudo cp ca.csr /etc/pki/tls/private/
```

#### Criar/editar o arquivo ssl.conf no caminho /etc/httpd/conf.d/ssl.conf e inserir o seguinte conteúdo:
<VirtualHost {{MAQUINA_IP}}:443>
DocumentRoot /var/www/html
ServerName {{HOSTNAME}}
SSLEngine on
SSLCertificateFile /etc/pki/tls/certs/ca.crt
SSLCertificateKeyFile /etc/pki/tls/private/ca.key
</VirtualHost>

Acessar arquivo de configuração do apache no caminho /etc/httpd/conf/httpd.conf


#### Confirme se o apache está com algum problema no arquivo de configuração com o comando:
```bash
 apachectl configtest
```
##### Reiniciar o apache:
```bash
systemctl restart httpd
```

###### Referencia 
[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-20-04-pt)