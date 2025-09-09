# 🚀 Actividad 1 - Semana2

---

## 💪 **Tarea del Día**

> **Instala Docker siguiendo la guía oficial.**  
> Ejecuta el siguiente comando para probar tu instalación:
>
> ```bash
> docker run hello-world
> ```
>
> Utiliza los comandos `ps`, `images`, `pull`, `run` con alguna imagen como **nginx** o **alpine**.  
> ¡Comparte en el grupo una captura de tu primer contenedor funcionando! 📸

---

## 👋 **¡Hola mundo desde un contenedor!**

Vamos a ejecutar tu primer contenedor con Docker:

```bash
docker run hello-world
```

Esto hace lo siguiente:

1. Descarga una imagen mínima desde Docker Hub.
2. Crea un contenedor basado en esa imagen.
3. Muestra un mensaje de éxito.

Si ves el mensaje: “Hello from Docker!”, todo está funcionando.

---

## 🔍 **Comandos básicos de Docker**

| Acción                     | Comando                |
|----------------------------|------------------------|
| Ver contenedores activos    | `docker ps`            |
| Ver todos los contenedores  | `docker ps -a`         |
| Descargar una imagen        | `docker pull <nombre>` |
| Ejecutar una imagen        | `docker run <nombre>`  |
| Detener un contenedor      | `docker stop <id>`     |
| Eliminar un contenedor     | `docker rm <id>`       |
| Eliminar una imagen        | `docker rmi <id>`      |

---

## 🧩 **Recursos recomendados**

- 📘 [Guía oficial de instalación de Docker](https://docs.docker.com/get-docker/)
- 🐳 [Play with Docker (laboratorio online)](https://labs.play-with-docker.com/)
- 📎 [Cheat Sheet de Docker](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet-esp.pdf)s