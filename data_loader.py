import json

def load_turing_machine_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def add_new_data(file_path, main_struct):
    with open(file_path, 'w') as file:
        json.dump(main_struct, file, indent=4)



def main():
    config_path = 'machine_structure.json'
    config = load_turing_machine_config(config_path)
    print("Configuración cargada:", config)
    


def text_to_stack(text: str): # signo - significa blank
    stack = ['-','-']
    for t in text:
        stack.append(t)
    
    stack = stack + ['-','-']
    
    key = stack[2]
    
    if stack[2] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            key = ord(stack[2]) - 65
            stack[2] = key
            
    return stack, key


def change_transitions(transitions, key, two_options):
    transit = []
    for trans in transitions:
        
        if 'k' in trans[1]:
            trans[1] = str(key)
        
        if 'k' == trans[3]:
            trans[3] = str(key)
        
        if '+ k' in trans[3]:
            valores = trans[3].split(' ')
            if two_options == '1':
                trans[3] = chr(((ord(valores[0])-65 + int(key)) % 26)+ 65)
            if two_options == '2':
                trans[3] = chr(((ord(valores[0])-65 - int(key)) % 26)+ 65)
            
            
        transit.append(trans)    
    return transit



print("Iniciando el programa...")

print(f"EJEMPLOS DE PRUEBA: \033[1;32;40m   3 # ROMA NO FUE CONSTRUIDA EN UN DIA \033[0m")


text = input('Ingresa la cadena que deseas utilizar: \n ')

two_options = input('Desea encriptar o desencriptar?\n1.Encriptar \n2.Desencriptar\n')

# text = '3 # ROMA NO FUE CONSTRUIDA EN UN DIA'

stack_text, key = text_to_stack(text)

print('Cinta de texto\n',stack_text)

print('llave', key)


main_struct = load_turing_machine_config('machine_structure.json')
states = main_struct['states']
input_alph = main_struct['input_alphabet']
tape_alph = main_struct['tape_alphabet']
initial_state = main_struct['initial_state']
accept_state = main_struct['accept_states']
transition = main_struct['transitions']
main_struct['transitions'] = change_transitions(transition, key, two_options)
add_new_data('structure_with_key.json',main_struct)


start_pos = 2

state = initial_state

accept_state_in_machine = False

while start_pos < len(stack_text) and accept_state_in_machine == False:    
    for transit in transition:
        if state == transit[0] and str(stack_text[start_pos]) == transit[1]:
            state = transit[2]
            if transit[4] == 'R':
                stack_text[start_pos] = transit[3]
                start_pos = start_pos + 1
            if transit[4] == 'S':
                stack_text[start_pos] = transit[3]
                start_pos = start_pos
            if transit[4] == 'L':
                stack_text[start_pos] = transit[3]
                start_pos = start_pos - 1    
            
    if state == accept_state[0]:
        accept_state_in_machine = True

    
    

print(stack_text)