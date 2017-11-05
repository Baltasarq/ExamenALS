# Examen ALS

Plantilla para exámenes de Aplicaciones con Lenguajes de Script.

Cada ejercicio se resolverá en su archivo independiente: el ejercicio 1 en ejercicio1.py, el ejercicio 2 en ejercicio2.py, etc. Una pequeña demostración de la resolución del ejercicio se incluirá en la función main() de cada uno de estos archivos.

Se pueden ejecutar todos los ejercicios con 'python main.py'

## Configuración automática (recomendada)
Ejecuta la herramienta *exam.py* con el parámetro *prep*, y contesta a las preguntas. A continuación, ya puedes abrir  MonoDevelop, o Xamarin/Visual Studio.

    $ python3 exam.py prep

## Ayudas en la configuración automática
En caso de que surja cualquier problema, será posible obtener la información del usuario tal cual está guardada:

    $ python3 exam.py info

Si es necesario, es posible recomenzar con la información por defecto:

    $ python3 examp.py ini

## Configuración manual
Recuerda, en primer lugar, modificar el nombre del directorio, siguiendo el formato dado, por los datos en minúsculas y usando solo caracteres básicos y dígitos. Por ejemplo:

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
Empaqueta el directorio donde se encuentran las preguntas del examen en un archivo zip, y entrégalo. Asegúrate de incorporar todos los archivos.


En primer lugar, modifica el nombre del directorio con tu dni, apellidos y nombre. No incluyas caracteres más allá del alfabeto básico. Por ejemplo:

    palotes_gomez_perico-11222333R
