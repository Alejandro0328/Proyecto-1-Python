# --- esteriles :) ---

def limpiar_pantalla():
    # Ajustado a 3 saltos para que sea más cómodo visualmente
    print("\n" * 3)

def imprimir_encabezado(titulo):
    ancho = 50
    print("\n" + "╔" + "═" * (ancho-2) + "╗")
    print("║" + titulo.center(ancho-2) + "║")
    print("╚" + "═" * (ancho-2) + "╝")

def filtro(usuarios,dic_fun):
    """Bucle de acceso que permite reintentar si el ID es incorrecto."""
    while True:
        limpiar_pantalla()
        imprimir_encabezado("🔑 ACCESO AL SISTEMA")
        print(" (Escriba 'SALIR' para cerrar el programa)")
        
        id_U = input("\n ➤ Ingrese su ID de usuario: ").strip().upper()
        
        if id_U == "SALIR":
            return None
            
        if id_U in usuarios:
            # Si el ID existe, permite la entrada
            return usuarios[id_U]
        else:
            dic_fun['registrar_error'] (f"ACCESO FALLIDO: ID incorrecto {id_U}")
            print("\n ❌ ID NO RECONOCIDO. Por favor, verifique sus datos.")
            input(" Presione Enter para intentar de nuevo...")

# --- SUBMENÚS ---

# --- menus.py ---

def menu_auditoria(dic_fun):
    """Submenú para que el Administrador consulte los archivos de texto."""
    while True:
        limpiar_pantalla()
        imprimir_encabezado("🔍 CENTRO DE AUDITORÍA Y REGISTROS")
        print(" 1. Ver Historial de Eventos (Éxitos/Actividad)")
        print(" 2. Ver Historial de Errores (Fallos/Validaciones)")
        print(" 0. Volver al Menú Principal")
        print("─" * 50)
        
        op = input("\n ➤ Seleccione una opción: ")
        
        if op == "1":
            dic_fun['ver_eventos']() 
        elif op == "2":
            dic_fun['ver_errores']() 
        elif op == "0":
            break
        else:
            print("⚠️ Opción no válida.")
            input("Presione Enter...")

def menu_ges_herramientas(herramientas, dic_fun):
    while True:
        limpiar_pantalla()
        imprimir_encabezado("🛠️ GESTIÓN DE HERRAMIENTAS")
        print("  1. ➕ Agregar Herramienta")
        print("  2. 🔄 Actualizar Herramienta")
        print("  3. ⚠️  Inhabilitar")
        print("  4. 🗑️  Eliminar")
        print("  5. 🔙 Volver/Guardar")
        print("═" * 50)
        
        opc = input("\n ➤ Opción: ")
        
        if opc == "1": herramientas = dic_fun['agregar_h'](herramientas,dic_fun)
        elif opc == "2": herramientas = dic_fun['actualizar_h'](herramientas,dic_fun)
        elif opc == "3": herramientas = dic_fun['inavilitar_h'](herramientas,dic_fun)
        elif opc == "4": herramientas = dic_fun['eliminar_h'](herramientas,dic_fun)
        elif opc == "5":
            dic_fun['guardar'](herramientas, "herramientas.json")
            return herramientas
        else:
            print("\n ❌ Opción no válida. Intente nuevamente.")
            input(" Enter para continuar...")

def menu_ges_usuarios(usuarios, dic_fun):
    while True:
        limpiar_pantalla()
        imprimir_encabezado("👥 GESTIÓN DE USUARIOS")
        print("  1. 👤 Agregar Usuario")
        print("  2. 📋 Mostrar Usuarios")
        print("  3. 🔍 Buscar Usuario")
        print("  4. 📝 Actualizar Usuario")
        print("  5. ❌ Eliminar Usuario")
        print("  6. 🔙 Volver/Guardar")
        print("═" * 50)

        opc = input("\n ➤ Opción: ")
        
        if opc == "1": usuarios = dic_fun['agregar_u'](usuarios,dic_fun)
        elif opc == "2": dic_fun['mostrar_u'](usuarios)
        elif opc == "3": dic_fun['buscar_u'](usuarios)
        elif opc == "4": usuarios = dic_fun['actualizar_u'](usuarios,dic_fun)
        elif opc == "5": usuarios = dic_fun['eliminar_u'](usuarios,dic_fun)
        elif opc == "6":
            dic_fun['guardar'](usuarios, "usuarios.json")
            return usuarios
        else:
            print("\n ❌ Opción no válida.")
            input(" Enter para continuar...")

def menu_ges_prestamos(prestamos, herramientas, usuario_actual, dic_fun):
    rol = usuario_actual['tipo']
    
    while True:
        limpiar_pantalla()
        imprimir_encabezado("📑 MÓDULO DE PRÉSTAMOS")
        print(f" Rol actual: {rol}")
        print("─" * 50)
        print("  1. 📑 Crear Solicitud de Préstamo")
        print("  2. 📊 Mis Pretamos")
        if rol == 'Administrador':
            print("  3. ✅ Aprobar/Rechazar Solicitudes")
            print("  4. 📥 Registrar Devolución")
            print("  5. 📊 Ver Historial Completo")
        
        print("  0. 🔙 Volver/Guardar")
        print("═" * 50)
        
        opc = input("\n ➤ Opción: ")
        
        if opc == "1":
            prestamos, herramientas = dic_fun['solicitar_p'](usuario_actual, herramientas, prestamos,dic_fun)
        elif opc == "2":
            dic_fun['mis_prestamos'](prestamos,usuario_actual)       
        elif opc == "3" and rol == 'Administrador':
            prestamos, herramientas = dic_fun['gestionar_s'](prestamos, herramientas)
            
        elif opc == "4" and rol == 'Administrador':
            prestamos, herramientas = dic_fun['reg_devolucion'](prestamos, herramientas)
            
        elif opc == "5" and rol == 'Administrador':
            dic_fun['mostrar_p'](prestamos)
            
        elif opc == "0":
            print("\n💾 Guardando cambios en el sistema...")
            dic_fun['guardar'](prestamos, "prestamos.json")
            dic_fun['guardar'](herramientas, "herramientas.json")
            return prestamos, herramientas
        input(" Enter para continuar...")

def menu_reportes(herramientas, prestamos, dic_fun):
    while True:
        limpiar_pantalla()
        imprimir_encabezado("📊 REPORTES Y LOGS")
        print("  1. ⚠️  Stock Bajo")
        print("  2. 📋 Préstamos por Estado")
        print("  3. ⏰ Préstamos VENCIDOS")       
        print("  4. 🔥 Herramientas Populares")
        print("  5. 👥 Usuarios más Activos")       
        print("  6. 📜 Historial de un Usuario")
        print("  7. 📜 Ver Logs del Sistema")
        print("  8. 🔙 Volver / Guardar")
        print("═" * 50)
        
        opc = input("\n ➤ Opción: ")
        
        if opc == "1": 
            dic_fun['rep_stock'](herramientas)
        elif opc == "2": 
            dic_fun['rep_estado'](prestamos)
        elif opc == "3": 
            dic_fun['rep_vencidos'](prestamos)
        elif opc == "4": 
            dic_fun['rep_popular'](prestamos)
        elif opc == "5":
            dic_fun['rep_usuarios'](prestamos)
        elif opc == "6": 
            dic_fun['rep_historial'](prestamos)
        elif opc == "7": 
            dic_fun['ver_logs']()
        elif opc == "8": 
            return
        else:
            print("\n ❌ Opción no válida.")
            input(" Enter para continuar...")

# --- MENÚ PRINCIPAL ---


def menu_principal(usuarios, herramientas, prestamos, dic_fun):
    usuario_sesion = filtro(usuarios, dic_fun)
    if not usuario_sesion: return 

    rol = usuario_sesion['tipo']

    while True:
        limpiar_pantalla()
        imprimir_encabezado(f"💻 MENÚ: {rol.upper()}")
        print(f" Usuario: {usuario_sesion['nombre']} {usuario_sesion['apellido']}")
        print("─" * 50)
        print("  1. 🔍 Buscar Herramienta")
        print("  2. 📦 Mostrar Inventario")
        print("  3. 📑 Módulo de Préstamos")
        print("  4. 👥 Consultar Poseedor (¿Quién la tiene?)")
        print("  5. 📊 Resumen Total del Barrio")

        if rol == 'Administrador':
            print("  6. ⚙️  Gestión de Herramientas")
            print("  7. 👥 Gestión de Usuarios")
            print("  8. 📈 Reportes ")
            print("  9. 📈 Eventos y Errores ") 
        
        print("─" * 50)
        print("  0. 🚪 Salir y Guardar")
        print("═" * 50)

        opcion = input("\n ➤ Seleccione una opción: ")
        
        if opcion == "1": dic_fun['buscar_h'](herramientas)
        elif opcion == "2": dic_fun['mostrar_h'](herramientas)
        elif opcion == "3": 
            prestamos, herramientas = menu_ges_prestamos(prestamos, herramientas, usuario_sesion, dic_fun)
        
        
        elif opcion == "4": dic_fun['consultar_p'](herramientas, prestamos)
        elif opcion == "5": dic_fun['resumen_b'](herramientas, prestamos)
        
        elif opcion == "0": 
            dic_fun['guardar'](usuarios, "usuarios.json")
            dic_fun['guardar'](herramientas, "herramientas.json")
            dic_fun['guardar'](prestamos, "prestamos.json")
            usuario_sesion = filtro(usuarios, dic_fun)
            if not usuario_sesion: return 

            rol = usuario_sesion['tipo']
            
        elif rol == 'Administrador':
            if opcion == "6": herramientas = menu_ges_herramientas(herramientas, dic_fun)
            elif opcion == "7": usuarios = menu_ges_usuarios(usuarios, dic_fun)
            elif opcion == "8": menu_reportes(herramientas, prestamos, dic_fun)
            elif opcion == "9": menu_auditoria(dic_fun)