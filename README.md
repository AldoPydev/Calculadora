## Calculadora - Python | Tkinter 

Creando alculadora interactiva con interface de usuario.

![Calculadora]([https://photos.fife.usercontent.google.com/pw/AP1GczM4lJnjahpwx8aprPVPBBc8cWCesvRCGiCTQs2MrDJw8w-bJhfFpgg=w661-h913-s-no?authuser=0](https://github.com/AldoPydev/Calculadora/blob/main/img/00.png?raw=true))

### Paso 1:
Se inicia por importar la librería de Tkinter, así mismo el apartado de messagebox

``` Python
import tkinter as tk
from tkinter import messagebox 
```
Creando la clase principal Calculadora, inicializando la instancia de la clase y el constructor en una función así mismo sus atributos:

- root (incializar)
- title (titulo de aplicación)
- configuracion bg (color de ventana)
- geometry (dimenciones de ventana)
- resizable (bloque el reajuste de ventana)

![Paso1](https://photos.fife.usercontent.google.com/pw/AP1GczNpRrI6qZwkG8rp0rv7jasMr5Yk90KLI8D7FfzsG3YIVIU65_y2xUw=w1420-h710-s-no?authuser=0)

### Paso 2:

Configurando input para la entrada del texto , asiganando al atributo de **self.entrada** realizando la referencia a instancia de clase, colcoando los atributos del input:

- dimenciones
- tipo y tamaño de fuente
- editar bordes
- color de fondo
- color de letra
- alineación de texto 

![Paso2](https://photos.fife.usercontent.google.com/pw/AP1GczP545ncyndSuiSoOEUnHlwEtNauCgEuhS-uPCK8hkZRA70sNJnXB0c=w1228-h710-s-no?authuser=0)

### Paso 3:

Creamos la GRID que contendra y organizara el input de entrada de texto, 
especificando las columnas, filas, padding de contendor y alineación

![Paso3](https://photos.fife.usercontent.google.com/pw/AP1GczNRJ-9XQxVDCkNMxJUONxDqS0k6HT8M9ZEZmbRh1WpapD8l--aA9Pk=w1262-h710-s-no?authuser=0)

### Paso 4:

Creamos los botones de la aplicacion asi como los colores respectivos.

**Botones:**
("C", 2) -> indica el caracter del boton , numero indica el numero de columnas que avarca  

**Colores:**
utilizando un diccionario de datos, se especifica los colores por grupo de los botones: numeros, operadores, fondo. Botones adicionales : signo igual, signo de borrar, reseteo y texto.  

![Paso4](https://photos.fife.usercontent.google.com/pw/AP1GczPBXVTabPyRoOymyFg_FLviKk4hr1QCHk0mXeN1rCQGGqNqZb4vQbM=w993-h913-s-no?authuser=0)

### Paso 5:

Creamos el **frame** de la aplicacion para el contendor y grid de los botones, indicando las columnas y filas así como el espaciado entre estos y el orden que van a seguir. 

![Paso5](https://photos.fife.usercontent.google.com/pw/AP1GczMefq1S5ylMKAkR0sqy1aV8XsinRrnjHSeGH0bA7dVRca8KD00vvAA=w1374-h596-s-no?authuser=0)

### Paso 6:

Con ayuda de un bucle for, ordenamos los botones por su categoria o grupo (los colores que previamente ya establecimos) indicando el grupo y los botones que pertenecen a este.

![Paso6](https://photos.fife.usercontent.google.com/pw/AP1GczPIE9Xu_IxVSCE_w7Ikz1u0-a-NfwhxjbsM9U35t11rX3K7ZPwHKOk=w1195-h913-s-no?authuser=0)

### Paso 7:

Establecemos las propiedades graficas y posicionamiento de los botones con el atributo **Button** (tamaño, tipografia, color de fondo y texto, bordes)

Indicamos el posicionamiento dentro de la GRID por medio de columna y filas.

Creamos la funcion **click_boton** haciendo referencia a la instancia de la clase, esto nos permite capturar el caracter o la operación de acuerdo al botón que presionamos. 

![Paso7](https://photos.fife.usercontent.google.com/pw/AP1GczMoOUEkl1L8HEBR6baJxo0chhrPI1H7Wi_Mu5iOuq4-TU-tN0evm5A=w1318-h913-s-no?authuser=0)

### Paso 8:
### Paso 9:
### Paso 10:
