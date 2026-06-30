def registrar_usuario():
    nombre = input("Nombre del alumno: ")
    carrera = input("Carrera: ")
    return {"nombre": nombre, "carrera": carrera}

def registrar_libro():
    libro = input("Título del libro: ")
    while True:
        try:
            dias = int(input("Días de préstamo: "))
            if dias > 0:
                return {"libro": libro, "dias": dias}
            print("Los días deben ser un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número entero para los días.")

def generar_resumen(usuario, prestamo):
    print("\n--- Resumen de Reserva ---")
    print(f"Estudiante: {usuario['nombre']} | Carrera: {usuario['carrera']}")
    print(f"Libro solicitado: {prestamo['libro']}")
    print(f"Plazo: {prestamo['dias']} días")
    
    if prestamo["dias"] > 14:
        print("⚠️ ADVERTENCIA: El préstamo supera los 14 días permitidos. Podrían aplicar multas.")

print("--- Sistema de Biblioteca ---")
datos_usuario = registrar_usuario()
datos_prestamo = registrar_libro()
generar_resumen(datos_usuario, datos_prestamo)