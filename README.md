# ALS-proyecto-Perez-Paramos-Pablo
Esta aplicación es parte del proyecto de la asignatura de Aplicaciones con Lenguajes de Script en 4º año de Ingeniería Informática. La aplicación permite gestionar usuarios, viajes y puntuaciones asociadas a los viajes realizados.

## Características principales
- Gestión de usuarios: permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre los usuarios.
- Gestión de viajes: los usuarios pueden crear viajes especificando información como hora, origen, destino, tiempo estimado y tarifa.
- Apuntarse a viajes: los usuarios pueden apuntarse a viajes creados por otros usuarios.
- Puntuaciones: los usuarios pueden dar puntuaciones a los viajes realizados y a otros usuarios.


## Tecnologías utilizadas

- Backend: Flask, Jinja2 y Sirope.
- Frontend: Boostrap.

## Elementos necesarios para la ejecución del proyecto

 - Python 3.11.3 o superior

 - Flask: instálalo utilizando el siguiente comando en la línea de comandos:
```bash
>pip install flask
```

- Jinja2: instálalo utilizando el siguiente comando en la línea de comandos:
```bash
>pip install jinja2
```

- WSL (Windows Subsystem for Linux): instala una distribución de Linux siguiendo las instrucciones específicas para tu sistema operativo.

- Redis: instálalo utilizando el siguiente comando en la línea de comandos:
```bash
>pip install redis
```

- Flask-login: instálalo utilizando el siguiente comando en la línea de comandos:
```bash
>pip install flask-login
```

## Despliegue
Sigue estos pasos para realizar el despliegue de la aplicación:

1. Abre dos terminales en tu WSL.
2. En la primera terminal, ejecuta el siguiente comando para iniciar el servidor Redis
```bash
>redis-server &
```

3. En la segunda terminal, ejecuta el siguiente comando para acceder a la interfaz de Redis:
```bash
>redis-cli
```

4. En la terminal del sistema operativo, navega hasta la carpeta raíz del proyecto.
5. Luego, ejecuta el siguiente comando para ingresar a la carpeta principal del proyecto:
```bash
>cd .\src\views\main\ 
```

6. Por último, ejecuta el siguiente comando para iniciar la aplicación:
```bash
>flask run
```

La aplicación será desplegada en un servidor local, cuyo enlace nos será dado en la pantalla donde hayamos ejecutado la aplicación.

Una vez realizados estos pasos, la aplicación ya estará desplegada y podremos utilizarla.