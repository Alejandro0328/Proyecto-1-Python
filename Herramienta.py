def mostrar_resumen_vecindario(herramientas, prestamos):
    total_bodega = 0
    total_prestado = 0
    
    # Sumamos lo que hay físicamente
    for h in herramientas.values():
        total_bodega += h['stock']
    
    # Sumamos lo que la gente tiene en su casa
    for p in prestamos.values():
        if p['estado'] == "Activo":
            total_prestado += p['cantidad']
            
    print("\n" + "📊" + "─"*38)
    print(" RESUMEN DE ACTIVOS COMUNITARIOS ".center(40))
    print("─"*40)
    print(f"🏠 En la Junta (Disponibles): {total_bodega}")
    print(f"🤝 En casas de vecinos:      {total_prestado}")
    print(f"🌍 TOTAL PROPIEDAD DEL BARRIO: {total_bodega + total_prestado}")
    print("─"*40)
    input("\nPresione Enter...")



def consultar_poseedor(herramientas, prestamos):
    print("\n" + "👥" + "─"*38)
    print(" CONSULTAR POSEEDOR ACTUAL ".center(40))
    print("─"*40)
    
    id_h = input("➤ ID de la Herramienta a rastrear: ").strip().upper()
    
    if id_h in herramientas:
        h = herramientas[id_h]
        print(f"\n🛠️  Herramienta: {h['nombre']}")
        print(f"📦 Stock en bodega: {h['stock']} unidades")
        
        # Buscamos en los préstamos
        encontrado = False
        print("\n📋 Estado de posesión en el barrio:")
        print("─"*40)
        
        for p in prestamos.values():
            # Filtramos por el nombre de la herramienta y que el préstamo esté ACTIVO
            if p['herramienta'] == h['nombre'] and p['estado'] == "Activo":
                print(f"👤 Vecino: {p['usuario']}")
                print(f"   Cant: {p['cantidad']} | Entrega el: {p['fecha_entrega']}")
                print("─"*20)
                encontrado = True
        
        if not encontrado:
            if h['stock'] > 0:
                print("✅ Todas las unidades están disponibles en la junta comunal.")
            else:
                print("⚠️ No hay préstamos activos, pero el stock es 0 (posible reparación).")
    else:
        print("\n❌ ID de herramienta no reconocido.")
    
    input("\nPresione Enter para continuar...")
def agregar_herramientas(herramientas):
    print("\n" + "═"*40)
    print(" ✨ REGISTRAR NUEVA HERRAMIENTA ".center(40))
    print("═"*40)
    
    id_h = input("➤ Ingrese el ID de la herramienta: ").strip().upper()
    if id_h in herramientas:
        print("\n❌ La Herramienta ya existe.....")
        input("Presione Enter para continuar -->")
        return herramientas
        
    nombre = input("➤ Nombre de la Herramienta: ").strip().capitalize()
    categoria = input("➤ Categoria de la Herramienta: ").strip().capitalize()
    
    stock = int(input("➤ Cantidad de la Herramienta: "))
    
    while True:
        estado = input("➤ Estado (Activo/Inactivo/Taller): ").strip().capitalize()
        if estado == "Activo" or estado == "Inactivo" or estado == "Taller":
            break
        print("❌ ERROR: Estado no valido. Ingrese (Activo/Inactivo/Taller)")
        input("-->")
        
    valor = float(input("➤ Valor estimado de la Herramienta: "))
    
    herramientas[id_h] = {
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "estado": estado,
        "valor": valor
    }
    print("\n✅ ¡Herramienta registrada con éxito!")
    return herramientas

def mostrar_herramientas_todas(herramientas):
    print("\n" + "═"*90)
    print(" 📋 LISTADO COMPLETO DE HERRAMIENTAS ".center(90))
    print("═"*90)
    
    if not herramientas:
        print("📭 No hay herramientas registradas.".center(90))
        print("═"*90)
        input("\nPresione Enter para continuar...")
        return herramientas

    print(f"{'ID':<10}{'Nombre':<30}{'Categoria':<20}{'Stock':<10}{'Estado':<10}")
    print("─"*90)

    for id, info in herramientas.items():
        print(f"{id:<10}{info['nombre']:<30}{info['categoria']:<20}{info['stock']:<10}{info['estado']:<10}")
    
    print("═"*90)
    input("\nPresione Enter para continuar -->")

def buscar_herramienta(herramientas):
    while True:
        print("\n" + "🔍" + "─"*38)
        print(" ¿QUÉ HERRAMIENTA BUSCAS? ".center(40))
        print("─"*40)
        
        herramienta_bus = input("➤ Ingrese Nombre o Categoria: ").strip().capitalize()
        encontrado = False
        
        print("\nResultados:")
        print("─"*40)
        for id, info in herramientas.items():
            if herramienta_bus in info['nombre']:
                print(f"✔️ Encontrado Nombre: {info['nombre']} | ID --> {id}")
                encontrado = True
            elif herramienta_bus in info['categoria']:
                print(f"✔️ Encontrado Categoria: {info['categoria']} | Nombre: {info['nombre']} | ID --> {id}")
                encontrado = True
                
        if not encontrado:
            print("❌ No hay coincidencias encontradas.")
        
        print("─"*40)
        continuar = input("\n¿Deseas seguir buscando? (Si/No): ").strip().capitalize()
        if continuar != "Si":
            break

def actualizar_herramienta(herramientas):
    print("\n" + "🔄" + "─"*38)
    print(" ACTUALIZAR HERRAMIENTA ".center(40))
    print("─"*40)
    
    id_h = input("➤ ID de la Herramienta: ").strip().upper()
    if id_h not in herramientas:
        print("\n❌ Esta Herramienta no existe :(")
        input("Presione Enter para continuar -->")
        return herramientas
        
    nombre = input("➤ Nuevo Nombre: ").strip().capitalize()
    categoria = input("➤ Nueva Categoria: ").strip().capitalize()
    stock = int(input("➤ Nueva Cantidad: "))
    estado = input("➤ Nuevo Estado: ").strip().capitalize()
    valor = float(input("➤ Nuevo Valor: "))
    
    herramientas[id_h] = {
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "estado": estado,
        "valor": valor
    }
    print("\n✅ ¡Herramienta Actualizada!")
    input("\nPresione Enter para continuar...")
    return herramientas

def inavilitar_herramienta(herramientas):
    print("\n" + "⚠️" + "─"*38)
    print(" INHABILITAR HERRAMIENTA ".center(40))
    print("─"*40)
    
    id_h = input("➤ Ingrese el ID de la Herramienta: ").strip().upper()
    if id_h not in herramientas:
        print("\n❌ La Herramienta no existe....")
        input("Presione Enter para continuar -->")
        return herramientas
        
    print(f"\n⚠️ Vas a inhabilitar: {herramientas[id_h]['nombre']}")
    confirmar = input("¿Confirmar acción? (Si/No): ").strip().capitalize()

    if confirmar == "Si":
        herramientas[id_h]['estado'] = "Fuera de servicio"
        herramientas[id_h]['stock'] = 0
        print("\n🚫 Se inhabilitó la herramienta con éxito.")
    else:
        print("\n❌ Acción cancelada.")
    
    input("\nPresione Enter para continuar -->")
    return herramientas

def eliminar_herramienta(herramientas):
    print("\n" + "🗑️" + "─"*38)
    print(" ELIMINAR HERRAMIENTA ".center(40))
    print("─"*40)
    
    id_h = input("➤ Ingrese el ID de la Herramienta: ").strip().upper()
    if id_h not in herramientas:
        print("\n❌ La Herramienta no existe....")
        input("Presione Enter para continuar -->")
        return herramientas
        
    print(f"\n❗ ¡VAS A ELIMINAR!: {herramientas[id_h]['nombre']}")
    confirmar = input("¿Estás seguro de ELIMINAR? (Si/No): ").strip().capitalize()

    if confirmar == "Si":
        del herramientas[id_h]
        print("\n✅ Registro eliminado satisfactoriamente.")
    else:
        print("\n❌ Acción cancelada.")
    
    input("\nPresione Enter para continuar -->")
    return herramientas