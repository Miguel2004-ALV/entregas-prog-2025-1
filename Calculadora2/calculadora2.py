#!/usr/bin/env python3

"""
Calculadora 1: Ejemolo basico de calculadora 

Este es un ejemplo de una caulculadora basica 

Autor:<maalvarezc3@academia.usbbog.edu.co>
Fecha: 2025-03-13
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    # Saludo

    def main():
        print("Calculadora Avanzada de Miguel")
        continuar = True
        
        while continuar:
            try:
                # Mostrar menú de operaciones primero
                print("\Operaciones disponibles:")
                print("1. Suma (+)")
                print("2. Resta (-)")
                print("3. Multiplicación (*)")
                print("4. División (/)")
                print("5. Potenciación (^)")
                print("6. División Entera (//)")
                print("7. Módulo (%)")
                
                # Pedir la operación antes de los operandos
                operacion = input("\Seleccione la operación (+, -, *, /, ^, //, %): ")
                
                # Validar la operación
                if operacion not in ['1', '2', '3', '4', '5', '6', '7', '+', '-', '*', '/', '^', '//', '%']:
                    print("Error: Operación no válida.")
                    continue
                
                # Pedir operandos con opción para cancelar
                operando_a_str = input("Ingrese el operando A (o 'cancelar' para volver al menú): ")
                if operando_a_str.lower() == 'cancelar':
                    continue
                    
                operando_b_str = input("Ingrese el operando B (o 'cancelar' para volver al menú): ")
                if operando_b_str.lower() == 'cancelar':
                    continue
                
                # Convertir operandos al tipo adecuado
                try:
                    operando_a = float(operando_a_str)
                    operando_b = float(operando_b_str)
                except ValueError:
                    print("Error: Por favor ingrese números válidos.")
                    continue
                
                # Si es división entera o módulo, convertir a enteros
                if operacion in ['6', '7', '//', '%']:
                    # Verificar si los números son realmente enteros
                    if operando_a != int(operando_a) or operando_b != int(operando_b):
                        print("Advertencia: División entera y módulo requieren enteros. Se convertirán los valores.")
                    operando_a = int(operando_a)
                    operando_b = int(operando_b)
                
                # Realizar la operación seleccionada
                if operacion == '1' or operacion == '+':
                    resultado = operando_a + operando_b
                    simbolo = '+'
                elif operacion == '2' or operacion == '-':
                    resultado = operando_a - operando_b
                    simbolo = '-'
                elif operacion == '3' or operacion == '*':
                    resultado = operando_a * operando_b
                    simbolo = '*'
                elif operacion == '4' or operacion == '/':
                    # Verificar división por cero
                    if operando_b == 0:
                        print("Error: No se puede dividir por cero.")
                        continue
                    resultado = operando_a / operando_b
                    simbolo = '/'
                elif operacion == '5' or operacion == '^':
                    resultado = operando_a ** operando_b
                    simbolo = '^'
                elif operacion == '6' or operacion == '//':
                    # Verificar división por cero
                    if operando_b == 0:
                        print("Error: No se puede dividir por cero.")
                        continue
                    resultado = operando_a // operando_b
                    simbolo = '//'
                elif operacion == '7' or operacion == '%':
                    # Verificar división por cero
                    if operando_b == 0:
                        print("Error: No se puede calcular el módulo por cero.")
                        continue
                    resultado = operando_a % operando_b
                    simbolo = '%'
                
                # Mostrar el resultado
                print(f"\nResultado: {operando_a} {simbolo} {operando_b} = {resultado}")
                
                # Preguntar si desea continuar
                respuesta = input("\n¿Desea realizar otra operación? (s/n): ")
                if respuesta.lower() != 's' and respuesta.lower() != 'si':
                    continuar = False
                    print("¡Gracias por usar la calculadora!")
                    
            except Exception as e:
                print(f"Error inesperado: {e}")
                respuesta = input("\n¿Desea intentar otra operación? (s/n): ")
                if respuesta.lower() != 's' and respuesta.lower() != 'si':
                    continuar = False
                    print("¡Gracias por usar la calculadora!")

    if __name__ == "__main__":
        main()

# **** ****

# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
