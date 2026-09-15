# Tarea Semana 14: Funciones con parámetros y retorno de valores

def calcular_precio_total(precio_unitario, cantidad, porcentaje_descuento):
    """
    Función que calcula el precio total de una compra aplicando un descuento.
    - Parámetros: precio_unitario, cantidad, porcentaje_descuento
    - Retorna: el total final a pagar
    """
    subtotal = precio_unitario * cantidad
    descuento = subtotal * (porcentaje_descuento / 100)
    total_final = subtotal - descuento
    return total_final  # Retorno del valor calculado

# --- Flujo principal del programa ---
print("--- SISTEMA DE CÁLCULO DE COMPRAS ---")

# Ingreso de datos por teclado mediante input()
precio = float(input("Ingrese el precio del producto: $"))
cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
descuento_aplicado = float(input("Ingrese el porcentaje de descuento (%): "))

# Llamada a la función pasándole los parámetros ingresados
total_pagar = calcular_precio_total(precio, cantidad_comprada, descuento_aplicado)

# Mostrar el resultado en pantalla
print("\n--- RESUMEN DE COMPRA ---")
print(f"Precio por unidad: ${precio:.2f}")
print(f"Cantidad: {cantidad_comprada}")
print(f"Descuento aplicado: {descuento_aplicado}%")
print(f"El total final a pagar es: ${total_pagar:.2f}")