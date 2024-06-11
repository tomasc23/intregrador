import tkinter as tk
import json
from tkinter import messagebox
import funcionesJSON
import gerencia
import re

def ventana_proveedores():

    def volver():
        ventana_gest_provee.destroy()
        gerencia.ventana_gerencial()

    def validar_datos(razon_social, cuit, pais, provincia, ciudad, direccion, telefono, email):
        if not re.match(r'^[\w\s]+$', razon_social):
            return "La Razón Social solo puede contener letras, números y espacios."
        if not re.match(r'^\d{2}-\d{8}-\d{1}$', cuit):
            return "El CUIT debe tener el formato ##-########-#."
        if not re.match(r'^[a-zA-Z\s]+$', pais):
            return "El País solo puede contener letras y espacios."
        if not re.match(r'^[a-zA-Z\s]+$', provincia):
            return "La Provincia solo puede contener letras y espacios."
        if not re.match(r'^[a-zA-Z\s]+$', ciudad):
            return "La Ciudad solo puede contener letras y espacios."
        if not re.match(r'^[\w\s]+$', direccion):
            return "La Dirección solo puede contener letras y números."
        if not re.match(r'^\d+$', telefono):
            return "El Teléfono solo puede contener números."
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return "El Correo Electrónico no tiene un formato válido."
        return None

    def agregar_proveedor():
        razon_social = ent_razon_social.get()
        cuit = ent_cuit.get()
        pais = ent_pais.get()
        provincia = ent_provincia.get()
        ciudad = ent_ciudad.get()
        direccion = ent_direccion.get()
        telefono = ent_telefono.get()
        email = ent_email.get()

        if not (razon_social and cuit and pais and provincia and ciudad and direccion and telefono and email):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        error = validar_datos(razon_social, cuit, pais, provincia, ciudad, direccion, telefono, email)
        if error:
            messagebox.showerror("Error de validación", error)
            return

        nuevo_proveedor = {
            "razon_social": razon_social,
            "cuit": cuit,
            "pais": pais,
            "provincia": provincia,
            "ciudad": ciudad,
            "direccion": direccion,
            "telefono": telefono,
            "email": email
        }

        proveedores = funcionesJSON.cargar_proveedores()
        proveedores.append(nuevo_proveedor)
        funcionesJSON.guardar_proveedores(proveedores)
        actualizar_listbox()
        limpiar_campos()

    def actualizar_listbox():
        proveedores = funcionesJSON.cargar_proveedores()
        caja_fichaproveedores.delete(0, tk.END)
        for idx, proveedor in enumerate(proveedores, start=1):
            display_text = (f"{idx}. Razón Social: {proveedor['razon_social']}, CUIT: {proveedor['cuit']}, "
                            f"País: {proveedor['pais']}, Provincia: {proveedor['provincia']}, Ciudad: {proveedor['ciudad']}, "
                            f"Dirección: {proveedor['direccion']}, Teléfono: {proveedor['telefono']}, Email: {proveedor['email']}")
            caja_fichaproveedores.insert(tk.END, display_text)

    def limpiar_campos():
        ent_razon_social.delete(0, tk.END)
        ent_cuit.delete(0, tk.END)
        ent_pais.delete(0, tk.END)
        ent_provincia.delete(0, tk.END)
        ent_ciudad.delete(0, tk.END)
        ent_direccion.delete(0, tk.END)
        ent_telefono.delete(0, tk.END)
        ent_email.delete(0, tk.END)

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

    label_cuit = tk.Label(ventana_gest_provee, bg=color_fondo, text="CUIT:", font=("arial", 11, "bold"))
    label_cuit.grid(row=2, column=0)

    ent_cuit = tk.Entry(ventana_gest_provee, width=50)
    ent_cuit.grid(row=2, column=1)

    label_pais = tk.Label(ventana_gest_provee, bg=color_fondo, text="País:", font=("arial", 11, "bold"))
    label_pais.grid(row=3, column=0)

    ent_pais = tk.Entry(ventana_gest_provee, width=50)
    ent_pais.grid(row=3, column=1)

    label_provincia = tk.Label(ventana_gest_provee, bg=color_fondo, text="Provincia:", font=("arial", 11, "bold"))
    label_provincia.grid(row=4, column=0)

    ent_provincia = tk.Entry(ventana_gest_provee, width=50)
    ent_provincia.grid(row=4, column=1)

    label_ciudad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Ciudad:", font=("arial", 11, "bold"))
    label_ciudad.grid(row=5, column=0)

    ent_ciudad = tk.Entry(ventana_gest_provee, width=50)
    ent_ciudad.grid(row=5, column=1)

    label_direccion = tk.Label(ventana_gest_provee, bg=color_fondo, text="Dirección:", font=("arial", 11, "bold"))
    label_direccion.grid(row=6, column=0)

    ent_direccion = tk.Entry(ventana_gest_provee, width=50)
    ent_direccion.grid(row=6, column=1)

    label_telefono = tk.Label(ventana_gest_provee, bg=color_fondo, text="Número de teléfono:", font=("arial", 11, "bold"))
    label_telefono.grid(row=7, column=0)

    ent_telefono = tk.Entry(ventana_gest_provee, width=50)
    ent_telefono.grid(row=7, column=1)

    label_mail = tk.Label(ventana_gest_provee, bg=color_fondo, text="Correo electrónico:", font=("arial", 11, "bold"))
    label_mail.grid(row=8, column=0)

    ent_email = tk.Entry(ventana_gest_provee, width=50)
    ent_email.grid(row=8, column=1)

    boton_agregar = tk.Button(ventana_gest_provee, bg=color_texto, text="Agregar Proveedor", font=("impact",14), command=agregar_proveedor)
    boton_agregar.grid(row=9, column=1, pady=15)

    boton_agregar = tk.Button(ventana_gest_provee, bg="red", text="Volver", font=("impact",14), command=volver)
    boton_agregar.grid(row=9, column=0, pady=15)

    label_cantidad = tk.Label(ventana_gest_provee, bg=color_fondo, text="Ficha de proveedores:", font=("arial", 11, "bold"))
    label_cantidad.grid(row=1, column=2, padx=40)

    frame_listbox = tk.Frame(ventana_gest_provee)
    frame_listbox.grid(row=1, column=3, rowspan=10)

    scrollbar_vertical = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
    scrollbar_horizontal = tk.Scrollbar(frame_listbox, orient=tk.HORIZONTAL)

    caja_fichaproveedores = tk.Listbox(frame_listbox, width=70, height=20, yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
    caja_fichaproveedores.grid(row=0, column=0)

    scrollbar_vertical.config(command=caja_fichaproveedores.yview)
    scrollbar_horizontal.config(command=caja_fichaproveedores.xview)

    scrollbar_vertical.grid(row=0, column=1, sticky='ns')
    scrollbar_horizontal.grid(row=1, column=0, sticky='ew')

    actualizar_listbox()

    ventana_gest_provee.mainloop()