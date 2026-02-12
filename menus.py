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
            dic_fun['guardar'](p, "archivos/prestamos.json")
            dic_fun['guardar'](h, "archivos/herramientas.json")
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        if opcion == "0":
            print("Cerrando sistema.....")
            break

