import json

def load_turing_machine_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def initialize_tape(shift, text):
    # Coloca el desplazamiento (n) al inicio, seguido del texto a procesar, luego el espacio final.
    return list(str(shift) + ' ' + text + ' ')

def apply_caesar_shift(char, shift, mode="encrypt"):
    """
    Aplica el desplazamiento César a una letra. Si `mode` es 'encrypt', suma el desplazamiento.
    Si `mode` es 'decrypt', lo resta.
    """
    if char == " ":
        return char
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx = alphabet.index(char)
    if mode == "encrypt":
        new_idx = (idx + shift) % 26
    else:
        new_idx = (idx - shift) % 26
    return alphabet[new_idx]

def simulate_turing_machine(config, tape, initial_state, shift, mode="encrypt"):
    # Inicializamos la máquina en el estado inicial
    state = initial_state
    head_position = 2  # Posición inicial después del número de desplazamiento
    text_mode = "encrypt" if mode == "encrypt" else "decrypt"
    
    # Ejecutar las transiciones hasta alcanzar un estado de aceptación
    while state not in config['accept_states']:
        symbol = tape[head_position]
        
        if state == "q_read_encrypt" or state == "q_read_decrypt":
            new_symbol = apply_caesar_shift(symbol, shift, mode=text_mode)
            tape[head_position] = new_symbol
            state = "q_shift_encrypt" if mode == "encrypt" else "q_shift_decrypt"
            head_position += 1
        elif state == "q_shift_encrypt" or state == "q_shift_decrypt":
            # Verifica si hemos alcanzado el espacio final para aceptar la operación
            if tape[head_position] == " ":
                state = "q_accept_encrypt" if mode == "encrypt" else "q_accept_decrypt"
            else:
                state = "q_read_encrypt" if mode == "encrypt" else "q_read_decrypt"

    return ''.join(tape[2:]).strip()  # Convertir la cinta a cadena y eliminar espacios en los extremos

# Configuración del JSON y la prueba
config_path = 'machine_structure.json'  # Cambia esto a la ruta correcta de tu JSON
config = load_turing_machine_config(config_path)

# Parámetros de entrada
shift = 3  # Desplazamiento dinámico
text = "ROMA NO FUE CONSTRUIDA EN UN DIA"
tape = initialize_tape(shift, text)

# Cifrar
result_encrypt = simulate_turing_machine(config, tape, "q0_encrypt", shift, mode="encrypt")
print("Resultado de cifrado:", result_encrypt)

# Inicializar la cinta nuevamente con el texto cifrado
tape = initialize_tape(shift, result_encrypt)

# Decifrar
result_decrypt = simulate_turing_machine(config, tape, "q0_decrypt", shift, mode="decrypt")
print("Resultado de decifrado:", result_decrypt)
