#cambio de proyecto xd
def conversor_divisas():
    """
    Calculadora de conversión de divisas a pesos colombianos.
    
    Permite convertir Dólares Estadounidenses (USD), Euros (EUR) y Libras Esterlinas (GBP)
    a Pesos Colombianos (COP) utilizando tasas de cambio predefinidas.
    """
    
    #1 Tasas de cambio (estas son ficticias, se deben actualizar con valores reales)
    tasa_dolar = 4100  # 1 USD a COP
    tasa_euro = 4800   # 1 EUR a COP
    tasa_libra = 5400  # 1 GBP a COP
    
    print("--- Conversor de Divisas a Pesos Colombianos (COP) ---")
    print("Opciones de conversión:")
    print("1. Dólares Estadounidenses (USD)")
    print("2. Euros (EUR)")
    print("3. Libras Esterlinas (GBP)")
    
    while True:
        opcion = input("Seleccione una opción (1, 2, 3) o 's' para salir: ").lower()
        
        if opcion == 's':
            print("Saliendo del conversor. ¡Hasta pronto!")
            break
            
        try:
            opcion = int(opcion)
            if opcion not in [1, 2, 3]:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número o 's'.")
            continue
        
        try:
            cantidad = float(input("Ingrese la cantidad a convertir: "))
            if cantidad < 0:
                print("La cantidad debe ser un número positivo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese una cantidad numérica.")
            continue
            
        if opcion == 1:
            resultado = cantidad * tasa_dolar
            print(f"{cantidad:,.2f} USD es equivalente a {resultado:,.2f} COP.")
        elif opcion == 2:
            resultado = cantidad * tasa_euro
            print(f"{cantidad:,.2f} EUR es equivalente a {resultado:,.2f} COP.")
        elif opcion == 3:
            resultado = cantidad * tasa_libra
            print(f"{cantidad:,.2f} GBP es equivalente a {resultado:,.2f} COP.")
            
        print("-" * 40)

# 2.Llamar a la función principal para ejecutar el conversor
if __name__ == "__main__":
    conversor_divisas()
