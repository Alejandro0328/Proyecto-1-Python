import Archivos
import Usuarios
import Herramienta
import menus
import Prestamos
def iniciar():
    U=Archivos.cargar_datos("usuarios.json")
    H=Archivos.cargar_datos("herramientas.json")
    P=Archivos.cargar_datos("prestamos.json")
    acciones = {
        'agregar_h':Herramienta.agregar_herramientas,
        'mostrar_h': Herramienta.mostrar_herramientas_todas,
        'buscar_h': Herramienta.buscar_herramienta,
        'actualizar_h':Herramienta.actualizar_herramienta,
        'inavilitar_h':Herramienta.inavilitar_herramienta,
        'eliminar_h':Herramienta.eliminar_herramienta,
        'agregar_u':Usuarios.agregar_Usuario,
        'mostrar_u':Usuarios.mostrar_usuarios,
        'buscar_u':Usuarios.buscar_usuario,
        'actualizar_u': Usuarios.actualizar_usuario,
        'eliminar_u':Usuarios.eliminar_usuario,
        'reg_prestamo': Prestamos.registrar_prestamo,
        'devolucion': Prestamos.devolver_herramienta,
        'guardar': Archivos.guardar_datos
    }
    menus.menu_principal(U,H,P,acciones)

iniciar()