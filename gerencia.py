import tkinter as tk
import json
from tkinter import messagebox
from productos_terminados import ventana_prod_terminado
from menu_gerencia import ventanaMenu_Gerencia
from gestproveedores import ventana_proveedores



def ventana_gerencial():
    # Paleta de colores
    color_fondo = "#ffa8ff"
    color_texto = "#66a3ff"
    color_salir = "#f50505"

    # Ventana Principal
    ventana_gerencia = tk.Tk()
    ventana_gerencia.configure(bg=color_fondo)
    ventana_gerencia.geometry("700x600")
    ventana_gerencia.title("SISTEMA GASTRONOMICO")

    titulosistema = tk.Label(ventana_gerencia, bg=color_fondo, text="Gerencia", font=("Impact", 25))
    titulosistema.place(relx=0.50, rely=0.075, anchor="center")

    # Botones y entradas
    boton_menu = tk.Button(ventana_gerencia, text="Menú", font=("impact",14), bg=color_texto, command=ventanaMenu_Gerencia)
    boton_menu.place(relx= 0.50, rely=0.15, anchor="center")

    boton_inf_compras = tk.Button(ventana_gerencia, text="Informe de compras", font=("impact",14), bg=color_texto)
    boton_inf_compras.place(relx= 0.50, rely=0.35, anchor="center")

    boton_inf_ventas = tk.Button(ventana_gerencia, text="Informe de ventas", font=("impact",14), bg=color_texto)
    boton_inf_ventas.place(relx= 0.50, rely=0.45, anchor="center")

    boton_prod_terminados= tk.Button(ventana_gerencia, text="Productos terminados", font=("impact",14), bg=color_texto, command=ventana_prod_terminado)
    boton_prod_terminados.place(relx= 0.50, rely=0.55, anchor="center")

    boton_proveedores = tk.Button(ventana_gerencia, text="Proveedores", font=("impact",14), bg=color_texto, command=ventana_proveedores)
    boton_proveedores.place(relx= 0.50, rely=0.25, anchor="center")

    boton_salir = tk.Button(ventana_gerencia, text="Salir",font=("impact",14), bg=color_salir, command=ventana_gerencia.destroy)
    boton_salir.place(relx= 0.3, rely=0.75, anchor="center")

    ventana_gerencia.mainloop()