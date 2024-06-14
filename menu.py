import tkinter as tk
import sys
import registroUser
import ventas
import gerencia
import iniciarSesion

# Paleta de colores
color_fondo = "#ffa8ff"
color_texto = "#66a3ff"
color_salir = "#f50505"

def salida_principal():
    sys.exit()

def registroUsuario():
    registroUser.ventanaRegistro()

def ventanaVentas():
    ventana.withdraw()
    def iniciar_ventas():
        ventas.ventanaVentas()
        ventana.deiconify()
    def volver():
        ventana.deiconify()
    iniciarSesion.ventanaSesion("Mozo", iniciar_ventas, volver)

def ventanaGerencia():
    ventana.withdraw()
    def iniciar_gerencia():
        gerencia.ventana_gerencial()
        ventana.deiconify()
    def volver():
        ventana.deiconify()
    iniciarSesion.ventanaSesion("Gerente", iniciar_gerencia, volver)


# Ventana Principal
ventana = tk.Tk()
ventana.configure(bg=color_fondo)
ventana.geometry("1000x700")
ventana.title("SISTEMA GASTRONOMICO")

titulosistema = tk.Label(bg=color_fondo, text="Sistema Gastronomico", font=("Impact", 35))
titulosistema.place(relx=0.5, rely=0.10, anchor="center")

# Botones y entradas
boton_registro = tk.Button(text="Registro", font=("impact", 25), width=15,bg=color_texto, command=registroUsuario)
boton_registro.place(relx=0.5, rely=0.5, anchor="center")

boton_ventas = tk.Button(text="Ventas", font=("impact", 25), width=15, bg=color_texto, command=ventanaVentas)
boton_ventas.place(relx=0.24, rely=0.4, anchor="center")

boton_gestion_gerencial = tk.Button(text="Gestion Gerencial", font=("impact", 25), width=15, bg=color_texto, command=ventanaGerencia)
boton_gestion_gerencial.place(relx=0.76, rely=0.4, anchor="center")

boton_salir = tk.Button(text="Salir", font=("impact", 25), bg=color_salir, command=salida_principal)
boton_salir.place(relx=0.1, rely=0.89, anchor="center")

ventana.mainloop()
