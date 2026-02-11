def agregar_herramientas(herramientas):
    id_h= input("Ingrese el ID de la herramienta: ").strip().upper()
    if id_h in herramientas:
        print("La Herramienta ya existe.....")
        input("presione cualquier tecla para continuar.......")
        return herramientas
    nombre= input("Nombre de la Herramienta: ").strip().capitalize()
    categoria= input("Categoria de la Herramienta: ").strip().capitalize()
    stock= int(input("Cantida de la Herramienta: "))
    estado = input("Estado de la Herramienta: ").strip().capitalize()
    valor= float(input("Valor estimado de la Herramienta: "))
    herramientas[id_h] = {
        "nombre":nombre,
        "categoria":categoria,
        "cantidad": stock,
        "estado": estado,
        "valor": valor
    }
    print("¡Herramienta registrada!")
    return herramientas

def mostrar_herramientas_todas(herramientas):
    if not herramientas:
        print("No hay herramientas")
        return
    print(f"{'ID Herramienta':<10}{'Nombre':<30}{'Categoria':<20}{'Cantidad':<10}{'Estado':<10}")
    print("="*90)

    for id , info in herramientas.items():
        print(f"{id:<10}{info['nombre']:<30}{info['categoria']:<20}{info['cantidad']:<10}{info['estado']:<10}")
    input("\n\nPresione cualquier tecla para continuar.........")

def buscar_herramienta(herramientas):
    while True:
        print("***¿QUE HERRAMIENTA BUSCAS?***")
        herramienta_bus=input("Ingrese el Nombre o Categoria de la Herramienta: ").strip().capitalize()
        encontrado= False
        for id , info in herramientas.items():
            if herramienta_bus in info['nombre']:
                print(f"Encontrado {info['nombre']} ID --> {id}")
                encontrado=True
            elif herramienta_bus in info['categoria']:
                print(f"Encontrado {info['categoria']}  Nombre: {info['nombre']} ID --> {id}")
                encontrado=True
        if not encontrado:
            print("No hay concidencias encontradas. Intente de nuevo...")
            input("Presione cualquier tecla para continuar -->")
        continuar = input("\nDeseas seguir buscando (Si\No)").strip().capitalize()
        if continuar != "Si":
            break

def actualizar_herramienta(herramientas):
    id_h = input("ID de la Herramienta: ").strip().upper()
    if id_h not in herramientas:
        print("\nEsta Herramienta no existe :(\n")
        input("Presione cualquier tecla para continuar -->")
        return herramientas
    else :
        nombre= input("Nombre de la Herramienta: ").strip().capitalize()
        categoria= input("Categoria de la Herramienta: ").strip().capitalize()
        stock= int(input("Cantida de la Herramienta: "))
        estado = input("Estado de la Herramienta: ").strip().capitalize()
        valor= float(input("Valor estimado de la Herramienta: "))
        herramientas[id_h] = {
            "nombre":nombre,
            "categoria":categoria,
            "cantidad": stock,
            "estado": estado,
            "valor": valor
        }
        print("¡Herramienta Actulizada!")
        return herramientas
