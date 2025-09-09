# 🛠️ Primeros pasos: Verificá tu instalación de Docker

Asegurate de tener Docker instalado.  
🔗 **Guía para instalar Docker sin gastar un peso**

## Verificá la instalación con este comando:

```bash
docker --version
```

---

## 🚀 Configurá tu primer contenedor Docker

### Paso 1: Descargar una imagen

Las imágenes son las plantillas base que usamos para crear contenedores.

Descargá la imagen oficial **hello-world**:

```bash
docker pull hello-world
```

### Paso 2: Ejecutar tu primer contenedor

```bash
docker run hello-world
```

---

### ✅ ¿Qué pasa aquí?

- Docker descarga la imagen (si no la tenés localmente).
- Crea un nuevo contenedor basado en esa imagen.
- Ejecuta el contenido y te da un mensaje de confirmación si todo funciona.

---

## 🌐 Probá algo más real: Servidor web con NGINX

1. **Descargá la imagen:**

    ```bash
    docker pull nginx
    ```

2. **Ejecutá el contenedor en background:**

    ```bash
    docker run -d -p 8080:80 --name web-nginx nginx
    ```

    - `-d`: Modo desatendido (en segundo plano).
    - `-p 8080:80`: Expone el puerto 80 del contenedor como 8080 en tu máquina.
    - `--name`: Le da un nombre personalizado al contenedor.

3. **Verificá que funcione**

    Abrí tu navegador y entrá en [http://localhost:8080](http://localhost:8080) 🚀  
    ¡Deberías ver la página por defecto de NGINX!

![Ejecución de NGINX en Docker](img/90DiasDevOps_Dia_2_Semana2.png)

---

## 🔄 Ciclo de vida del contenedor

| Estado   | Qué significa                |
|----------|-----------------------------|
| created  | El contenedor fue creado    |
| running  | Está ejecutándose activamente|
| paused   | Está suspendido             |
| exited   | Finalizó su ejecución       |