import json

def load_turing_machine_config(file_path):
    """
    Carga la configuración de la máquina de Turing desde un archivo JSON.
    
    Args:
        file_path (str): Ruta al archivo JSON que contiene la configuración de la máquina.

    Returns:
        dict: Diccionario con la estructura de la máquina de Turing.
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("El archivo especificado no fue encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Verifica el formato.")
    return None

# 