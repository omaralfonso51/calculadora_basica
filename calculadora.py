# calculadora.py
# Versión mejorada
# Autor: Omar Alfonso
# Descripción: Calculadora que realiza operaciones básicas con manejo de errores y opción de repetir.

def calcular():
    while True:
        print("\n=== CALCULADORA BÁSICA ===")
        print("Operaciones disponibles:")
        print(" +  Suma")
        print(" -  Resta")
        print(" *  Multiplicación")
        print(" /  División")
        print(" ^  Potencia")
        print(" x  Salir")
        
        operacion = input("\nSelecciona una operación: ").strip()

        if operacion.lower() == 'x':
            print("Saliendo de la calculadora... ¡Hasta luego!")
            break

        try:
            numero_1 = float(input("Primer número: "))
            numero_2 = float(input("Segundo número: "))

            if operacion == '+':
                resultado = numero_1 + numero_2
            elif operacion == '-':
                resultado = numero_1 - numero_2
            elif operacion == '*':
                resultado = numero_1 * numero_2
            elif operacion == '/':
                if numero_2 != 0:
                    resultado = numero_1 / numero_2
                else:
                    print("❌ Error: no se puede dividir por cero.")
                    continue
            elif operacion == '^':
                resultado = numero_1 ** numero_2
            else:
                print("⚠️ Operación no válida. Intenta nuevamente.")
                continue

            print(f"✅ Resultado: {resultado}")

        except ValueError:
            print("⚠️ Error: debes ingresar solo números válidos.")

# Llamar a la función principal
calcular()
