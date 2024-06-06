import tkinter as tk
import json

# Paleta de colores
color_fondo = "#ffa8ff"
color_texto = "#66a3ff"
color_salir = "#f50505"

def ventanaRegistro():
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
    contraUsu = tk.Entry(ventana_registro)
    contraUsu.place(relx=0.5, rely=0.4, anchor="center")

    boton_registrar = tk.Button(ventana_registro, text="Registrar",font=("impact",15), bg=color_texto)
    boton_registrar.place(relx= 0.5, rely=0.5, anchor="center")

    ventana_registro.mainloop()

    