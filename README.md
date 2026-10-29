# Titulo del proyecto
 A definir
 ## Descripcion del proyecto 
 (que es, para que, usuarios enfocados)

 ## Dependencias e instalacion 
 - Tener instalado KivyMD, mas adelante otras librerias
    | Dependencia | Versión | Para que se usa |
    | ----------- | ------- | ---------------|
    | Python | 3.13.15 | Ejecutar el programa | 
    | KivyMD | b | Apartado visual | 

    instalacion: 
    
    ```
    python -m venv venv

    .\venv\Scripts\activate 

    pip install --upgrade pip
    pip install kivy

    pip install kivymd

    
## Como levantar el proyecto 
1. Abris la carpeta
2. instalas las dependencias necesarias
3. Abris la terminal dentro de la carpeta
4. inicializas el entorno virtual(venv)
5. Entras en el archivo app.py
6. Ejecutas la aplicacion 

## Estructura de archivos
1. - Carpeta Proyecto
        secciones(bd, clases, home, images, inicio, login, perfil, programadores, registro, venv), app.py, README.md
              Archivo.kv y Archivo.py
    2. A DEFINIR  

## Clase usuario 
La aplicación utiliza la clase *Usuario* ubicada en *clases/usuario.py* para gestionar la lógica de los perfiles:
- **Atributos (__init__)**: nombre, edad, correo y contrasena.
- **datos_completos()**: Verifica que ningún campo esté vacío.
- **correo_valido()**: Comprueba que el correo termine en **@pioix.edu.ar**.
- **nombre_valido()**: Asegura que el nombre tenga solo letras.
- **contrasena_correcta(contrasena)`**: Valida si la contraseña ingresada coincide con la del usuario.


## Estructura de la base de datos 
  - A definir (estructura de la base de datos)
    | Tabla | Columna | Tipo | Descripción |
    | ----- | ------- | ---- | -----------|
    |ejemplo | id | INT | identificador (Clave primaria) |

## Integrantes, materia y división
 - Nicolas Degdeg 
 - Manuel Di Oduardo
 - Manuel Perez
 - Matias Schendel

 **Materia:** Taller de programacion 
 
 **Curso:** 4to B