## Calculadora - Python | Tkinter 

Creando calculadora interactiva con interfaz de usuario.

![Calculadora](https://github.com/AldoPydev/Calculadora/blob/main/img/0.png?raw=true)

### Paso 1:
Se inicia por importar la librería de Tkinter, así mismo el apartado de messagebox

``` Python
import tkinter as tk
from tkinter import messagebox 
```
Creando la clase principal Calculadora, inicializando la instancia de la clase y el constructor en una función así mismo sus atributos:

- root (incializar)
- title (titulo de aplicación)
- configuración bg (color de ventana)
- geometry (dimenciones de ventana)
- resizable (bloque el reajuste de ventana)

![Paso1](https://github.com/AldoPydev/Calculadora/blob/main/img/1.png?raw=true)

### Paso 2:

Configurando input para la entrada del texto, asiganando al atributo de **self.entrada** realizando la referencia a la instancia de clase, y colocando los atributos del input:

- dimenciones
- tipo y tamaño de fuente
- editar bordes
- color de fondo
- color de letra
- alineación de texto 

![Paso2](https://github.com/AldoPydev/Calculadora/blob/main/img/2.png?raw=true)

### Paso 3:

Creamos la GRID que contendra y organizara el input de entrada de texto, 
especificando las columnas, filas, padding de contendor y alineación

![Paso3](https://github.com/AldoPydev/Calculadora/blob/main/img/3.png?raw=true)

### Paso 4:

Creamos los botones de la aplicación así como los colores respectivos.

**Botones:**
("C", 2) -> indica el caracter del boton, indicando el numero de columnas que avarca.  

**Colores:**
utilizando un diccionario de datos, se especifica los colores por grupo de los botones: numeros, operadores, fondo. Botones adicionales : signo igual, signo de borrar, reseteo y texto.  

![Paso4](https://github.com/AldoPydev/Calculadora/blob/main/img/4.png?raw=true)

### Paso 5:

Creamos el **frame** de la aplicacion para el contendor y grid de los botones, indicando las columnas y filas así como el espaciado entre estos y el orden que van a seguir. 

![Paso5](https://github.com/AldoPydev/Calculadora/blob/main/img/5.png?raw=true)

### Paso 6:

Con ayuda de un bucle for, ordenamos los botones por su categoria o grupo (los colores que previamente ya establecimos) indicando el grupo y los botones que pertenecen a este.

![Paso6](https://github.com/AldoPydev/Calculadora/blob/main/img/6.png?raw=true)

### Paso 7:

Establecemos las propiedades graficas y posicionamiento de los botones con el atributo **Button** (tamaño, tipografia, color de fondo y texto, bordes)

Indicamos el posicionamiento dentro de la GRID por medio de columna y filas.

Creamos la funcion **click_boton** haciendo referencia a la instancia de la clase, esto nos permite capturar el caracter o la operación de acuerdo al botón que presionamos. 

![Paso7](https://github.com/AldoPydev/Calculadora/blob/main/img/7.png?raw=true)

### Paso 8:

Utilizamos un for para recorrer las columnas y otro para recorrer las filas y configurar dentro de la ventana. Con ancho de una columna 

![Paso8](https://github.com/AldoPydev/Calculadora/blob/main/img/8.png?raw=true)

### Paso 9:

Creamos la función de **click_boton** la cual resibe el parametro del valor de la entrada. Primeramente manejando un control de excepciones o errores de entrada, en cuyo caso se ingresen datos invaludos o no sea algun caracter de la aplicación. Al aver un error de entrada , se muestra una ventana con el mensaje "Entrada no valida"

Igualmente configuramos la funcionalidad de los botones de reset, borarr y resultado.

En caso de no encontrarse algun error se imprime el resultado de la operación

![Paso9](https://github.com/AldoPydev/Calculadora/blob/main/img/9.png?raw=true)

### Paso 10:

- Indicamos que si el nombre es main la aplicacion se ejecuta, de este modo si utilizamos otras funciones no se ejecutada cuando no lo deseamos
- root es la base de la interfaz en Tkinter, se manda a llamar para abrir la ventana de la aplicación 
- Calculadora(root) está conectando la lógica con la interfaz. Creando una instancia de la clase y pasando el argumento root, para indicar que se abra la ventanada y le asigne todos los elementos

- mainloop() es un bucle infinito que indica la ventana se mantenga abierta hasta que el usuario la cierre. Sin esto, la ventana se abriría y se cerraría al instante.

![Paso10](https://github.com/AldoPydev/Calculadora/blob/main/img/10.png?raw=true)
