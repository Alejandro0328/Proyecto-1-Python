def filtro(usuarios):
    id_U=input("Ingrese su ID de usuario: ").strip().upper()
    if id_U not in usuarios:
        print("ID no reconocido. Acceso denegado.")
        return None
    usu_tipo= usuarios[id_U]['tipo']
    if usu_tipo == 'Administrador':
        print(f"\n***BIENVENIDO ADMIN: {usuarios[id_U]['nombre']}***")
    else:
        print(f"\n***BIENVENIDO RESIDENTE: {usuarios[id_U]['nombre']}***")
    return usu_tipo

def menu_ges_herramientas(herramientas,dic_fun):
    while True:
        print("""***GESTION DE HERRAMIENTAS***""")
        print("1. Agregar Herramienta")
        print("2. Actualizar Herramienta")
        print("3. Inavilitar Herramienta")
        print("4. Eliminar Herramienta")
        print("5. Volver")
        opcion=input(("\nSelecione una opcion: "))
        if opcion == "1":
            dic_fun['agregar_h'](herramientas)
        elif opcion == "2":
            dic_fun['actualizar_h'](herramientas)
        elif opcion == "3":
            dic_fun['inavilitar_h'](herramientas)
        elif opcion == "4":
            dic_fun['eliminar_h'](herramientas)    
        elif opcion == "5":
            print ("Saliendo de Gestion de Herramientas.....")
            dic_fun['guardar'](herramientas, "herramientas.json")
            return herramientas
        
def menu_ges_usuarios(usuarios,dic_fun):
    while True:
        print("""***GESTION DE USUARIOS***""")
        print("1. Agregar Usuario")
        print("2. Mostrar Usuarios")
        print("3. Buscar Usuario")
        print("4. Actualizar Usuario")
        print("5. Eliminar Usuario")
        print("6. Volver")
        opcion=input(("\nSelecione una opcion: "))
        if opcion == "1":
            dic_fun['agregar_u'](usuarios)
        elif opcion == "2":
            dic_fun['mostrar_u'](usuarios)
        elif opcion == "3":
            dic_fun['buscar_u'](usuarios)
        elif opcion == "4":
            dic_fun['actualizar_u'](usuarios)
        elif opcion == "5":
            dic_fun['eliminar_u'](usuarios)    
        elif opcion == "6":
            print ("Saliendo de Gestion de Herramientas.....")
            dic_fun['guardar'](usuarios, "usuarios.json")
            return usuarios
        else:
            print ("ERROR.Elija una opcion 1-6")
            input("-->")

        


def menu_principal(usuarios,herramientas,prestamos,dic_fun):
    rol= filtro(usuarios)
    while True:
        print(f"***---MENÚ DE {rol.upper()}---***")
        print("1. Buscar Herramienta")
        print("2. Mostrar todas las herramientas")
        print("3. Solicitar prestamo")

        if rol == 'Administrador':
            print("4. Gestion de Herramienta")
            print("5. Gestion de Usuarios")
            print("6. Ver lista de prestamos")
            print("7. Registrar Devolucion")
            print("0. Salir")
        opcion = input("\nSelecione una Opcion: ")
        if opcion == "1":
            dic_fun['buscar_h'](herramientas)
        elif opcion == "2":
            dic_fun['mostrar_h'](herramientas)
        elif opcion == "3":
            p, h = dic_fun['reg_prestamo'](usuarios,herramientas,prestamos)
            dic_fun['guardar'](p, "prestamos.json")
            dic_fun['guardar'](h, "herramientas.json")
        elif opcion == "4":
            herramientas=menu_ges_herramientas(herramientas,dic_fun)
        elif opcion == "5":
            usuarios =menu_ges_usuarios(usuarios,dic_fun)
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        if opcion == "0":
            print("Cerrando sistema.....")
            break

