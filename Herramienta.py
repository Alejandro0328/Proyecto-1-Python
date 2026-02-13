def agregar_herramientas(herramientas):
    id_h= input("Ingrese el ID de la herramienta: ").strip().upper()
    if id_h in herramientas:
        print("La Herramienta ya existe.....")
        input("Presione cualquier tecla para continuar -->")
        return herramientas
    nombre= input("Nombre de la Herramienta: ").strip().capitalize()
    categoria= input("Categoria de la Herramienta: ").strip().capitalize()
    stock= int(input("Cantida de la Herramienta: "))
    while True:
        estado = input("Estado (Activo/Inactivo/Taller): ").strip().capitalize()
        if estado == "Activo" or estado == "Inactivo" or estado == "Taller":
            break
        print("ERROR: Estado no vaalido por favor ingrese (Activo/Inactivo/Taller) ")
        input("-->")
    valor= float(input("Valor estimado de la Herramienta: "))
    herramientas[id_h] = {
        "nombre":nombre,
        "categoria":categoria,
        "stock": stock,
        "estado": estado,
        "valor": valor
    }
    print("¡Herramienta registrada!")
    return herramientas

def mostrar_herramientas_todas(herramientas):
    if not herramientas:
        print("No hay herramientas")
        return herramientas
    print(f"{'ID':<10}{'Nombre':<30}{'Categoria':<20}{'Stock':<10}{'Estado':<10}")
    print("="*90)

    for id , info in herramientas.items():
        print(f"{id:<10}{info['nombre']:<30}{info['categoria']:<20}{info['stock']:<10}{info['estado']:<10}")
    input("Presione cualquier tecla para continuar -->")

def buscar_herramienta(herramientas):
    while True:
        print("***¿QUE HERRAMIENTA BUSCAS?***")
        herramienta_bus=input("Ingrese el Nombre o Categoria de la Herramienta: ").strip().capitalize()
        encontrado= False
        for id , info in herramientas.items():
            if herramienta_bus in info['nombre']:
                print(f"Encontrado Nombre: {info['nombre']} ID --> {id}")
                encontrado=True
            elif herramienta_bus in info['categoria']:
                print(f"Encontrado Categoria: {info['categoria']}  Nombre: {info['nombre']} ID --> {id}")
                encontrado=True
        if not encontrado:
            print("No hay concidencias encontradas. Intente de nuevo...")
            input("Presione cualquier tecla para continuar -->")
        continuar = input("\nDeseas seguir buscando (Si/No)").strip().capitalize()
        if continuar != "Si":
            break

def actualizar_herramienta(herramientas):
    id_h = input("ID de la Herramienta: ").strip().upper()
    if id_h not in herramientas:
        print("\nEsta Herramienta no existe :(\n")
        input("Presione cualquier tecla para continuar -->")
        return herramientas
    nombre= input("Nombre de la Herramienta: ").strip().capitalize()
    categoria= input("Categoria de la Herramienta: ").strip().capitalize()
    stock= int(input("Cantida de la Herramienta: "))
    estado = input("Estado de la Herramienta: ").strip().capitalize()
    valor= float(input("Valor estimado de la Herramienta: "))
    herramientas[id_h] = {
        "nombre":nombre,
        "categoria":categoria,
        "stock": stock,
        "estado": estado,
        "valor": valor
    }
    print("¡Herramienta Actulizada!")
    return herramientas

def inavilitar_herramienta(herramientas):
    id_h= input ("Ingrese el ID de la Herramienta: ").strip().upper()
    if id_h not in herramientas:
        print("La Herramienta no existe....")
        input("Presione cualquier tecla para continuar -->")
        return herramientas
    print(f"Vas inavilitar: {herramientas[id_h]['nombre']}")
    confirmar = input("¿Estas seguro de INAVILITAR la herramienta? (Si/No)").strip().capitalize()

    if confirmar == "Si":
        herramientas[id_h]['estado'] = "Fuera de servicio"
        herramientas[id_h]['stock'] = 0
        print("Se inavilito la herramienta con exito :) ")
        return herramientas
    else:
        print("Accion cancelada.Vuelva pronto")
        input("-->")
        return herramientas

def eliminar_herramienta(herramientas):
    id_h= input ("Ingrese el ID de la Herramienta: ").strip().upper()
    if id_h not in herramientas:
        print("La Herramienta no existe....")
        input("Presione cualquier tecla para continuar -->")
        return herramientas
    print(f"!Vas a Eliminar¡: {herramientas[id_h]['nombre']}")
    confirmar = input("¿Estas seguro de ELIMINAR la herramienta? (Si/No)").strip().capitalize()

    if confirmar == "Si":
        del herramientas[id_h]
        return herramientas
    else:
        print("Accion cancelada.Vuelva pronto")
        input("-->")
        return herramientas