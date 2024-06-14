import tkinter as tk
from tkinter import messagebox, StringVar
import funcionesJSON
import json
import os
from datetime import datetime

# Definición de los colores
color_fondo = "#ffa8ff"
color_texto = "#66a3ff"
color_salir = "#f50505"
color_listbox = "#a3d5ff"

def ventanaVentas():
    #CARGAR PEDIDO
    def cargar_pedido():
        ventana_cargarPedido = tk.Toplevel()
        ventana_cargarPedido.configure(bg=color_fondo)
        ventana_cargarPedido.geometry("1500x700")
        ventana_cargarPedido.title("Cargar Pedido")

        ventana_ventas.withdraw()

        def volver_ventana_ventas():
            ventana_cargarPedido.destroy()
            ventana_ventas.deiconify()

        label_cargar = tk.Label(ventana_cargarPedido, text="Cargar Pedido", bg=color_fondo, font=("Impact", 20))
        label_cargar.place(relx=0.5, rely=0.1, anchor="center")

        label_numero_mesa = tk.Label(ventana_cargarPedido, text="N° Mesa:", bg=color_fondo, font=("Impact", 16))
        label_numero_mesa.place(relx=0.25, rely=0.2, anchor="center")

        opciones_mesa = [str(i) for i in range(1, 11)]
        var_mesa = StringVar(ventana_cargarPedido)
        var_mesa.set(opciones_mesa[0])
        menu_mesa = tk.OptionMenu(ventana_cargarPedido, var_mesa, *opciones_mesa)
        menu_mesa.config(font=("Impact", 15))
        menu_mesa.place(relx=0.33, rely=0.2, anchor="center")

        label_consumicion = tk.Label(ventana_cargarPedido, text="Consumición:", bg=color_fondo, font=("Impact", 16))
        label_consumicion.place(relx=0.10, rely=0.3, anchor="center")

        marco_consumicion = tk.Frame(ventana_cargarPedido)
        marco_consumicion.place(relx=0.3, rely=0.45, anchor="center")

        scrollbar_consumicion = tk.Scrollbar(marco_consumicion, orient=tk.VERTICAL)
        listbox_consumicion = tk.Listbox(marco_consumicion, font=("Impact", 15), bg=color_listbox, height=10, width=40, yscrollcommand=scrollbar_consumicion.set)
        scrollbar_consumicion.config(command=listbox_consumicion.yview)

        scrollbar_consumicion.pack(side=tk.RIGHT, fill=tk.Y)
        listbox_consumicion.pack(side=tk.LEFT, fill=tk.BOTH)

        subtotal = 0.0
        label_subtotal = tk.Label(ventana_cargarPedido, text="Subtotal:", bg=color_fondo, font=("Impact", 16))
        label_subtotal.place(relx=0.3, rely=0.8, anchor="center")
        
        label_subtotal_valor = tk.Label(ventana_cargarPedido, text=f"${subtotal:.2f}", bg=color_fondo, font=("Impact", 16))
        label_subtotal_valor.place(relx=0.4, rely=0.8, anchor="center")

        def agregar_item():
            indice_seleccionado = listbox_menu.curselection()
            if not indice_seleccionado:
                messagebox.showwarning("Advertencia", "Seleccione un item del menú para agregar.")
                return
            item_seleccionado = listbox_menu.get(indice_seleccionado)
            nombre_item = item_seleccionado.split(' --- ')[0]  
            precio = float(item_seleccionado.split(' --- $')[-1]) 
            
            listbox_consumicion.insert(tk.END, nombre_item)
            nonlocal subtotal
            subtotal += precio
            label_subtotal_valor.config(text=f"${subtotal:.2f}")

        def realizar_pedido():
            nonlocal subtotal
            numero_mesa = var_mesa.get()
            items_consumicion = listbox_consumicion.get(0, tk.END)
            
            lista_pedidos = funcionesJSON.cargar_pedidos()
            menu_actualizado = funcionesJSON.cargar_menu()
            productos_actualizados = funcionesJSON.cargar_productos()

            for pedido in lista_pedidos:
                if pedido["numero_mesa"] == numero_mesa:
                    messagebox.showerror("Error", f"Ya hay un pedido registrado para la mesa {numero_mesa}.")
                    return

            for item in items_consumicion:
                for platillo in menu_actualizado:
                    if platillo['nombre'] == item:
                        if platillo['cantidad'] <= 0:
                            messagebox.showerror("Error", f"No hay suficiente stock de {item}. Cantidad disponible: {platillo['cantidad']}. No se puede realizar el pedido. Comuníquese con su proveedor.")
                            return
                        platillo['cantidad'] -= 1
                        break
                for producto in productos_actualizados:
                    if producto['nombre'] == item:
                        if producto['cantidad'] <= 0:
                            messagebox.showerror("Error", f"No hay suficiente stock de {item}. Cantidad disponible: {producto['cantidad']}. No se puede realizar el pedido. Comuníquese con su proveedor.")
                            return
                        producto['cantidad'] -= 1 
                        break
            
            funcionesJSON.guardar_menu(menu_actualizado)
            funcionesJSON.guardar_prod_terminado(productos_actualizados)
            
            pedido = {
                "numero_mesa": numero_mesa,
                "consumicion": list(items_consumicion), 
                "subtotal": subtotal
            }

            lista_pedidos = funcionesJSON.cargar_pedidos()
            lista_pedidos.append(pedido)
            funcionesJSON.guardar_pedidos(lista_pedidos)

            messagebox.showinfo("Pedido Realizado", "El pedido ha sido guardado exitosamente.")
            listbox_consumicion.delete(0, tk.END)
            actualizar_lista_pedidos()
            subtotal = 0.0
            label_subtotal_valor.config(text=f"${subtotal:.2f}")
            ventana_cargarPedido.destroy()
            ventana_ventas.deiconify() 

        #Sección de Menú
        label_menu = tk.Label(ventana_cargarPedido, text="Menú:", bg=color_fondo, font=("Impact", 16))
        label_menu.place(relx=0.75, rely=0.2, anchor="center")

        marco_menu = tk.Frame(ventana_cargarPedido)
        marco_menu.place(relx=0.75, rely=0.45, anchor="center")

        scrollbar_menu = tk.Scrollbar(marco_menu, orient=tk.VERTICAL)
        listbox_menu = tk.Listbox(marco_menu, font=("Impact", 15), bg=color_listbox, height=10, width=40, yscrollcommand=scrollbar_menu.set)
        scrollbar_menu.config(command=listbox_menu.yview)

        scrollbar_menu.pack(side=tk.RIGHT, fill=tk.Y)
        listbox_menu.pack(side=tk.LEFT, fill=tk.BOTH)
        
        menu = funcionesJSON.cargar_menu()
        for item in menu:
            listbox_menu.insert(tk.END, f"{item['nombre']} --- ${item['precio']}")

        boton_agregar_menu = tk.Button(ventana_cargarPedido, text="Agregar", font=("Impact", 15), bg=color_texto, command=agregar_item)
        boton_agregar_menu.place(relx=0.75, rely=0.7, anchor="center")

        boton_agregar_consumicion = tk.Button(ventana_cargarPedido, text="Realizar Pedido", font=("Impact", 15), bg=color_texto, command=realizar_pedido)
        boton_agregar_consumicion.place(relx=0.3, rely=0.7, anchor="center")

        boton_volver = tk.Button(ventana_cargarPedido, text="Volver", font=("Impact", 15), bg="red", command=volver_ventana_ventas)
        boton_volver.place(relx=0.95, rely=0.95, anchor="center")

        actualizar_lista_pedidos()
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    #CANCELAR PEDIDO
    def cancelar_pedido():
        menu = funcionesJSON.cargar_menu()
        productos = funcionesJSON.cargar_productos()
        pedidos = funcionesJSON.cargar_pedidos()
        
        indice_seleccionado = caja_lista_de_pedido.curselection()
        if indice_seleccionado:
            indice = indice_seleccionado[0]
            pedido_seleccionado = pedidos[indice]

            confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro que quieres cancelar el pedido para la mesa {pedido_seleccionado['numero_mesa']}?")

            if confirmacion:
                for consumicion in pedido_seleccionado['consumicion']:
                    nombre_item = consumicion  
                    
                    #Actualizar la cantidad en el menú
                    for item_menu in menu:
                        if item_menu['nombre'] == nombre_item:
                            item_menu['cantidad'] += 1
                            break
                    
                    #Actualizar la cantidad en el inventario de productos
                    for producto in productos:
                        if producto['nombre'] == nombre_item:
                            producto['cantidad'] += 1
                            break

                del pedidos[indice]

                funcionesJSON.guardar_pedidos(pedidos)
                funcionesJSON.guardar_menu(menu)
                funcionesJSON.guardar_prod_terminado(productos)
                actualizar_lista_pedidos()
        else:
            messagebox.showinfo("Advertencia", "Por favor, seleccione un pedido para cancelar.")
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    #CERRAR MESA
    def cerrar_mesa():
        lista_pedidos = funcionesJSON.cargar_pedidos()
        indice_seleccionado = caja_lista_de_pedido.curselection()
        if indice_seleccionado:
            indice = indice_seleccionado[0]
            pedido_seleccionado = lista_pedidos[indice]

            confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro que quieres cerrar la mesa {pedido_seleccionado['numero_mesa']}?")

            if confirmacion:
                numero_mesa = pedido_seleccionado["numero_mesa"]
                consumicion = pedido_seleccionado["consumicion"]
                total = pedido_seleccionado["subtotal"]
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                venta = {
                    "numero_mesa": numero_mesa,
                    "consumicion": consumicion,
                    "total": total,
                    "fecha": fecha
                }

                lista_ventas = funcionesJSON.cargar_ventas()
                lista_ventas.append(venta)
                funcionesJSON.guardar_ventas(lista_ventas)

                del lista_pedidos[indice]
                funcionesJSON.guardar_pedidos(lista_pedidos)

                actualizar_lista_pedidos()
                messagebox.showinfo("Mesa Cerrada", f"La mesa {numero_mesa} ha sido cerrada. Total de la venta: ${total:.2f}.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un pedido de la lista para cerrar la mesa.")
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    def modificar_pedido():
        pedidos = funcionesJSON.cargar_pedidos()
        indice_seleccionado = caja_lista_de_pedido.curselection()
        if indice_seleccionado:
            indice = indice_seleccionado[0]
            pedido_seleccionado = pedidos[indice]

            ventana_modificar_pedido = tk.Toplevel()
            ventana_modificar_pedido.configure(bg=color_fondo)
            ventana_modificar_pedido.geometry("1500x700")
            ventana_modificar_pedido.title("Modificar Pedido")

            ventana_ventas.withdraw()

            def confirmar_modificacion():
                respuesta = messagebox.askyesno("Confirmar Modificación", "¿Está seguro de que desea modificar este pedido?")
                if respuesta:
                    nueva_mesa = var_mesa.get()
                    nueva_consumicion = listbox_consumicion.get(0, tk.END)
                    nuevo_subtotal = subtotal

                    nuevas_comidas_agregadas = []

                    comidas_originales = pedido_seleccionado["consumicion"]

                    for nueva_comida in nueva_consumicion:
                        if nueva_comida not in comidas_originales:
                            nuevas_comidas_agregadas.append(nueva_comida)

                    pedido_seleccionado["numero_mesa"] = nueva_mesa
                    pedido_seleccionado["consumicion"] = nueva_consumicion
                    pedido_seleccionado["subtotal"] = nuevo_subtotal

                    pedidos[indice] = pedido_seleccionado
                    funcionesJSON.guardar_pedidos(pedidos)

                    menu_actualizado = funcionesJSON.cargar_menu()
                    productos_actualizados = funcionesJSON.cargar_productos()

                    for nueva_comida in nuevas_comidas_agregadas:
                        for platillo in menu_actualizado:
                            if platillo['nombre'] == nueva_comida:
                                if platillo['cantidad'] <= 0:
                                    messagebox.showerror("Error", f"No hay suficiente stock de {nueva_comida}. Cantidad disponible: {platillo['cantidad']}. No se puede realizar el pedido. Comuníquese con su proveedor.")
                                    return
                                platillo['cantidad'] -= 1  #restar una unidad al platillo consumido
                                break
                        for producto in productos_actualizados:
                            if producto['nombre'] == nueva_comida:
                                if producto['cantidad'] <= 0:
                                    messagebox.showerror("Error", f"No hay suficiente stock de {nueva_comida}. Cantidad disponible: {producto['cantidad']}. No se puede realizar el pedido. Comuníquese con su proveedor.")
                                    return
                                producto['cantidad'] -= 1  #rstar una unidad al producto consumido
                                break
                    
                    funcionesJSON.guardar_menu(menu_actualizado)
                    funcionesJSON.guardar_prod_terminado(productos_actualizados)
                    actualizar_lista_pedidos()
                    messagebox.showinfo("Éxito", "Pedido modificado exitosamente.")
                    ventana_modificar_pedido.destroy()
                    ventana_ventas.deiconify()

            def volver_ventana_ventas():
                ventana_modificar_pedido.destroy()
                ventana_ventas.deiconify()

            label_modificar = tk.Label(ventana_modificar_pedido, text="Modificar Pedido", bg=color_fondo, font=("Impact", 20))
            label_modificar.place(relx=0.5, rely=0.1, anchor="center")

            label_numero_mesa = tk.Label(ventana_modificar_pedido, text="N° Mesa:", bg=color_fondo, font=("Impact", 16))
            label_numero_mesa.place(relx=0.25, rely=0.2, anchor="center")

            opciones_mesa = [str(i) for i in range(1, 11)]
            var_mesa = StringVar(ventana_modificar_pedido)
            var_mesa.set(pedido_seleccionado["numero_mesa"])
            menu_mesa = tk.OptionMenu(ventana_modificar_pedido, var_mesa, *opciones_mesa)
            menu_mesa.config(font=("Impact", 15))
            menu_mesa.place(relx=0.33, rely=0.2, anchor="center")

            label_consumicion = tk.Label(ventana_modificar_pedido, text="Consumición:", bg=color_fondo, font=("Impact", 16))
            label_consumicion.place(relx=0.10, rely=0.3, anchor="center")

            marco_consumicion = tk.Frame(ventana_modificar_pedido)
            marco_consumicion.place(relx=0.3, rely=0.45, anchor="center")

            scrollbar_consumicion = tk.Scrollbar(marco_consumicion, orient=tk.VERTICAL)
            listbox_consumicion = tk.Listbox(marco_consumicion, font=("Impact", 15), bg=color_listbox, height=10, width=40, yscrollcommand=scrollbar_consumicion.set)
            scrollbar_consumicion.config(command=listbox_consumicion.yview)

            scrollbar_consumicion.pack(side=tk.RIGHT, fill=tk.Y)
            listbox_consumicion.pack(side=tk.LEFT, fill=tk.BOTH)

            subtotal = pedido_seleccionado["subtotal"]
            label_subtotal = tk.Label(ventana_modificar_pedido, text="Subtotal:", bg=color_fondo, font=("Impact", 16))
            label_subtotal.place(relx=0.3, rely=0.8, anchor="center")

            label_subtotal_valor = tk.Label(ventana_modificar_pedido, text=f"${subtotal:.2f}", bg=color_fondo, font=("Impact", 16))
            label_subtotal_valor.place(relx=0.4, rely=0.8, anchor="center")

            def agregar_item():
                indice_seleccionado = listbox_menu.curselection()
                if not indice_seleccionado:
                    messagebox.showwarning("Advertencia", "Seleccione un item del menú para agregar.")
                    return
                item_seleccionado = listbox_menu.get(indice_seleccionado)
                nombre_item = item_seleccionado.split(' --- ')[0]
                precio = float(item_seleccionado.split(' --- $')[-1])

                listbox_consumicion.insert(tk.END, nombre_item)
                nonlocal subtotal
                subtotal += precio
                label_subtotal_valor.config(text=f"${subtotal:.2f}")

            label_menu = tk.Label(ventana_modificar_pedido, text="Menú:", bg=color_fondo, font=("Impact", 16))
            label_menu.place(relx=0.75, rely=0.2, anchor="center")
            marco_menu = tk.Frame(ventana_modificar_pedido)
            marco_menu.place(relx=0.75, rely=0.45, anchor="center")

            scrollbar_menu = tk.Scrollbar(marco_menu, orient=tk.VERTICAL)
            listbox_menu = tk.Listbox(marco_menu, font=("Impact", 15), bg=color_listbox, height=10, width=40, yscrollcommand=scrollbar_menu.set)
            scrollbar_menu.config(command=listbox_menu.yview)

            scrollbar_menu.pack(side=tk.RIGHT, fill=tk.Y)
            listbox_menu.pack(side=tk.LEFT, fill=tk.BOTH)

            menu = funcionesJSON.cargar_menu()
            for item in menu:
                listbox_menu.insert(tk.END, f"{item['nombre']} --- ${item['precio']}")

            for comida in pedido_seleccionado["consumicion"]:
                listbox_consumicion.insert(tk.END, comida)

            boton_agregar_menu = tk.Button(ventana_modificar_pedido, text="Agregar", font=("Impact", 15), bg=color_texto, command=agregar_item)
            boton_agregar_menu.place(relx=0.75, rely=0.7, anchor="center")

            boton_confirmar_modificacion = tk.Button(ventana_modificar_pedido, text="Confirmar Modificación", font=("Impact", 15), bg=color_texto, command=confirmar_modificacion)
            boton_confirmar_modificacion.place(relx=0.3, rely=0.7, anchor="center")

            boton_volver = tk.Button(ventana_modificar_pedido, text="Volver", font=("Impact", 15), bg="red", command=volver_ventana_ventas)
            boton_volver.place(relx=0.95, rely=0.95, anchor="center")
        else:
            messagebox.showinfo("Advertencia", "Por favor, seleccione un pedido para modificar.")
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #VENTANA DE VENTAS
    def actualizar_lista_pedidos():
        caja_lista_de_pedido.delete(0, tk.END)
        lista_pedidos = funcionesJSON.cargar_pedidos()
        for pedido in lista_pedidos:
            numero_mesa = pedido["numero_mesa"]
            consumiciones = ", ".join(pedido["consumicion"])
            subtotal = pedido["subtotal"]
            caja_lista_de_pedido.insert(tk.END, f"Mesa {numero_mesa}: Consumición: {consumiciones}, Subtotal: ${subtotal}")

    pedidos = funcionesJSON.cargar_pedidos()
    ventana_ventas = tk.Toplevel()
    ventana_ventas.configure(bg=color_fondo)
    ventana_ventas.geometry("1300x700")
    ventana_ventas.title("VENTAS")

    titulosistema = tk.Label(ventana_ventas, bg=color_fondo, text="Sistema Ventas", font=("Impact", 35))
    titulosistema.place(relx=0.50, rely=0.075, anchor="center")

    boton_cargar_pedido = tk.Button(ventana_ventas, text="Cargar Pedido", width=15, font=("Impact", 20), bg=color_texto, command=cargar_pedido)
    boton_cargar_pedido.place(relx=0.14, rely=0.2, anchor="center")

    boton_modificar_pedido = tk.Button(ventana_ventas, text="Modificar Pedido", width=15, font=("Impact", 20), bg=color_texto, command=modificar_pedido)
    boton_modificar_pedido.place(relx=0.38, rely=0.2, anchor="center")

    boton_cancelar_pedido = tk.Button(ventana_ventas, text="Cancelar Pedido", width=15, font=("Impact", 20), bg=color_texto, command=cancelar_pedido)
    boton_cancelar_pedido.place(relx=0.63, rely=0.2, anchor="center")

    boton_cerrar_mesa = tk.Button(ventana_ventas, text="Cerrar Mesa", width=15, font=("Impact", 20), bg=color_texto, command=cerrar_mesa)
    boton_cerrar_mesa.place(relx=0.87, rely=0.2, anchor="center")

    boton_salir = tk.Button(ventana_ventas, text="Salir", font=("Impact", 20), bg=color_salir, command=ventana_ventas.destroy)
    boton_salir.place(relx=0.040, rely=0.94, anchor="center")

    label_lista_de_pedido = tk.Label(ventana_ventas, text="Lista de Pedidos:", bg=color_fondo, font=("Impact", 20))
    label_lista_de_pedido.place(relx=0.2, rely=0.34)

    frame_pedidos = tk.Frame(ventana_ventas)
    frame_pedidos.place(relx=0.5, rely=0.6, anchor="center")

    scrollbar_pedidos_y = tk.Scrollbar(frame_pedidos, orient=tk.VERTICAL)
    scrollbar_pedidos_x = tk.Scrollbar(frame_pedidos, orient=tk.HORIZONTAL)

    caja_lista_de_pedido = tk.Listbox(frame_pedidos, font=("Impact", 10), bg=color_listbox, yscrollcommand=scrollbar_pedidos_y.set, xscrollcommand=scrollbar_pedidos_x.set, width=112, height=20)
    scrollbar_pedidos_y.config(command=caja_lista_de_pedido.yview)
    scrollbar_pedidos_x.config(command=caja_lista_de_pedido.xview)

    scrollbar_pedidos_x.pack(side=tk.BOTTOM, fill=tk.X)
    scrollbar_pedidos_y.pack(side=tk.RIGHT, fill=tk.Y)
    caja_lista_de_pedido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    actualizar_lista_pedidos()

    ventana_ventas.mainloop()