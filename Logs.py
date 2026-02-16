def registrar_evento(mensaje):
    """
    Guarda un evento en el archivo logs.txt. 
    """
    # Creamos la línea del evento
    linea = f" EVENTO: {mensaje}\n"
    
    try:
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except:
        pass

def ver_logs():
    """
    Muestra el historial de errores y eventos guardados.
    """
    print("\n" + "📜" + "─"*48)
    print(" REGISTRO DE EVENTOS DEL SISTEMA ".center(50))
    print("─"*50)
    
    try:
        with open("logs.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if not contenido:
                print(" No hay eventos registrados.")
            else:
                print(contenido)
    except FileNotFoundError:
        print(" Aún no se han generado registros.")
    
    print("─"*50)
    input("\nPresione Enter para continuar...")
    