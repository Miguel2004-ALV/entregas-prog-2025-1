#!/usr/bin/env python3

"""
Título de práctica: CalcFecha1

Programa de calculos de fecha 

Autor:<maalvarezc3@academia.usbbog.edu.co>
Fecha: 2025-05-18
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    # Saludo

    from datetime import datetime, timedelta

    def main():
        while True:
            # Mostrar la fecha actual
            now = datetime.now()
            print(f"La fecha actual es: {now}")

            # Menú de opciones
            print("Escriba 1 para ingresar segundos,")
            print("        2 para ingresar días,")
            print("        3 para salir.")
            
            # Leer la opción del usuario
            option = input("< ")
            
            if option == '1':
                # Ingresar segundos
                seconds = int(input("Escriba la cantidad de segundos: "))
                new_date = now + timedelta(seconds=seconds)
                print(f"La nueva fecha es: {new_date}")
            
            elif option == '2':
                # Ingresar días
                days = int(input("Escriba la cantidad de días: "))
                new_date = now + timedelta(days=days)
                print(f"La nueva fecha es: {new_date}")
            
            elif option == '3':
                print("Gracias!")
                break
            
            else:
                print("Opción no válida. Intente de nuevo.")

    if __name__ == "__main__":
        main()

    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()