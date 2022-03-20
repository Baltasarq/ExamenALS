# Examen ALS

Plantilla para exámenes de Aplicaciones con Lenguajes de Script.

La respuesta al examen está en **CodigoExamen**:
    
    $ cd CodigoExamen

Cada ejercicio se resolverá en su archivo independiente: el ejercicio 1 en ejercicio1.py, el ejercicio 2 en ejercicio2.py, etc. Una pequeña demostración de la resolución del ejercicio se incluirá en la función main() de cada uno de estos archivos.

Se pueden ejecutar todos los ejercicios con 'python main.py'

    $ python main.py

## Preparación del examen

La primera vez que se ejecute *main.py*, el código preguntará por los datos del usuario. A partir de entonces, solo se ejecutará el código de las respuestas. A continuación se muestra una ejecución de ejemplo. La letra inicial o prefijo del DNI solo se utiliza en DNI's de extranjeros, en otro caso se pulsa simplemente ENTER, al igual que en la pregunta de seguridad sobre si los datos son correctos. Eliminando el archivo `usr_exam_data.json` el programa volverá a ejecutar la petición de datos.

``` 
$ python main.py
Letra prefijo del DNI [-/]: 
DNI (solo dígitos): 12345678
Letra del DNI: D
Nombre: Súper
Apellidos: López
Datos: 12345678D: López, Súper
Es correcto [S]:

Ejercicio 1
-----------

Ejercicio 2
-----------

Ejercicio 3
-----------

Ejercicio 4
-----------

Ejercicio 5
-----------

Examen comprimido en zip en /home/lopez
```

## Entrega

La simple ejecución genera un archivo comprimido en zip en el directorio de escritorio. Nótese que, para que este archivo esté al día, el examen debe al menos comenzar a ejecutarse (no hay errores sintácticos).
