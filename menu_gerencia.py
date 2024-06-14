import tkinter as tk
import json
from tkinter import messagebox
import funcionesJSON
from tkinter import simpledialog
import gerencia
def ventanaMenu_Gerencia():
    def cargar_comida():
        seleccion = caja_productos_t.curselection()
        if seleccion:
            producto_seleccionado = productos[seleccion[0]]
            nombre_producto = producto_seleccionado['nombre']
            precio_producto = producto_seleccionado['precio']
            cantidad_producto = producto_seleccionado['cantidad']
            
            for item in caja_lista_de_menu.get(0, tk.END):
                if nombre_producto in item:
                    messagebox.showwarning("Advertencia", f"El producto '{nombre_producto}' ya ha sido agregado al menú.")
                    return

            comida = {
                'nombre': nombre_producto,
                'precio': precio_producto,
                'cantidad': cantidad_producto
            }
            
            caja_lista_de_menu.insert(tk.END, f"{nombre_producto} --- ${precio_producto}")
            
            menu = funcionesJSON.cargar_menu()  
            menu.append(comida)  
            funcionesJSON.guardar_menu(menu)  
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un producto de la lista antes de cargar comida.")
    def modificar_precio():
        seleccion = caja_lista_de_menu.curselection()
        
        if seleccion:
            comida_seleccionada = menu[seleccion[0]]
            nombre_comida = comida_seleccionada['nombre']
            precio_actual = comida_seleccionada['precio']
            
            nuevo_precio = simpledialog.askfloat("Modificar Precio", f"Ingrese el nuevo precio para {nombre_comida}:", initialvalue=precio_actual)
            
            if nuevo_precio is not None:
                comida_seleccionada['precio'] = nuevo_precio
                
                for producto in productos:
                    if producto['nombre'] == nombre_comida:
                        producto['precio'] = nuevo_precio
                        funcionesJSON.guardar_prod_terminado(productos)
            
                caja_lista_de_menu.delete(seleccion[0])
                caja_lista_de_menu.insert(seleccion[0], f"{nombre_comida} --- ${nuevo_precio}")
                
                funcionesJSON.guardar_menu(menu)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una comida del menú antes de modificar el precio.")

    def eliminar_comida():
        seleccion = caja_lista_de_menu.curselection()
        if seleccion:
            comida_eliminada = menu.pop(seleccion[0])
            caja_lista_de_menu.delete(seleccion[0])
            funcionesJSON.guardar_menu(menu)
            
            messagebox.showinfo("Información", f"La comida '{comida_eliminada['nombre']}' ha sido eliminada del menú.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una comida del menú antes de eliminarla.")

    def volver():
        ventana_menu_comida.destroy()
        gerencia.ventana_gerencial()

    # Paleta de colores
    color_fondo = "#ffa8ff"
    color_texto = "#66a3ff"
    color_salir = "#f50505"

    # Ventana Principal
    ventana_menu_comida = tk.Tk()
    ventana_menu_comida.configure(bg=color_fondo)
    ventana_menu_comida.geometry("1200x700")
    ventana_menu_comida.title("SISTEMA GASTRONOMICO")

    titulosistema = tk.Label(ventana_menu_comida, bg=color_fondo, text="MENÚ", font=("Impact", 25))
    titulosistema.place(relx=0.50, rely=0.075, anchor="center")

    # Botones y entradas
    boton_cargar_comida = tk.Button(ventana_menu_comida, text="Cargar Comida", width=15, font=("impact",14), bg=color_texto, command=cargar_comida)
    boton_cargar_comida.place(relx= 0.5, rely=0.45, anchor="center")

    boton_modificar_comida = tk.Button(ventana_menu_comida, text="Modificar Precio", width=15, font=("impact",14), bg=color_texto, command=modificar_precio)
    boton_modificar_comida.place(relx= 0.5, rely=0.55, anchor="center")

    boton_elim_comida = tk.Button(ventana_menu_comida, text="Eliminar Comida", width=15, font=("impact",14), bg="red", command=eliminar_comida)
    boton_elim_comida.place(relx= 0.5, rely=0.65, anchor="center")

    boton_salir = tk.Button(ventana_menu_comida, text="VOLVER", font=("impact",14), bg=color_salir, command=volver)
    boton_salir.place(relx= 0.040, rely=0.94, anchor="center")

    #LISTBOX 
    label_lista_menu = tk.Label(ventana_menu_comida, text="NUEVO MENÚ:",bg= color_fondo,font=("impact", 14))
    label_lista_menu.place(relx= 0.12, rely= 0.35)

    label_lista_de_comidas = tk.Label(ventana_menu_comida, text="PRODUCTOS DISPONIBLES:",bg= color_fondo,font=("impact", 14))
    label_lista_de_comidas.place(relx= 0.63, rely= 0.35)

    caja_lista_de_menu = tk.Listbox(ventana_menu_comida, width=55, height=20)
    caja_lista_de_menu.place(relx=0.12, rely=0.4)

    caja_productos_t = tk.Listbox(ventana_menu_comida, width=55, height=20)
    caja_productos_t.place(relx=0.63, rely=0.4)

    productos = funcionesJSON.cargar_productos()
    for producto in productos:
        caja_productos_t.insert(tk.END, f"{producto['nombre']} ------------ ${producto['precio']}")

    menu = funcionesJSON.cargar_menu()
    for comida in menu:
        caja_lista_de_menu.insert(tk.END, )

    menu = funcionesJSON.cargar_menu()
    for comida in menu:
        caja_lista_de_menu.insert(tk.END, f"{comida['nombre']} --- ${comida['precio']}")

    ventana_menu_comida.mainloop()
    