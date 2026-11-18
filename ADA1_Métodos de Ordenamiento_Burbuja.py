def ordenamiento_burbuja(latencias):
    """
    Ordena una lista de latencias de menor a mayor
    utilizando el algoritmo de Ordenamiento de Burbuja optimizado.
    """
    n = len(latencias)
    datos = latencias.copy()

    print(f"\nLista inicial ingresada (ms): {datos}\n")

    for i in range(n - 1):
        intercambiado = False

        # En cada pasada, los últimos 'i' elementos ya quedaron en su posición final
        for j in range(0, n - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                intercambiado = True

        print(f"Pasada {i + 1}: {datos}")

        # Detiene el ciclo si la lista ya quedó ordenada antes de completar todas las vueltas
        if not intercambiado:
            print("-> Optimización: La lista ya quedó ordenada antes de terminar todas las pasadas.")
            break

    return datos


def capturar_latencias():
    """Solicita al usuario la cantidad de servidores y sus tiempos de respuesta."""
    while True:
        try:
            cantidad = int(input("¿Cuántos servidores deseas registrar? (mínimo 2): "))
            if cantidad >= 2:
                break
            print("Error: Ingresa al menos 2 servidores para poder ordenar.")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    latencias = []
    for i in range(cantidad):
        while True:
            try:
                valor = float(input(f"Ingresa la latencia del servidor #{i + 1} (en ms): "))
                if valor >= 0:
                    latencias.append(int(valor) if valor.is_integer() else valor)
                    break
                print("Error: La latencia no puede ser negativa.")
            except ValueError:
                print("Error: Ingresa un valor numérico válido.")

    return latencias


if __name__ == "__main__":
    print("=== ORDENAMIENTO DE BURBUJA: LATENCIAS DE RED ===")
    tiempos_respuesta = capturar_latencias()
    resultado = ordenamiento_burbuja(tiempos_respuesta)
    print(f"\nResultado final ordenado (menor a mayor): {resultado}")