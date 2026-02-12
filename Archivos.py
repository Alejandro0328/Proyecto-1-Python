import json
def cargar_datos(nom_archivo):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}

def guardar_datos(datos, nom_archivo):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch,indent=4)
    except Exception as e:
        print(f"Error al guardar: {e}")