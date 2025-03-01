#!/usr/bin/env python3

"""
Título de práctica: breve descripción

Descripción extendida del programa

Autor: ElAutor <el@correo>
Fecha: 2025-02-01
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    # Saludo
    print("Calculadora basica miguel!")
    def calculadora():
        print("Calculadora Básica")
    print("Operaciones disponibles: +, -, *, /")
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
                return
            resultado = num1 / num2
        else:
            print("Operación no válida.")
            return
        
        print(f"El resultado es: {resultado}")
    except ValueError:
        print("Error: Entrada no válida. Ingrese números válidos.")
    
    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()


