#!/bin/bash

#Generar claves ssh
#ssh-keygen -t rsa

# Crea el grupo de recursos llamado acopioM
az group create --name acopioM --location westeurope

#Crea una maquina en el grupo de recursos generado anteriormente con nombre maquinaHito4, genero las claves ssh aqui
az vm create --resource-group acopioM --name maquinaHito4 --image UbuntuLTS --generate-ssh-keys > tmp

cat tmp

#Extrae la ip del campo .publicIpAddress del fichero generado anteriormente
ip=$(jq -r '.publicIpAddress' tmp)

#Abro los puertos ssh y http
az network nsg rule create --resource-group acopioM --nsg-name maquinaHito4 --name SSH_rule \
    --protocol tcp \
    --priority 320 \
    --destination-port-range 22 \
    --access allow >/dev/null

az network nsg rule create --resource-group acopioM --nsg-name maquinaHito4 --name HTTP_rule \
    --protocol tcp \
    --priority 300 \
    --destination-port-range 80 \
    --access allow >/dev/null

#Añado la clave publica
az vm user update --resource-group acopioM -n maquinaHito4 -u xenahort --ssh-key-value "$(< $HOME/.ssh/id_rsa.pub)"z

#Clono el proyecto
git clone https://github.com/xenahort/proyectoCloudComputing
cd proyectoCloudComputing/provision/ansible/

#Modifico el fichero hosts
echo "[ubuntuserver]\nxenahort ansible_ssh_port=22 ansible_ssh_host=$ip\n[ubuntuserver:vars]\nansible_ssh_user=xenahort\nansible_ssh_private_key_file=$HOME/.ssh/id_rsa" > hosts

#Finalmente hay que ejecutar el playbook
ansible-playbook playbook.yml