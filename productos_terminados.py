import tkinter as tk
import sys
from tkinter import messagebox

color_fondo = "#ffa8ff"
color_texto = "#66a3ff"
color_salir = "#f50505"

ventana_productos_terminados = tk.Tk()
ventana_productos_terminados.configure(bg=color_fondo)
ventana_productos_terminados.geometry("750x700")
ventana_productos_terminados.title("Gerencia")

titulosistema = tk.Label(ventana_productos_terminados, bg=color_fondo, text="PRODUCTOS TERMINADOS", font=("Impact", 14))
titulosistema.place(relx=0.5, rely=0.10, anchor="center")

# Botones y entradas

boton_agregar = tk.Button(ventana_productos_terminados, bg=color_texto, text="Agregar Producto")
boton_agregar.place(relx=0.43, rely=0.19)
lista_productos_terminados = tk.Listbox(ventana_productos_terminados, width=50, height=20)
lista_productos_terminados.place(relx= 0.5, rely=0.5, anchor="center")

boton_salir = tk.Button(ventana_productos_terminados, text="Salir", font=("impact",16), bg=color_salir, command=ventana_productos_terminados.destroy)
boton_salir.place(relx= 0.1, rely=0.79, anchor="center")

ventana_productos_terminados.mainloop()