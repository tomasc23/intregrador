import json

usuarioMozo=[]
usuarioGerente=[]

def guardar_usuarioMozo_json():
    with open("registroMozo.json", "w") as archivo:
        json.dump(usuarioMozo, archivo, indent=4)

def cargar_usuarioMozo_json():
    try:
        with open("registroMozo.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
def guardar_usuarioGerente_json():
    with open("registroGerente.json", "w") as archivo:
        json.dump(usuarioGerente, archivo, indent=4)

def cargar_usuarioMozo_json():
    try:
        with open("registroGerente.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []