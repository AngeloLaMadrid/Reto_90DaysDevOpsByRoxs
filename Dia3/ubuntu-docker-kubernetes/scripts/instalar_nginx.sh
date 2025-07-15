#!/bin/bash

# Mostrar mensajes en consola
echo "[INFO] Iniciando instalación de Nginx..."

# Actualizar lista de paquetes
sudo apt update -y

# Instalar Nginx
sudo apt install -y nginx

# Habilitar e iniciar el servicio
sudo systemctl enable nginx
sudo systemctl start nginx

# Copiar el index.html personalizado desde la carpeta compartida de Vagrant
sudo cp /vagrant/index.html /var/www/html/index.html

# Confirmar estado del servicio
sudo systemctl status nginx --no-pager

echo "[INFO] Nginx instalado y funcionando en http://192.168.33.10"