import tkinter as tk
import json
from tkinter import messagebox
import funcionesJSON

def ventana_proveedores():
    # Paleta de colores
    color_fondo = "#ffa8ff"
    color_texto = "#66a3ff"
    color_salir = "#f50505"

    # Ventana Principal
    ventana_gest_provee = tk.Tk()
    ventana_gest_provee.configure(bg=color_fondo)
    ventana_gest_provee.geometry("1200x500")
    ventana_gest_provee.title("SISTEMA GASTRONOMICO")

    titulosistema = tk.Label(ventana_gest_provee, bg=color_fondo, text="SUS PROVEEDORES", font=("Impact", 25))
    titulosistema.grid(row=0, column=0, columnspan=2, pady=20)

    label_razon_social = tk.Label(ventana_gest_provee, bg=color_fondo, text="Razon Social:", font=("arial", 11, "bold"))
    label_razon_social.grid(row=1, column=0)

    ent_razon_social = tk.Entry(ventana_gest_provee, width=50)
    ent_razon_social.grid(row=1, column=1, padx=20)

    label_precio = tk.Label(ventana_gest_provee, bg=color_fondo, text="CUIT:", font=("arial", 11, "bold"))
    label_precio.grid(row=2, column=0)

    ent_precio = tk.Entry(ventana_gest_provee, width=50)
    ent_precio.grid(row=2, column=1)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="País:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=3, column=0)

    ent_cantidad = tk.Entry(ventana_gest_provee, width=50)
    ent_cantidad.grid(row=3, column=1)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Provincia:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=4, column=0)

    ent_cantidad = tk.Entry(ventana_gest_provee, width=50)
    ent_cantidad.grid(row=4, column=1)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Ciudad:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=5, column=0)

    ent_cantidad = tk.Entry(ventana_gest_provee, width=50)
    ent_cantidad.grid(row=5, column=1)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Dirección:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=6, column=0)

    ent_cantidad = tk.Entry(ventana_gest_provee, width=50)
    ent_cantidad.grid(row=6, column=1)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Número de teléfono:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=7, column=0)

    ent_cantidad = tk.Entry(ventana_gest_provee, width=50)
    ent_cantidad.grid(row=7, column=1)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Correo electrónico:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=8, column=0)

    ent_cantidad = tk.Entry(ventana_gest_provee, width=50)
    ent_cantidad.grid(row=8, column=1)

    boton_agregar = tk.Button(ventana_gest_provee, bg=color_texto, text="Agregar Proveedor", font=("impact",14))
    boton_agregar.grid(row=9, column=1, pady=15)

    boton_agregar = tk.Button(ventana_gest_provee, bg="red", text="Volver", font=("impact",14), command=ventana_gest_provee.destroy)
    boton_agregar.grid(row=9, column=0, pady=15)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Ficha de proveedores:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=1, column=2, padx=40)

    caja_fichaproveedores = tk.Listbox(ventana_gest_provee, width=70, height=20)
    caja_fichaproveedores.grid(row=1, column=3, rowspan=10)

    ventana_gest_provee.mainloop()