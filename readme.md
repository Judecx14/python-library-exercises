# Ejercicios de Selenuim Python

A continuación se muestran dos ejercicios realizados en Python para la materia Extracción de Conocimiento en Bases de Datos. Dichos ejercicios constan de automatizar tareas haciendo uso de la librería Selenuim. El primer ejercicio consta en tomar la información de una tabla que se este actualizando constantemente, realizar una cuatro lecturas y graficar dichos datos, ademas de crear un archivo csv.

# Archivos

La esctuctura del proyecto es simple, se cuenta con una carpeta de contine las clases utilizadas para el proyecto, así como una carpeta de configuración que contine el archivo que realiza la configuración del navegador. Tambien se cuenta con una carpeta de constantes que contiene clases enumeradas que sirven para hacer uso de constantes en el proyecto. Por ultimo se tiene una dos carpetas, la primera es la carpeta de recursos que contiene un archivo json que sirve para configurar la aplicación así como otra carpeta app donde estan los archivos necesarios para cada ejercicio.

# Configuración

Para configurar la aplicación es necesario realizarlo desde el archivo **settings.json**, que se encuentra en la carpeta **resources**. Dentro de este archivo se tendrán dos opciones

- La primera opción contiene la llave **options** dentro de esta llave se tiene un objeto.
	> En dicho objeto se tendrán opciones como, maximizar pantalla, modo de busqueda, el enlace de la pagina, etc.

- La segunda opción **elements** contiene un arreglo de objetos.
	> Dentro de este arreglo se deberán colocar los elementos con los que se desea interactuar, dicho objeto contiene caracteristicas como el tipo, el valor, la acción, etc.

# Correr aplicación

Para correr la aplicación es necesario realizarlo desde dentro de la carpeta **source** en caso de que suceda un error.

- Debera entrar a la carpeta **source** desde la consola despues ejecutar de nuevo el programa.
	> cd source