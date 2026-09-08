def calcular_promedio(nota1, nota2, nota3):
    """
    Función que recibe dos notas y calcula su promedio.

    Parámetros:
    nota1 (float): Primera nota
    nota2 (float): Segunda nota
    nota3 (float): Tercera nota

    Retorna:
    float: El promedio ponderado de las tres notas
    """
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


if __name__ == "__main__":
    print("=== PROGRAMA PARA CALCULAR EL PROMEDIO DE NOTAS ===")

    # Lectura de datos desde la consola
    nota_uno = float(input("Ingrese la primera nota: "))
    nota_dos = float(input("Ingrese la segunda nota: "))
    nota_tres = float(input("Ingrese la tercera nota: "))

    # Llamada a la función con dos parámetros
    resultado_promedio = calcular_promedio(nota_uno, nota_dos, nota_tres)

    # Impresión del resultado
    print(f"\nEl promedio obtenido es: {resultado_promedio:.1f}")
