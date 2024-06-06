import tkinter as tk
import json
from tkinter import Listbox, messagebox


def ventanaVentas():
    # Paleta de colores
    color_fondo = "#ffa8ff"
    color_texto = "#66a3ff"
    color_salir = "#f50505"


    # Ventana Principal
    ventana_ventas = tk.Tk()
    ventana_ventas.configure(bg=color_fondo)
    ventana_ventas.geometry("1300x700")
    ventana_ventas.title("SISTEMA GASTRONOMICO")

    titulosistema = tk.Label(ventana_ventas, bg=color_fondo, text="Sistema Ventas", font=("Impact", 35))
    titulosistema.place(relx=0.50, rely=0.075, anchor="center")

    # Botones y entradas
    boton_ventas = tk.Button(ventana_ventas, text="Cargar Pedido", width=15, font=("impact",25), bg=color_texto)
    boton_ventas.place(relx= 0.14, rely=0.2, anchor="center")

    boton_ventas = tk.Button(ventana_ventas, text="Modificar Pedido", width=15, font=("impact",25), bg=color_texto)
    boton_ventas.place(relx= 0.38, rely=0.2, anchor="center")

    boton_ventas = tk.Button(ventana_ventas, text="Cancelar Pedido", width=15, font=("impact",25), bg=color_texto)
    boton_ventas.place(relx= 0.63, rely=0.2, anchor="center")

    boton_ventas = tk.Button(ventana_ventas, text="Cerrar Mesa", width=15, font=("impact",25), bg=color_texto)
    boton_ventas.place(relx= 0.87, rely=0.2, anchor="center")

    boton_salir = tk.Button(ventana_ventas, text="Salir",font=("impact",25), bg=color_salir)
    boton_salir.place(relx= 0.040, rely=0.94, anchor="center")

    #LISTBOX 
    label_lista_de_pedido = tk.Label(ventana_ventas, text="LISTA DE PEDIDOS",bg= color_fondo,font=("impact", 20))
    label_lista_de_pedido.place(relx= 0.42, rely= 0.3)

    caja_lista_de_pedido = tk.Listbox(ventana_ventas, height=23, width= 120)
    caja_lista_de_pedido.place(relx=0.23, rely=0.4)

    ventana_ventas.mainloop()