import random
import datetime

# Base de datos simulada
usuarios = [
    {"id": 0, "nombre": "admin", "tipo": "administrador", "activo": True},
    {"id": 1, "nombre": "moderador1", "tipo": "moderador", "activo": True},
    {"id": 2, "nombre": "usuario1", "tipo": "estudiante", "activo": True},
    {"id": 3, "nombre": "usuario2", "tipo": "estudiante", "activo": True},
]

reportes = [
    {"id_reportante": 2, "id_reportado": 3, "estado": 0, "motivo": "comportamiento inapropiado"},
]

# Función para mostrar el menú de administrador
def menu_administrador():
    while True:
        print("\n--- Menú de Administrador ---")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Reportes")
        print("3. Reportes Estadísticos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_usuarios()
        elif opcion == "2":
            gestionar_reportes()
        elif opcion == "3":
            reportes_estadisticos()
        elif opcion == "4":
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

# Función para gestionar usuarios
def gestionar_usuarios():
    while True:
        print("\n--- Gestionar Usuarios ---")
        print("1. Eliminar un Usuario")
        print("2. Dar de alta un Moderador")
        print("3. Desactivar Usuario")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            eliminar_usuario()
        elif opcion == "2":
            alta_moderador()
        elif opcion == "3":
            desactivar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

# Función para eliminar un usuario (excepto administradores)
def eliminar_usuario():
    id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            if usuario["tipo"] == "administrador":
                print("No puede eliminar a otro administrador.")
            else:
                usuarios.remove(usuario)
                print(f"Usuario {usuario['nombre']} eliminado.")
            return
    print("Usuario no encontrado.")

# Función para dar de alta un moderador
def alta_moderador():
    nombre = input("Ingrese el nombre del nuevo moderador: ")
    nuevo_moderador = {
        "id": len(usuarios),
        "nombre": nombre,
        "tipo": "moderador",
        "activo": True
    }
    usuarios.append(nuevo_moderador)
    print(f"Moderador {nombre} dado de alta exitosamente.")

# Función para desactivar un usuario
def desactivar_usuario():
    id_usuario = int(input("Ingrese el ID del usuario a desactivar: "))
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario["activo"] = False
            print(f"Usuario {usuario['nombre']} desactivado.")
            return
    print("Usuario no encontrado.")

# Función para gestionar reportes
def gestionar_reportes():
    print("\n--- Gestionar Reportes ---")
    for reporte in reportes:
        if reporte["estado"] == 0:  # Mostrar solo reportes pendientes
            print(f"Reporte del usuario {reporte['id_reportante']} contra el usuario {reporte['id_reportado']}.")
            accion = input("¿Ignorar reporte (i) o bloquear usuario (b)?: ")

            if accion == "i":
                reporte["estado"] = 2
                print("Reporte ignorado.")
            elif accion == "b":
                bloquear_usuario(reporte["id_reportado"])
                reporte["estado"] = 1
                print("Usuario bloqueado y reporte aceptado.")
            else:
                print("Opción inválida.")

# Función para bloquear un usuario
def bloquear_usuario(id_usuario):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario["activo"] = False
            print(f"Usuario {usuario['nombre']} bloqueado.")
            return
    print("Usuario no encontrado.")

# Función para mostrar reportes estadísticos
def reportes_estadisticos():
    total_reportes = len(reportes)
    ignorados = sum(1 for r in reportes if r["estado"] == 2)
    aceptados = sum(1 for r in reportes if r["estado"] == 1)

    if total_reportes > 0:
        print(f"Total de reportes: {total_reportes}")
        print(f"Reportes ignorados: {ignorados} ({(ignorados/total_reportes)*100:.2f}%)")
        print(f"Reportes aceptados: {aceptados} ({(aceptados/total_reportes)*100:.2f}%)")
    else:
        print("No hay reportes para mostrar.")

# Iniciar el menú de administrador
menu_administrador()
