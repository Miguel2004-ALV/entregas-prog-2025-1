#!/usr/bin/env python3

"""
Título de práctica: Breve ejemplo de cambios de texto

Este programa realiza diferentes cambios de en textos como mayusculas a minuculas entre otras

Autor: <maalvarezc3@academia.usbbog.edu.co>
Fecha: 2025-05-04
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    # Saludo
    def mostrar_menu():
        """Muestra el menú de operaciones disponibles."""
        print("\n===== MENÚ DE OPERACIONES =====")
        print("1. Pasar a minúsculas")
        print("2. Pasar a mayúsculas")
        print("3. Invertir mayúsculas/minúsculas")
        print("4. Pasar a capitalización (Primera letra mayúscula, las demás minúsculas)")
        print("5. Pasar a titulación (Primera letra mayúscula en cada palabra)")
        print("6. Reemplazar espacios por guiones bajos")
        print("0. Salir")
        print("==============================")

    def minusculas(texto):
        """Convierte el texto a minúsculas."""
        return texto.lower()

    def mayusculas(texto):
        """Convierte el texto a mayúsculas."""
        return texto.upper()

    def invertir_maymin(texto):
        """Invierte mayúsculas y minúsculas en el texto."""
        return ''.join([c.lower() if c.isupper() else c.upper() for c in texto])

    def capitalizar(texto):
        """Capitaliza el texto (primera letra mayúscula, resto minúsculas)."""
        return texto.capitalize()

    def titular(texto):
        """Convierte el texto a formato título (primera letra de cada palabra en mayúscula)."""
        return texto.title()

    def espacios_a_guiones(texto):
        """Reemplaza espacios por guiones bajos."""
        return texto.replace(' ', '_')

    def main():
        # Paso 1: Permitir al usuario ingresar una línea de texto
        print("Bienvenido al Modificador de Texto")
        texto_original = input("\nIngrese una línea de texto: ")
        texto_actual = texto_original
        
        opcion = None
        
        # Paso 2: Mostrar menú de operaciones y permitir repetir
        while opcion != '0':
            # Mostrar el texto actual
            print(f"\nTexto actual: {texto_actual}")
            
            # Mostrar menú
            mostrar_menu()
            
            # Obtener opción del usuario
            opcion = input("Seleccione una opción: ")
            
            # Ejecutar la operación seleccionada
            if opcion == '1':
                texto_actual = minusculas(texto_actual)
                print("\nTexto convertido a minúsculas.")
            elif opcion == '2':
                texto_actual = mayusculas(texto_actual)
                print("\nTexto convertido a mayúsculas.")
            elif opcion == '3':
                texto_actual = invertir_maymin(texto_actual)
                print("\nSe invirtieron mayúsculas/minúsculas.")
            elif opcion == '4':
                texto_actual = capitalizar(texto_actual)
                print("\nTexto capitalizado.")
            elif opcion == '5':
                texto_actual = titular(texto_actual)
                print("\nTexto titulado.")
            elif opcion == '6':
                texto_actual = espacios_a_guiones(texto_actual)
                print("\nEspacios reemplazados por guiones bajos.")
            elif opcion == '0':
                print("\nSaliendo del programa...")
            else:
                print("\nOpción no válida. Intente de nuevo.")
        
        # Mostrar el resultado final
        print("\nTexto final:", texto_actual)
        print("\n¡Gracias por usar el Modificador de Texto!")

    if __name__ == "__main__":
        main()

    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
