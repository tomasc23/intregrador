import json
import os
import funcionesJSON
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import gerencia

def ventana_infoventas():
    def cargar_ventas_en_listbox():
        ventas = funcionesJSON.cargar_ventas()
        caja_lista_ventas.delete(0, tk.END)

        total_ventas = 0
        cantidad_ventas = len(ventas)
        contador = 1

        for venta in ventas:
            numero_mesa = venta.get("numero_mesa")
            consumicion = ", ".join(venta.get("consumicion"))
            total = venta.get("total")
            fecha = venta.get("fecha")
            texto_venta = f"{contador}. Mesa {numero_mesa}: Consumición: {consumicion}, Total: ${total}, Fecha: {fecha}"
            caja_lista_ventas.insert(tk.END, texto_venta)
            total_ventas += total
            contador += 1

        etiqueta_suma_total.config(text=f"Suma Total: ${total_ventas}")
        etiqueta_cantidad_ventas.config(text=f"Cantidad de Ventas: {cantidad_ventas}")

    def imprimir_informacion():
        ventas = funcionesJSON.cargar_ventas()
        total_ventas = 0
        ventas_info = []

        for venta in ventas:
            numero_mesa = venta.get("numero_mesa")
            consumicion = ", ".join(venta.get("consumicion"))
            total = venta.get("total")
            fecha = venta.get("fecha")
            texto_venta = f"Mesa {numero_mesa}: Consumición: {consumicion}, Total: ${total}, Fecha: {fecha}"
            ventas_info.append(texto_venta)
            total_ventas += total

        cantidad_ventas = len(ventas)

        ruta_descarga = r"C:\Users\enzot\OneDrive\Escritorio\Lic. Sistemas\2do año\1er cuatrimestre\Programacion II"
        nombre_archivo = "informe_ventas.txt"
        ruta_destino = os.path.join(ruta_descarga, nombre_archivo)

        contador = 1
        while os.path.exists(ruta_destino):
            nombre_archivo = f"informe_ventas_{contador}.txt"
            ruta_destino = os.path.join(ruta_descarga, nombre_archivo)
            contador += 1

        with open(ruta_destino, "w") as archivo:
            archivo.write("Ventas Realizadas:\n\n")
            for venta_info in ventas_info:
                archivo.write(venta_info + "\n")
            
            archivo.write(f"\nTotal de ventas: ${total_ventas}\n")
            archivo.write(f"Cantidad de ventas: {cantidad_ventas}\n")

        messagebox.showinfo("Información", f"Informe de ventas generado correctamente. Se descargó en: {ruta_destino}")
            
    def borrar_venta_seleccionada():
        seleccion = caja_lista_ventas.curselection()
        if seleccion:
            indice = seleccion[0]
            ventas = funcionesJSON.cargar_ventas()
            del ventas[indice]

            funcionesJSON.guardar_ventas(ventas)
            cargar_ventas_en_listbox()
            messagebox.showinfo("Información", "Venta eliminada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una venta para eliminar.")

    def volver():
        ventana_info_ventas.destroy()
        gerencia.ventana_gerencial()

    #Paleta de colores
    color_fondo = "#ffa8ff"
    color_texto = "#66a3ff"
    color_salir = "#f50505"

    #Ventana Principal
    ventana_info_ventas = tk.Tk()
    ventana_info_ventas.configure(bg=color_fondo)
    ventana_info_ventas.geometry("680x770")
    ventana_info_ventas.title("SISTEMA GASTRONOMICO")

    titulodel_sistema = tk.Label(ventana_info_ventas, bg=color_fondo, text="INFORME DE VENTAS", font=("Impact", 25))
    titulodel_sistema.grid(row=0, column=1, columnspan=2, pady=15)

    subtitutlodel_sistema = tk.Label(ventana_info_ventas, bg=color_fondo, text="Ventas Registradas:", font=("Impact", 10))
    subtitutlodel_sistema.grid(row=1, column=0, pady=10)

    caja_lista_ventas = tk.Listbox(ventana_info_ventas, width=70, height=30)
    caja_lista_ventas.grid(row=2, column=1)

    scrollbar_vertical = tk.Scrollbar(ventana_info_ventas, orient="vertical")
    scrollbar_vertical.grid(row=2, column=2, sticky="ns")

    scrollbar_horizontal = tk.Scrollbar(ventana_info_ventas, orient="horizontal")
    scrollbar_horizontal.grid(row=3, column=1, columnspan=2, sticky="ew")

    caja_lista_ventas.config(yscrollcommand=scrollbar_vertical.set)
    caja_lista_ventas.config(xscrollcommand=scrollbar_horizontal.set)

    scrollbar_vertical.config(command=caja_lista_ventas.yview)
    scrollbar_horizontal.config(command=caja_lista_ventas.xview)

    etiqueta_suma_total = tk.Label(ventana_info_ventas, bg=color_fondo, text="", font=("Impact", 12))
    etiqueta_suma_total.grid(row=4, column=1, sticky="w", padx=10, pady=5)

    etiqueta_cantidad_ventas = tk.Label(ventana_info_ventas, bg=color_fondo, text="", font=("Impact", 12))
    etiqueta_cantidad_ventas.grid(row=4, column=1, sticky="e", padx=10, pady=5)

    boton_actualizar = tk.Button(ventana_info_ventas, text="Actualizar Ventas", bg=color_texto, font=("Impact", 12), command=cargar_ventas_en_listbox)
    boton_actualizar.grid(row=5, column=1, pady=10)

    boton_salir = tk.Button(ventana_info_ventas, text="Volver", bg=color_salir, font=("Impact", 12), command=volver)
    boton_salir.grid(row=5, column=0, pady=10)

    boton_imprimir = tk.Button(ventana_info_ventas, text="Imprimir", bg=color_texto, font=("Impact", 12), command=imprimir_informacion)
    boton_imprimir.grid(row=6, column=1, pady=10)

    boton_eliminar = tk.Button(ventana_info_ventas, text="Eliminar Venta", bg=color_salir, font=("Impact", 12), command=borrar_venta_seleccionada)
    boton_eliminar.grid(row=5, column=3, pady=10)

    # Cargar las ventas al inicio
    cargar_ventas_en_listbox()

    ventana_info_ventas.mainloop()

