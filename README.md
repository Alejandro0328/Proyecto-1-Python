# 🛠️ Sistema de Gestión de Herramientas Comunitarias (JAC)

Este software ha sido desarrollado para la **Junta de Acción Comunal (JAC)** con el objetivo de digitalizar y optimizar el control de herramientas propiedad del barrio. Permite gestionar préstamos, devoluciones y mantener un inventario actualizado en tiempo real, eliminando el uso de planillas manuales.

---

## 🚀 Funcionalidades Principales

El sistema cuenta con una arquitectura robusta dividida por roles:

### 🏠 Para Residentes (Vecinos)
* **Consulta de Disponibilidad:** Ver qué herramientas están en bodega.
* **Solicitud de Préstamos:** Pedir herramientas indicando cantidad y fechas.
* **Mis Préstamos:** Panel personal para ver el estado de sus solicitudes (En trámite, Activo, Devuelto).
* **Resumen Comunitario:** Ver el total de activos que pertenecen al barrio.

### ⚙️ Para Administradores
* **Gestión de Inventario:** Altas, bajas (por daño), y edición de herramientas.
* **Control de Usuarios:** Registro y actualización de los datos de los vecinos.
* **Aprobación de Solicitudes:** Validar y autorizar la salida de herramientas.
* **Reportes Estadísticos:** Ver herramientas más usadas y alertas de stock bajo.
* **Auditoría (Logs):** Registro de accesos fallidos y eventos del sistema.

---

## 📂 Estructura del Proyecto

El código está organizado de forma modular para facilitar el mantenimiento:

| Módulo | Descripción |
| :--- | :--- |
| `main.py` | Punto de entrada que inicializa los datos y el ciclo principal. |
| `menus.py` | Contiene toda la interfaz visual por consola y lógica de navegación. |
| `Herramienta.py` | Lógica de negocio para el stock y activos del vecindario. |
| `Usuarios.py` | Manejo de perfiles, validación de teléfonos y tipos de usuario. |
| `Prestamos.py` | Motor de transacciones (solicitudes, aprobaciones y devoluciones). |
| `Archivos.py` | Persistencia de datos en formato JSON. |
| `Reportes.py` | Generación de métricas y filtros de búsqueda avanzada. |
| `Logs.py` | Sistema de registro de eventos en archivo de texto. |

---

## 🛠️ Requisitos e Instalación

1.  **Lenguaje:** Python 3.10 o superior.
2.  **Archivos de Datos:** El sistema genera automáticamente los archivos `.json` y `logs.txt` al ejecutarse.

**Instrucciones de ejecución:**
1. Descarga todos los archivos en una sola carpeta.
2. Abre una terminal en esa ubicación.
3. Ejecuta el comando:
   ```bash
   python main.py