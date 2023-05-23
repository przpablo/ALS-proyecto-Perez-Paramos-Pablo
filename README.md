# ALS-proyecto-Perez-Paramos-Pablo
Esta aplicación es para la asignatura de Aplicacións con linguaxes de script de 4º en Ingeniería Informática. 
Que consta de usuarios (CRUD) que realizan viajes (con una hora, origen, destino, tiempo estimado y tarifa), a los que otros usuarios pueden apuntarse. Los usuarios pueden puntuar un viaje que hayan realizado, a posteriori, y darle así una puntuación al usuario. 

Para esta aplicación se hará uso de Flask, Jinja2 y Sirope para el backend y Bootstrap para el frontend.

## Elementos necesarios para la ejecución del proyecto

## - Python 3.0 o superior

## - Flask
```bash
>pip install flask
```

## - Jinja2
```bash
>pip install jinja2
```

## - WSL
```bash
>wsl --install -d Ubuntu
```

## - Redis
```bash
>pip install redis
```

## - Flask-login
```bash
>pip install flask-login
```

## Despliegue
Para realizar el despliegue se deben realizar los siguientes pasos:

Abrir 2 terminales en WSL, en una de ellas ejecutar el comando:
```bash
>redis-server &
```

En la otra terminal ejecutar el comando:
```bash
>redis-cli
```

Una vez echo todo esto, en la terminal del PC, debemos entrar en primer lugar en la carpeta del proyecto. 
Una vez dentro, ejecutamos el comando:
```bash
>cd .\views\main\ 
```

Y por último, ejecutamos el comando:
```bash
>flask run
```

La aplicación será desplegada en un servidor local, cuyo enlace nos será dado en la pantalla donde hayamos ejecutado la aplicación.

Una vez realizados estos pasos, la aplicación ya estará desplegada y podremos utilizarla.