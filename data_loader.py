import json

def load_turing_machine_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def initialize_tape(shift, text):
    return list(str(shift) + ' ' + text + ' ')

def apply_caesar_shift(char, shift, mode="encrypt"):
    if char == " ":
        return char
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx = alphabet.index(char)
    new_idx = (idx + shift) % 26 if mode == "encrypt" else (idx - shift) % 26
    return alphabet[new_idx]

def simulate_turing_machine(config, tape, initial_state, shift, mode="encrypt"):
    state = initial_state
    head_position = 2
    text_mode = "encrypt" if mode == "encrypt" else "decrypt"
    steps = 0
    
    while state not in config['accept_states']:
        if steps > 1000:
            print("Se alcanzó el límite de pasos, posible bucle infinito.")
            break
        
        symbol = tape[head_position]
        print(f"Estado actual: {state}, Símbolo actual: '{symbol}', Posición: {head_position}")
        
        if state == "q0_encrypt" and symbol == str(shift):
            state = "q_read_encrypt"
            head_position += 1
        elif state == "q0_decrypt" and symbol == str(shift):
            state = "q_read_decrypt"
            head_position += 1
        elif state == "q_read_encrypt" or state == "q_read_decrypt":
            new_symbol = apply_caesar_shift(symbol, shift, mode=text_mode)
            print(f"Símbolo transformado: '{new_symbol}'")
            tape[head_position] = new_symbol
            state = "q_shift_encrypt" if mode == "encrypt" else "q_shift_decrypt"
            head_position += 1
        elif state == "q_shift_encrypt" or state == "q_shift_decrypt":
            if tape[head_position] == " ":
                state = "q_accept_encrypt" if mode == "encrypt" else "q_accept_decrypt"
            else:
                state = "q_read_encrypt" if mode == "encrypt" else "q_read_decrypt"
        
        steps += 1

    return ''.join(tape[2:]).strip()

def main():
    config_path = 'machine_structure.json'
    config = load_turing_machine_config(config_path)
    print("Configuración cargada:", config)

    shift = 3
    text = "ROMA NO FUE CONSTRUIDA EN UN DIA"
    tape = initialize_tape(shift, text)

    result_encrypt = simulate_turing_machine(config, tape, "q0_encrypt", shift, mode="encrypt")
    print("Resultado de cifrado:", result_encrypt)

    tape = initialize_tape(shift, result_encrypt)
    result_decrypt = simulate_turing_machine(config, tape, "q0_decrypt", shift, mode="decrypt")
    print("Resultado de decifrado:", result_decrypt)

if __name__ == "__main__":
    print("Iniciando el programa...")
    main()
