import tkinter as tk
from tkinter import messagebox
import re
import json
from funcionesJSON import guardar_prod_terminado, cargar_productos

def ventana_prod_terminado():
    def registrar_prod_t():
        nombre_prod_t = ent_prod.get()
        precio_prod_t = ent_precio.get()
        cantidad_prod_t = ent_cantidad.get()

        if not validar_nombre(nombre_prod_t):
            messagebox.showerror("Error", "El nombre solo puede contener letras y números")
            return
        
        if not validar_numero(precio_prod_t):
            messagebox.showerror("Error", "El precio solo puede contener números")
            return
        
        if not validar_numero(cantidad_prod_t):
            messagebox.showerror("Error", "La cantidad solo puede contener números")
            return
        
        producto = {
            "nombre": nombre_prod_t,
            "precio": float(precio_prod_t),
            "cantidad": int(cantidad_prod_t)
        }

        productos.append(producto)
        guardar_prod_terminado(productos)

        lista_productos_terminados.insert(tk.END, f"{nombre_prod_t} | Precio $: {precio_prod_t} | Cantidad: {cantidad_prod_t}")

        ent_prod.delete(0, tk.END)
        ent_precio.delete(0, tk.END)
        ent_cantidad.delete(0, tk.END)
    
    def validar_nombre(nombre_prod_t):
        return bool(re.match("^[A-Za-z0-9. ]+$", nombre_prod_t))

    def validar_numero(valor):
        return bool(re.match("^[0-9.]+$", valor))

    def modificar_producto():
        try:
            indice_seleccionado = lista_productos_terminados.curselection()[0]
            producto_seleccionado = productos[indice_seleccionado]

            ventana_modificar = tk.Toplevel(ventana_productos_terminados)
            ventana_modificar.title("Modificar Producto")
            ventana_modificar.configure(bg=color_fondo)
            ventana_modificar.geometry("300x300")

            tk.Label(ventana_modificar, text="Ingrese la Modificacion", bg=color_fondo, font=("Impact", 15)).grid(row=0, column=1)

            tk.Label(ventana_modificar, text="Nombre:", bg=color_fondo).grid(row=1, column=0)
            nuevo_nombre = tk.Entry(ventana_modificar)
            nuevo_nombre.grid(row=1, column=1)
            nuevo_nombre.insert(0, producto_seleccionado['nombre'])

            tk.Label(ventana_modificar, text="Precio:", bg=color_fondo).grid(row=2, column=0)
            nuevo_precio = tk.Entry(ventana_modificar)
            nuevo_precio.grid(row=2, column=1)
            nuevo_precio.insert(0, producto_seleccionado['precio'])

            tk.Label(ventana_modificar, text="Cantidad:", bg=color_fondo).grid(row=3, column=0)
            nueva_cantidad = tk.Entry(ventana_modificar)
            nueva_cantidad.grid(row=3, column=1)
            nueva_cantidad.insert(0, producto_seleccionado['cantidad'])

            def guardar_cambios():
                if not validar_nombre(nuevo_nombre.get()):
                    messagebox.showerror("Error", "El nombre solo puede contener letras, números y espacios")
                    return

                if not validar_numero(nuevo_precio.get()):
                    messagebox.showerror("Error", "El precio solo puede contener números")
                    return

                if not validar_numero(nueva_cantidad.get()):
                    messagebox.showerror("Error", "La cantidad solo puede contener números")
                    return

                producto_seleccionado['nombre'] = nuevo_nombre.get()
                producto_seleccionado['precio'] = float(nuevo_precio.get())
                producto_seleccionado['cantidad'] = int(nueva_cantidad.get())

                productos[indice_seleccionado] = producto_seleccionado
                guardar_prod_terminado(productos)
                lista_productos_terminados.delete(indice_seleccionado)
                lista_productos_terminados.insert(indice_seleccionado, f"{producto_seleccionado['nombre']} | Precio $: {producto_seleccionado['precio']} | Cantidad: {producto_seleccionado['cantidad']}")
                ventana_modificar.destroy()
                messagebox.showinfo("Éxito", "Producto modificado correctamente")
            tk.Button(ventana_modificar, text="Guardar", bg=color_texto ,command=guardar_cambios).grid(row=5, column=1)
        
        except IndexError:
            messagebox.showerror("Error", "Seleccione un producto para modificar")

    def modificar_stock():
        try:
            indice_seleccionado = lista_productos_terminados.curselection()[0]
            producto_seleccionado = productos[indice_seleccionado]

            ventana_modificar_stock = tk.Toplevel(ventana_productos_terminados)
            ventana_modificar_stock.title("Modificar Stock")
            ventana_modificar_stock.configure(bg=color_fondo)
            ventana_modificar_stock.geometry("300x150")

            tk.Label(ventana_modificar_stock, text="Ingrese el nuevo Stock", bg=color_fondo, font=("Impact", 15)).grid(row=0, column=1)

            tk.Label(ventana_modificar_stock, text="Cantidad:", bg=color_fondo).grid(row=1, column=0)
            nueva_cantidad = tk.Entry(ventana_modificar_stock)
            nueva_cantidad.grid(row=1, column=1)
            nueva_cantidad.insert(0, producto_seleccionado['cantidad'])

            def guardar_cambios_stock():
                if not validar_numero(nueva_cantidad.get()):
                    messagebox.showerror("Error", "La cantidad solo puede contener números")
                    return
                producto_seleccionado['cantidad'] = int(nueva_cantidad.get())

                productos[indice_seleccionado] = producto_seleccionado
                guardar_prod_terminado(productos)
                lista_productos_terminados.delete(indice_seleccionado)
                lista_productos_terminados.insert(indice_seleccionado, f"{producto_seleccionado['nombre']} | Precio $: {producto_seleccionado['precio']} | Cantidad: {producto_seleccionado['cantidad']}")
                ventana_modificar_stock.destroy()

                messagebox.showinfo("Éxito", "Stock modificado correctamente")

            tk.Button(ventana_modificar_stock, text="Guardar", bg=color_texto, command=guardar_cambios_stock).grid(row=2, column=1)

        except IndexError:
            messagebox.showerror("Error", "Seleccione un producto para modificar el stock")
    
    def eliminar_prod():
        try:
            indice_seleccionado = lista_productos_terminados.curselection()[0]
            producto_eliminado = productos.pop(indice_seleccionado)
            guardar_prod_terminado(productos)
            lista_productos_terminados.delete(indice_seleccionado)
            messagebox.showinfo("Éxito", f"Producto '{producto_eliminado['nombre']}' eliminado correctamente")
        except IndexError:
            messagebox.showerror("Error", "Seleccione un producto para eliminar")


    color_fondo = "#ffa8ff"
    color_texto = "#66a3ff"
    color_salir = "#f50505"

    ventana_productos_terminados = tk.Tk()
    ventana_productos_terminados.configure(bg=color_fondo)
    ventana_productos_terminados.geometry("750x700")
    ventana_productos_terminados.title("Gerencia")

    titulosistema = tk.Label(ventana_productos_terminados, bg=color_fondo, text="PRODUCTOS TERMINADOS", font=("Impact", 25))
    titulosistema.place(relx=0.5, rely=0.10, anchor="center")

    label_prod = tk.Label(ventana_productos_terminados, bg=color_fondo, text="Nombre:")
    label_prod.place(relx=0.33, rely=0.19, anchor="center")

    ent_prod = tk.Entry(ventana_productos_terminados)
    ent_prod.place(relx=0.48, rely=0.19, anchor="center")

    label_precio = tk.Label(ventana_productos_terminados, bg=color_fondo, text="Precio:")
    label_precio.place(relx=0.33, rely=0.23, anchor="center")

    ent_precio = tk.Entry(ventana_productos_terminados)
    ent_precio.place(relx=0.48, rely=0.23, anchor="center")

    label_cantidad = tk.Label(ventana_productos_terminados, bg=color_fondo, text="Cantidad de stock:")
    label_cantidad.place(relx=0.32, rely=0.27, anchor="center")

    ent_cantidad = tk.Entry(ventana_productos_terminados)
    ent_cantidad.place(relx=0.48, rely=0.27, anchor="center")

    label_subtitulo = tk.Label(ventana_productos_terminados, bg=color_fondo, text="PRODUCTOS")
    label_subtitulo.place(relx=0.48, rely=0.45, anchor="center")

    boton_agregar = tk.Button(ventana_productos_terminados, bg=color_texto, text="Agregar Producto", command=registrar_prod_t)
    boton_agregar.place(relx=0.42, rely=0.32)

    lista_productos_terminados = tk.Listbox(ventana_productos_terminados, width=50, height=20)
    lista_productos_terminados.place(relx= 0.48, rely=0.7, anchor="center")

    boton_modificar = tk.Button(ventana_productos_terminados, bg=color_texto, text="Modificar Producto", command=modificar_producto)
    boton_modificar.place(relx=0.70, rely=0.55)

    boton_eliminar = tk.Button(ventana_productos_terminados, bg=color_texto, text="Eliminar Producto", command=eliminar_prod)
    boton_eliminar.place(relx=0.70, rely=0.65)

    boton_modificar_stock = tk.Button(ventana_productos_terminados, bg=color_texto, text="Modificar Stock", command=modificar_stock)
    boton_modificar_stock.place(relx=0.70, rely=0.75)

    boton_salir = tk.Button(ventana_productos_terminados, text="Volver", bg=color_salir, command=ventana_productos_terminados.destroy)
    boton_salir.place(relx= 0.1, rely=0.79, anchor="center")

    productos = cargar_productos()
    for producto in productos:
        lista_productos_terminados.insert(tk.END, f"{producto['nombre']} | Precio $: {producto['precio']} | Cantidad: {producto['cantidad']}")

    ventana_productos_terminados.mainloop()
