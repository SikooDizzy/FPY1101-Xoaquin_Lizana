def validar_nota():
    while True:
        try:
            nota = float(input("Ingresa nota (1.0 a 7.0): "))
            if 1.0 <= nota <= 7.0:
                return nota
            print("La nota debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("Entrada no válida. Usa números (ej: 5.5).")

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mostrar_estado(alumno, promedio):
    print(f"\nAlumno: {alumno}")
    print(f"Promedio Final: {promedio:.1f}")
    if promedio >= 4.0:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")

def iniciar_erp():
    while True:
        print("\n--- Mini ERP Académico ---")
        print("1. Registrar Alumno y Notas")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            alumno = input("Nombre del alumno: ")
            notas = []
            print("Registraremos 3 notas para este alumno.")
            for i in range(3):
                print(f"Nota {i+1}:")
                nota = validar_nota()
                notas.append(nota)
            
            prom_estudiante = calcular_promedio(notas)
            mostrar_estado(alumno, prom_estudiante)
            
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Elige 1 o 2.")

iniciar_erp()