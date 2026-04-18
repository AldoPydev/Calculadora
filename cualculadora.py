import tkinter as tk
from tkinter import messagebox


class Calculadora:
    def __init__(self, root):
        self.root = root  # inicializar
        self.root.title("Calculadora")  # Titulo de ventana
        self.root.configure(bg="#2b2b2b")  # color de ventana
        self.root.geometry("375x550")  # tamaño de ventana
        self.root.resizable(False, False)  # Evitar reajuste de ventana

        # Entrada de texto
        self.entrada = tk.Entry(
            root,
            width=17,
            font=("Arial", 28),  # fuente
            borderwidth=0,  # borde
            relief="solid",
            bg="#2b2b2b",  # color de fondo
            fg="white",  # color de texto
            justify="right",  # alineacion
        )

        # GRID de contenido
        self.entrada.grid(
            # atributos para input de entrada
            row=0,
            column=0,
            columnspan=4,
            ipadx=8,
            ipady=10,
            pady=(10, 5),
        )

        # CREAR BOTONES
        self.crear_botones()

    def crear_botones(self):
        botones = [
            # "Caracter", columnas a ocupar
            ("C", 2),
            ("←", 1),
            ("/", 1),
            ("7", 1),
            ("8", 1),
            ("9", 1),
            ("*", 1),
            ("4", 1),
            ("5", 1),
            ("6", 1),
            ("-", 1),
            ("1", 1),
            ("2", 1),
            ("3", 1),
            ("+", 1),
            ("0", 2),
            (".", 1),
            ("=", 1),
        ]

        # Color para los botones
        colores_botones = {
            "numero": "#4d4d4d",
            "operador": "#5a74a1",
            "igual": "#8fb3e2",
            "fondo": "#2b2b2b",
            "texto": "#ffffff",
            "reset": "#31487a",
            "borrar": "#8fb3e2",
        }

        # Contenedor de botones
        frame_botones = tk.Frame(self.root, bg="#2b2b2b")  # color
        frame_botones.grid(row=1, column=0, columnspan=4, pady=(0, 10))  # GRID

        # Ordenar botones
        fila = 0
        columna = 0

        # bucle For para ordenar segun su color
        for (
            boton,
            span,
        ) in (
            botones
        ):  # especificar la cotagoria / los botones relacioandos / el color para los botones
            color_fondo = (
                colores_botones["operador"]
                if boton in ["/", "*", "-", "+", "=", "←"]
                else colores_botones["numero"]
            )
            if boton == "C":
                color_fondo = colores_botones["reset"]
            elif boton == "←":
                color_fondo = colores_botones["borrar"]
            elif boton == "=":
                # especificar el color de acuerdo a los que ya establecimos
                color_fondo = colores_botones["igual"]

            # Propiedades graficas de los botones y de posicionamiento
            tk.Button(
                frame_botones,
                text=boton,
                width=5 * span,
                height=2,
                font=("Arial", 20),
                bg=color_fondo,
                fg=colores_botones["texto"],
                borderwidth=0,
                command=lambda b=boton: self.click_boton(b),
            ).grid(
                row=fila, column=columna, columnspan=span, padx=1, pady=1, sticky="nsew"
            )

            columna += span
            if columna >= 4:
                columna = 0
                fila += 1
        # Configuracion y expansion de columnas y filas dentro de la ventana
        for i in range(4):
            frame_botones.grid_columnconfigure(i, weight=1)
        for i in range(fila + 1):
            frame_botones.grid_rowconfigure(i, weight=1)

    # Crear funcion de click boton / funcion principal para funcionamiento
    def click_boton(self, valor):

        if valor == "=":
            try:  # Manedo de excepciones / error de entrada, dato no vlaido
                resultado = str(eval(self.entrada.get()))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, resultado)
            except Exception as e:
                messagebox.showerror("Error", "Entrada no valida")
                self.entrada.delete(0, tk.END)
        elif valor == "C":
            self.entrada.delete(0, tk.END)  # limpiar input de entrada
        elif valor == "←":
            self.entrada.delete(
                len(self.entrada.get()) - 1, tk.END
            )  # Eliminar lo que se inserto
        else:
            self.entrada.insert(tk.END, valor)


# Ejecutar la aplicacion
if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
