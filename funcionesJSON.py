import json
import os

def guardar_mozo(usuario, contrasena):
    nuevo_mozo = {'usuario': usuario, 'contrasena': contrasena}
    if os.path.exists("mozos.json"):
        with open("mozos.json", 'r') as archivo:
            mozos = json.load(archivo)
    else:
        mozos = []
    mozos.append(nuevo_mozo)
    with open("mozos.json", 'w') as archivo:
        json.dump(mozos, archivo, indent=4)

def guardar_gerente(usuario, contrasena):
    nuevo_gerente = {'usuario': usuario, 'contrasena': contrasena}
    if os.path.exists("gerentes.json"):
        with open("gerentes.json", 'r') as archivo:
            gerentes = json.load(archivo)
    else:
        gerentes = []
    gerentes.append(nuevo_gerente)
    with open("gerentes.json", 'w') as archivo:
        json.dump(gerentes, archivo, indent=4)

def validar_mozo(usuario, contrasena):
    if os.path.exists("mozos.json"):
        with open("mozos.json", 'r') as archivo:
            mozos = json.load(archivo)
            for mozo in mozos:
                if mozo['usuario'] == usuario and mozo['contrasena'] == contrasena:
                    return True
    return False

def validar_gerente(usuario, contrasena):
    if os.path.exists("gerentes.json"):
        with open("gerentes.json", 'r') as archivo:
            gerentes = json.load(archivo)
            for gerente in gerentes:
                if gerente['usuario'] == usuario and gerente['contrasena'] == contrasena:
                    return True
    return False

def guardar_prod_terminado(productos, archivo='productos.json'):
    with open(archivo, 'w') as file:
        json.dump(productos, file, indent=4)

def cargar_productos(archivo='productos.json'):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]
    

ARCHIVO_MENU = 'menu.json'
def guardar_menu(menu):
    with open(ARCHIVO_MENU, 'w') as file:
        json.dump(menu, file, indent=4)

def cargar_menu():
    try:
        with open(ARCHIVO_MENU, 'r') as file:
            menu = json.load(file)
            # Cargar la cantidad y el precio del archivo de productos
            productos = cargar_productos()
            for comida in menu:
                for producto in productos:
                    if comida['nombre'] == producto['nombre']:
                        comida['cantidad'] = producto['cantidad']
                        comida['precio'] = producto['precio']
            return menu
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []