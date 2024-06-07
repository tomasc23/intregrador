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