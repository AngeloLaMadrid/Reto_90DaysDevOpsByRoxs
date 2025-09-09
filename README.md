# Reto_90DaysDevOpsByRoxs
` vagrant destroy && vagrant up `

Detener todos los contenedores:

docker stop $(docker ps -q)
Eliminar todos los contenedores:

docker rm $(docker ps -a -q)