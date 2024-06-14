import tkinter as tk
from tkinter import messagebox
import funcionesJSON 
import re
import os
import json

# Paleta de colores
color_fondo = "#ffa8ff"
color_texto = "#66a3ff"
color_salir = "#f50505"

def es_valido(texto):
    return re.match("^[a-zA-Z0-9]+$", texto) is not None

def cargar_usuarios(archivo):
    try:
        if os.path.exists(archivo):
            with open(archivo, 'r') as file:
                return json.load(file)
        else:
            return []
    except json.JSONDecodeError:
        return []

def usuario_existe(usuario):
    mozos = cargar_usuarios("mozos.json")
    gerentes = cargar_usuarios("gerentes.json")
    return any(u["usuario"] == usuario for u in mozos + gerentes)

def registrar_usuario():
    usuario = nombreUsu.get()
    contrasena = contraUsu.get()
    rol = rol_var.get()

    if not (usuario and contrasena and rol):
        messagebox.showerror("Error de registro", "Todos los campos son obligatorios.")
        return

    if not es_valido(usuario):
        messagebox.showerror("Error de registro", "El nombre de usuario solo debe contener letras y números.")
        return

    if not es_valido(contrasena):
        messagebox.showerror("Error de registro", "La contraseña solo debe contener letras y números.")
        return
    
    if usuario_existe(usuario):
        messagebox.showerror("Error de registro", "El nombre de usuario ya está registrado.")
        return

    if rol == "Mozo":
        funcionesJSON.guardar_mozo(usuario, contrasena)
    elif rol == "Gerente":
        funcionesJSON.guardar_gerente(usuario, contrasena)
        
    messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado correctamente.")
    ventana_registro.destroy()

def ventanaRegistro():
    global ventana_registro, nombreUsu, contraUsu, rol_var

    ventana_registro = tk.Toplevel()
    ventana_registro.configure(bg=color_fondo)
    ventana_registro.geometry("400x400")
    ventana_registro.title("Registro de Usuario")

    titulo = tk.Label(ventana_registro, bg=color_fondo, text="Registro", font=("Impact", 20))
    titulo.place(relx=0.5, rely=0.10, anchor="center")

    etiquetaNombreUsu = tk.Label(ventana_registro, bg=color_fondo, text="USUARIO:")
    etiquetaNombreUsu.place(relx=0.25, rely=0.3, anchor="center")
    nombreUsu = tk.Entry(ventana_registro)
    nombreUsu.place(relx=0.5, rely=0.3, anchor="center")

    etiquetaContraUsu = tk.Label(ventana_registro, bg=color_fondo, text="CONTRASEÑA:")
    etiquetaContraUsu.place(relx=0.22, rely=0.4, anchor="center")
    contraUsu = tk.Entry(ventana_registro, show='*')
    contraUsu.place(relx=0.5, rely=0.4, anchor="center")

    etiquetaRol = tk.Label(ventana_registro, bg=color_fondo, text="ROL:")
    etiquetaRol.place(relx=0.22, rely=0.5, anchor="center")

    rol_var = tk.StringVar(value="Mozo")
    opciones_rol = tk.OptionMenu(ventana_registro, rol_var, "Mozo", "Gerente")
    opciones_rol.place(relx=0.5, rely=0.5, anchor="center")

    boton_registrar = tk.Button(ventana_registro, text="Registrar", font=("impact", 15), bg=color_texto, command=registrar_usuario)
    boton_registrar.place(relx=0.5, rely=0.6, anchor="center")

    ventana_registro.mainloop()
    