import tkinter as tk
from tkinter import messagebox, StringVar
import json
import os

# Definición de los colores
color_fondo = "#ffa8ff"
color_texto = "#66a3ff"
color_salir = "#f50505"
color_listbox = "#a3d5ff"  # Color azul para las Listbox

# Ruta del archivo JSON
archivo_pedidos = "pedidos.json"

def salida_ventana_ventas(ventana):
    ventana.destroy()

def cargar_pedido(caja_lista_de_pedido):
    ventana_cargar = tk.Toplevel()
    ventana_cargar.configure(bg=color_fondo)
    ventana_cargar.geometry("1500x700")
    ventana_cargar.title("Cargar Pedido")

    label_cargar = tk.Label(ventana_cargar, text="Cargar Pedido", bg=color_fondo, font=("Impact", 20))
    label_cargar.place(relx=0.5, rely=0.1, anchor="center")

    # Sección de N° Mesa y Consumo
    label_numero_mesa = tk.Label(ventana_cargar, text="N° Mesa:", bg=color_fondo, font=("Impact", 16))
    label_numero_mesa.place(relx=0.25, rely=0.2, anchor="center")

    opciones_mesa = [str(i) for i in range(1, 11)]
    var_mesa = StringVar(ventana_cargar)
    var_mesa.set(opciones_mesa[0])
    menu_mesa = tk.OptionMenu(ventana_cargar, var_mesa, *opciones_mesa)
    menu_mesa.config(font=("Impact", 15))
    menu_mesa.place(relx=0.33, rely=0.2, anchor="center")

    label_consumicion = tk.Label(ventana_cargar, text="Consumición:", bg=color_fondo, font=("Impact", 16))
    label_consumicion.place(relx=0.13, rely=0.3, anchor="center")

    listbox_consumicion = tk.Listbox(ventana_cargar, font=("Impact", 15), bg=color_listbox, height=10, width=30)
    listbox_consumicion.place(relx=0.3, rely=0.45, anchor="center")

    boton_agregar_consumicion = tk.Button(ventana_cargar, text="Pagar Pedido", font=("Impact", 15), bg=color_texto)
    boton_agregar_consumicion.place(relx=0.3, rely=0.7, anchor="center")
    
    boton_volver = tk.Button(ventana_cargar, text="Volver", font=("Impact", 15), bg=color_texto, command=lambda: salida_ventana_ventas(ventana_cargar))
    boton_volver.place(relx=0.95, rely=0.95, anchor="center")
    # Sección de Menú
    label_menu = tk.Label(ventana_cargar, text="Menú:", bg=color_fondo, font=("Impact", 16))
    label_menu.place(relx=0.75, rely=0.2, anchor="center")

    listbox_menu = tk.Listbox(ventana_cargar, font=("Impact", 15), bg=color_listbox, height=10, width=30)
    listbox_menu.place(relx=0.75, rely=0.45, anchor="center")

    boton_agregar_menu = tk.Button(ventana_cargar, text="Agregar", font=("Impact", 15), bg=color_texto)
    boton_agregar_menu.place(relx=0.75, rely=0.7, anchor="center")

    def agregar_pedido():
        pedido = var_mesa.get()
        if pedido:
            caja_lista_de_pedido.insert(tk.END, pedido)
            guardar_pedidos(caja_lista_de_pedido)
            ventana_cargar.destroy()
        else:
            messagebox.showwarning("Advertencia", "El pedido no puede estar vacío")

    

