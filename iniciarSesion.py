import tkinter as tk
from tkinter import messagebox
import funcionesJSON 

# Paleta de colores
color_fondo = "#ffa8ff"
color_texto = "#66a3ff"

def validar_credenciales(usuario, contrasena, rol):
    if rol == "Mozo":
        return funcionesJSON.validar_mozo(usuario, contrasena)
    elif rol == "Gerente":
        return funcionesJSON.validar_gerente(usuario, contrasena)
    return False

def iniciar_sesion(rol_requerido):
    usuario = nombreUsu.get()
    contrasena = contraUsu.get()
    rol = rol_var.get()

    if not (usuario and contrasena and rol):
        messagebox.showerror("Error de inicio de sesión", "Todos los campos son obligatorios.")
        return False

    if rol != rol_requerido:
        messagebox.showerror("Error de inicio de sesión", f"Debe ingresar como {rol_requerido}.")
        return False

    if validar_credenciales(usuario, contrasena, rol):
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido {rol}: {usuario}")
        ventana_sesion.destroy()
        return True
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos.")
        return False

def ventanaSesion(rol_requerido, callback_exito, callback_volver):
    global ventana_sesion, nombreUsu, contraUsu, rol_var

    ventana_sesion = tk.Toplevel()
    ventana_sesion.configure(bg=color_fondo)
    ventana_sesion.geometry("400x400")
    ventana_sesion.title("Inicio de Sesión")

    titulo = tk.Label(ventana_sesion, bg=color_fondo, text="Inicio de Sesión", font=("Impact", 20))
    titulo.place(relx=0.5, rely=0.10, anchor="center")

    etiquetaNombreUsu = tk.Label(ventana_sesion, bg=color_fondo, text="USUARIO:", font=("arial", 9, "bold"))
    etiquetaNombreUsu.place(relx=0.24, rely=0.3, anchor="center")
    nombreUsu = tk.Entry(ventana_sesion)
    nombreUsu.place(relx=0.5, rely=0.3, anchor="center")

    etiquetaContraUsu = tk.Label(ventana_sesion, bg=color_fondo, text="CONTRASEÑA:", font=("arial", 9, "bold"))
    etiquetaContraUsu.place(relx=0.21, rely=0.4, anchor="center")
    contraUsu = tk.Entry(ventana_sesion, show='*')
    contraUsu.place(relx=0.5, rely=0.4, anchor="center")

    etiquetaRol = tk.Label(ventana_sesion, bg=color_fondo, text="ROL:", font=("arial", 9, "bold"))
    etiquetaRol.place(relx=0.28, rely=0.5, anchor="center")

    rol_var = tk.StringVar(value=rol_requerido)
    opciones_rol = tk.OptionMenu(ventana_sesion, rol_var, "Mozo", "Gerente")
    opciones_rol.place(relx=0.5, rely=0.5, anchor="center")

    def on_iniciar_sesion():
        if iniciar_sesion(rol_requerido):
            callback_exito()

    boton_iniciar_sesion = tk.Button(ventana_sesion, text="Iniciar Sesión", font=("impact", 15), bg=color_texto, command=on_iniciar_sesion)
    boton_iniciar_sesion.place(relx=0.5, rely=0.6, anchor="center")

    def volver():
        ventana_sesion.destroy()
        callback_volver()

    boton_volver = tk.Button(ventana_sesion, text="Volver", font=("impact", 10), bg="red", command=volver)
    boton_volver.place(relx=0.5, rely=0.75, anchor="center")

    ventana_sesion.mainloop()

