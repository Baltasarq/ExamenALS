# Examen ALS

Plantilla para exámenes de Aplicaciones con Lenguajes de Script.

Cada ejercicio se resolverá en su archivo independiente: el ejercicio 1 en ejercicio1.py, el ejercicio 2 en ejercicio2.py, etc. Una pequeña demostración de la resolución del ejercicio se incluirá en la función main() de cada uno de estos archivos.

Se pueden ejecutar todos los ejercicios con 'python main.py'

## Configuración automática (recomendada)
Ejecuta la herramienta *exam.py* con el parámetro *prep*, y contesta a las preguntas. A continuación, ya puedes abrir  cualquier editor de textos, o un IDE (PyCharm, WingIDE...), que permiten varias comodidas extras como autocompletar, comprobación de errores...

    $ python3 exam.py prep

## Ayudas en la configuración automática
En caso de que surja cualquier problema, será posible obtener la información del usuario tal cual está guardada:

    $ python3 exam.py info

Si es necesario, es posible recomenzar con la información por defecto:

    $ python3 examp.py ini

## Configuración manual
Recuerda, en primer lugar, modificar el nombre del directorio con los ejercicios del examen (**no** el directorio padre, *ExamenALS*), siguiendo el siguiente formato (datos en minúsculas y usando solo caracteres básicos y dígitos).

    <apellido1>_<apellido2>_<nombre>-<dni>

Por ejemplo:

    palotes_gomez_perico-11222333R

Además, debes escribir tus datos personales en el archivo *usr_exam_data.txt*, con el formato:
<pre>
11222333R
Perico Gómez
Palotes
perico@palotes.com
</pre>

## Entrega automatizada (recomendada)
Ejecuta la herramienta *exam.py* con el parámetro *zip*, de forma que se generará un archivo zip ya preparado para la entrega.

    $ python3 exam.py zip

## Entrega manual

En primer lugar, tal y como se indica más arriba, modifica el nombre del directorio que contiene las preguntas del examen con tu dni, apellidos y nombre. No incluyas caracteres más allá de los dígitos y el alfabeto básico. Por ejemplo:

    palotes_gomez_perico-11222333R

Empaqueta el directorio donde se encuentran las preguntas del examen (**no** el directorio padre, *ExamenALS*) en un archivo zip, y entrégalo. Asegúrate de incorporar todos los archivos.

Si se desea hacer en línea de comandos (¡TAB autocompleta los nombres de archivos!):

    $ zip palotes_gomez_perico-11222333R.zip palotes_gomez_perico-11222333R/*