def modificar_pedido(caja_lista_de_pedido):
    seleccion = caja_lista_de_pedido.curselection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Debe seleccionar un pedido para modificar")
        return

    index = seleccion[0]
    pedido_actual = caja_lista_de_pedido.get(index)

    ventana_modificar = tk.Toplevel()
    ventana_modificar.configure(bg=color_fondo)
    ventana_modificar.geometry("600x400")
    ventana_modificar.title("Modificar Pedido")

    label_modificar = tk.Label(ventana_modificar, text="Modificar Pedido", bg=color_fondo, font=("Impact", 20))
    label_modificar.place(relx=0.5, rely=0.1, anchor="center")

    opciones_mesa = [str(i) for i in range(1, 11)]
    var_mesa = StringVar(ventana_modificar)
    var_mesa.set(pedido_actual)
    menu_mesa = tk.OptionMenu(ventana_modificar, var_mesa, *opciones_mesa)
    menu_mesa.config(font=("Impact", 15))
    menu_mesa.place(relx=0.5, rely=0.3, anchor="center")

    def guardar_cambios():
        nuevo_pedido = var_mesa.get()
        if nuevo_pedido:
            caja_lista_de_pedido.delete(index)
            caja_lista_de_pedido.insert(index, nuevo_pedido)
            guardar_pedidos(caja_lista_de_pedido)
            ventana_modificar.destroy()
        else:
            messagebox.showwarning("Advertencia", "El pedido no puede estar vacío")

    boton_guardar = tk.Button(ventana_modificar, text="Guardar", font=("Impact", 15), bg=color_texto, command=guardar_cambios)
    boton_guardar.place(relx=0.5, rely=0.5, anchor="center")

    listbox_comida = tk.Listbox(ventana_modificar, font=("Impact", 15), bg=color_listbox, height=10, width=30)
    listbox_comida.place(relx=0.5, rely=0.7, anchor="center")

def guardar_pedidos(caja_lista_de_pedido):
    pedidos = caja_lista_de_pedido.get(0, tk.END)
    with open(archivo_pedidos, "w") as file:
        json.dump(pedidos, file)

def cargar_pedidos(caja_lista_de_pedido):
    if os.path.exists(archivo_pedidos):
        with open(archivo_pedidos, "r") as file:
            pedidos = json.load(file)
            for pedido in pedidos:
                caja_lista_de_pedido.insert(tk.END, pedido)

def ventanaVentas():
    ventana_ventas = tk.Toplevel()
    ventana_ventas.configure(bg=color_fondo)
    ventana_ventas.geometry("1300x700")
    ventana_ventas.title("VENTAS")

    titulosistema = tk.Label(ventana_ventas, bg=color_fondo, text="Sistema Ventas", font=("Impact", 35))
    titulosistema.place(relx=0.50, rely=0.075, anchor="center")

    boton_cargar_pedido = tk.Button(ventana_ventas, text="Cargar Pedido", width=15, font=("Impact", 25), bg=color_texto, command=lambda: cargar_pedido(caja_lista_de_pedido))
    boton_cargar_pedido.place(relx=0.14, rely=0.2, anchor="center")

    boton_modificar_pedido = tk.Button(ventana_ventas, text="Modificar Pedido", width=15, font=("Impact", 25), bg=color_texto, command=lambda: modificar_pedido(caja_lista_de_pedido))
    boton_modificar_pedido.place(relx=0.38, rely=0.2, anchor="center")

    boton_cancelar_pedido = tk.Button(ventana_ventas, text="Cancelar Pedido", width=15, font=("Impact", 25), bg=color_texto)
    boton_cancelar_pedido.place(relx=0.63, rely=0.2, anchor="center")

    boton_cerrar_mesa = tk.Button(ventana_ventas, text="Cerrar Mesa", width=15, font=("Impact", 25), bg=color_texto)
    boton_cerrar_mesa.place(relx=0.87, rely=0.2, anchor="center")

    boton_salir = tk.Button(ventana_ventas, text="Salir", font=("Impact", 25), bg=color_salir, command=lambda: salida_ventana_ventas(ventana_ventas))
    boton_salir.place(relx=0.040, rely=0.94, anchor="center")

    label_lista_de_pedido = tk.Label(ventana_ventas, text="LISTA DE PEDIDOS", bg=color_fondo, font=("Impact", 20))
    label_lista_de_pedido.place(relx=0.42, rely=0.3)

    caja_lista_de_pedido = tk.Listbox(ventana_ventas, font=("Impact", 15), bg=color_listbox, width=75, height=14)
    caja_lista_de_pedido.place(relx=0.20, rely=0.4)

    cargar_pedidos(caja_lista_de_pedido)

    ventana_ventas.mainloop()