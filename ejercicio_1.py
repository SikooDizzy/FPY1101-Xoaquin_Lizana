def validar_temperatura():
    while True:
        try:
            temp = float(input("Ingresa la temperatura: "))
            return temp
        except ValueError:
            print("Eso no es un número válido. Intenta otra vez.")

def calcular_promedio(lista_temps):
    return sum(lista_temps) / len(lista_temps)

def obtener_alerta(promedio):
    if promedio < 10:
        return "Alerta: Temperatura extrañamente baja."
    elif 10 <= promedio <= 25:
        return "Temperatura en rango normal."
    else:
        return "Alerta: Temperatura peligrosamente alta."

temperaturas = []
print("--- Registro de Temperaturas ---")
for i in range(5):
    print(f"Temperatura {i+1}:")
    t = validar_temperatura()
    temperaturas.append(t)

promedio_final = calcular_promedio(temperaturas)
alerta_final = obtener_alerta(promedio_final)

print("\n--- Reporte Final ---")
print(f"Temperaturas registradas: {temperaturas}")
print(f"Promedio: {promedio_final:.2f}°C")
print(f"Estado: {alerta_final}")