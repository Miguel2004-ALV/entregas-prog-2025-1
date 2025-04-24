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
    
    print("Calculadora Básica de Miguel")

    # Pedir operandos
    try:
        operando_a = float(input("Ingrese el operando A: "))
        operando_b = float(input("Ingrese el operando B: "))
    
        # Mostrar menú de operaciones
        print("\nOperaciones disponibles:")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        
        # Pedir la operación
        operacion = input("\nSeleccione la operación (+, -, *, /): ")
        
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
            # Verificar división por cero antes de realizar la operación
            if operando_b == 0:
                print("Error: No se puede dividir por cero.")
            else:
                resultado = operando_a / operando_b
                simbolo = '/'
        else:
            print("Error: Operación no válida.")
            exit()
        
        # Mostrar el resultado
        if operacion == '4' or operacion == '/' and operando_b == 0:
            pass  # No mostrar resultado si hubo división por cero
        else:
            print(f"\nResultado: {operando_a} {simbolo} {operando_b} = {resultado}")
            
    except ValueError:
        print("Error: Entrada no válida. Por favor ingrese números válidos.")

# **** ****

# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
    