def agregar_Usuario(usuario):
    id_U= input("Ingrese el ID Usuario: ").strip().upper()
    if id_U in usuario:
        print("El Usuario ya existe.....")
        input("Presione cualquier tecla para continuar -->")
        return usuario
    nombre= input("Nombre del Usuario: ").strip().capitalize()
    apellidos= input("Apellidos del Usuario: ").strip().capitalize()
    while True:
        telefono= input("Número de telefono del Usuario: ").strip()
        if  telefono.isdigit() and len(telefono) == 10:
            break
        print ("El número debe ser de 10 Números.")
        input("Presione cualquier tecla para volver intentar ->")
        
    direccion= input("Direccion del usuario: ").strip().capitalize() 
    while True:
        tipo= input("Tipo de usuario(Administrador/Residente)").strip().capitalize()
        if tipo =="Administrador" or tipo== "Residente":
            break
        print("ERROR: Tipo no válido. Por favor ingrese (Administrador/Residente)")
        input("-->")

    usuario[id_U] = {
        "nombre":nombre,
        "apellido":apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }
    print("¡Usuario registradio!")
    return usuario

def mostrar_usuarios(usuarios):
    if not usuarios:
        print("No hay Usuarios")
        return usuarios
    print(f"{'ID Usuario':<10}{'Nombre Completo':<30}{'Telefono':<20}{'Direccion':<10}{'Tipo':<10}")
    print("="*90)

    for id , info in usuarios.items():
        print(f"{id:<10}{info['nombre']+" "+info['apellido']:<30}{info['telefono']:<20}{info['direccion']:<10}{info['tipo']:<10}")
    input("Presione cualquier tecla para continuar -->")

def buscar_usuario(Usuarios):
    while True:
        print("***¿QUE USUARIO BUSCAS?***")
        usuarios_bus=input("Ingrese el Nombre o Tipo de Usuario: ").strip().capitalize()
        encontrado= False
        for id , info in Usuarios.items():
            if usuarios_bus in info['nombre']:
                print(f"Encontrado {info['nombre']} ID --> {id}")
                encontrado=True
            elif usuarios_bus in info['tipo']:
                print(f"Encontrado {info['tipo']}  Nombre: {info['nombre']} ID --> {id}")
                encontrado=True
        if not encontrado:
            print("No hay concidencias encontradas. Intente de nuevo...")
            input("Presione cualquier tecla para continuar -->")
        continuar = input("Deseas seguir buscando (Si/No)").strip().capitalize()
        if continuar != "Si":
            break

def actualizar_usuario(Usuarios):
    id_U = input("ID del Usuario: ").strip().upper()
    if id_U not in Usuarios:
        print("\nEste Usuario no existe :(\n")
        input("Presione cualquier tecla para continuar -->")
        return Usuarios
    nombre= input("Nombre del Usuario: ").strip().capitalize()
    apellidos= input("Apellidos del Usuario: ").strip().capitalize()
    while True:
        telefono= input("Número de telefono del Usuario: ").strip()
        if  telefono.isdigit() and len(telefono) == 10:
            break
        print ("El número debe ser de 10 Números.")
        input("Presione cualquier tecla para volver intentar ->")
        
    direccion= input("Direccion del usuario: ").strip().capitalize() 
    while True:
        tipo= input("Tipo de usuario(Administrador/Residente)").strip().capitalize()
        if tipo =="Administrador" or tipo== "Residente":
            break
        print("ERROR: Tipo no válido. Por favor ingrese (Administrador/Residente)")
        input("-->")
    
    Usuarios[id_U] = {
        "nombre":nombre,
        "apellido":apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }
    print("¡Usuario registradio!")
    return Usuarios

def eliminar_usuario(usuarios):
    id_U= input ("Ingrese el ID del U: ").strip().upper()
    if id_U not in usuarios:
        print("El Usuario no existe....")
        input("Presione cualquier tecla para continuar -->")
        return usuarios
    print(f"!Vas a Eliminar¡: {usuarios[id_U]['nombre']}")
    confirmar = input("¿Estas seguro de ELIMINAR el Usuario? (Si/No)").strip().capitalize()

    if confirmar == "Si":
        del usuarios[id_U]
        print("Usuario eliminado :( ")
        return usuarios
    else:
        print("Accion cancelada.Vuelva pronto")
        input("-->")
        return usuarios