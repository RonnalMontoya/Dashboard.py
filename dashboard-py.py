import os

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del archivo de script especificado.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def listar_archivos(directorio):
    """
    Lista todos los archivos en el directorio especificado.
    """
    try:
        archivos = os.listdir(directorio)
        print(f"\n--- Archivos en {directorio} ---")
        for archivo in archivos:
            print(archivo)
    except FileNotFoundError:
        print("El directorio no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al listar los archivos: {e}")

def agregar_ruta(opciones):
    """
    Permite agregar una nueva ruta de script al menú.
    """
    nueva_clave = input("Ingrese el número de la nueva opción: ")
    nueva_ruta = input("Ingrese la ruta del nuevo script: ")
    opciones[nueva_clave] = nueva_ruta

def mostrar_menu():
    """
    Muestra el menú principal y gestiona las opciones del usuario.
    """
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Diccionario de opciones del menú
    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("L - Listar archivos en un directorio")
        print("A - Agregar una nueva ruta de script")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        elif eleccion == 'L':
            directorio = input("Ingrese la ruta del directorio: ")
            listar_archivos(directorio)
        elif eleccion == 'A':
            agregar_ruta(opciones)
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
