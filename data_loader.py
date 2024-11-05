import json

def load_turing_machine_config(file_path):
    """
    Carga la configuración de la máquina de Turing desde un archivo JSON.
    
    Args:
        file_path (str): Ruta al archivo JSON que contiene la configuración de la máquina.

    Returns:
        dict: Diccionario con la estructura de la máquina de Turing, o None si hay un error.
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        if validate_turing_machine_config(config):
            return config
        else:
            print("El archivo JSON no contiene la estructura requerida.")
            return None
    except FileNotFoundError:
        print("El archivo especificado no fue encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Verifica el formato.")
    return None

def validate_turing_machine_config(config):
    """
    Valida que el diccionario de configuración tenga las claves requeridas para la máquina de Turing.

    Args:
        config (dict): Diccionario con la configuración de la máquina de Turing.

    Returns:
        bool: True si la configuración es válida, False en caso contrario.
    """
    required_keys = {"states", "input_alphabet", "tape_alphabet", "initial_state", "accept_states", "transitions"}
    if not all(key in config for key in required_keys):
        print("Faltan algunas claves esenciales en el archivo JSON.")
        return False
    # Validar que los elementos principales estén correctamente estructurados
    if not isinstance(config["states"], list) or not isinstance(config["input_alphabet"], list) or not isinstance(config["tape_alphabet"], list):
        print("Error en los formatos de 'states', 'input_alphabet' o 'tape_alphabet'. Deben ser listas.")
        return False
    if not isinstance(config["initial_state"], str):
        print("Error: 'initial_state' debe ser una cadena.")
        return False
    if not isinstance(config["accept_states"], list):
        print("Error: 'accept_states' debe ser una lista.")
        return False
    if not isinstance(config["transitions"], list):
        print("Error: 'transitions' debe ser una lista de transiciones.")
        return False
    return True

# Ejemplo de uso
config_path = 'machine_structure.json'
config = load_turing_machine_config(config_path)
if config:
    print("Configuración cargada correctamente.")
else:
    print("Error al cargar la configuración.")