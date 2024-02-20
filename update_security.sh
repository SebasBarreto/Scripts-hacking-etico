# update_security.sh
#!/bin/bash

echo "Actualizando la lista de paquetes..."
sudo apt update

echo "Actualizando paquetes instalados..."
sudo apt upgrade -y

echo "Aplicando parches de seguridad..."
sudo apt-get install unattended-upgrades
sudo unattended-upgrade -d

echo "Actualización de seguridad completada."
