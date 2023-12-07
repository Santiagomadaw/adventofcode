def is_last_char(stringList, x, y):
    '''Devuelve si un valor es el ultimo de una cadena'''
    return not y < len(stringList[x]) - 1

def is_valid_simbol(char):
    '''Devuelve si un valor es un simbolo difente de 
    un punto'''
    return not char.isdigit() and char != '.'

def read_file(file_path):
    '''Lee el archivo y devuelve sus líneas como una lista de strings'''
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')


def is_part_number(list_of_strings, x, start_y, finish_y):
    '''Devuelve si un número linda con algun simbolo distinto del punto'''

    start_x = max(0, x-1)
    finish_x = min(x+1, len(list_of_strings)-1)+1
    for i in range(start_x, finish_x):
        for j in range(start_y, finish_y):
            if is_valid_simbol(list_of_strings[i][j]):
                return True
    return False


def part_finder(file):
    '''Busca numeros correlativos,
     revisa si lindan con un simbolo
     distinto del punto y acumula su
     valor'''
    motor_open = read_file(file)
    part_number = 0
    for indexx in range(len(motor_open)):
        number = ''
        start = -1
        finish = -1
        for indexy in range(len(motor_open[indexx])):
            
            # si encuentra un digito lo acumula en number si era el
            # primero da valor a start, de lo contrario mira si es
            # el ultimo de la fila antes de ver si el numero tiene
            # mas digitos
            
            if motor_open[indexx][indexy].isdigit():
                number += motor_open[indexx][indexy]
                if start == -1:
                    start = max(0, indexy-1)
                else:
                    if is_last_char(motor_open, indexx, indexy):
                        finish = indexy +1
                        
            else:
                
                # Si no encuientra un digito comprueba si start tiene valor,
                # de ser asi da valor a finish.En caso contrario sigue su
                # busqueda
                
                if start != -1:
                    finish = indexy+1
            # Si hay un finish valido procedo a mirar si tiene un simbolo
            # colindante y de sere asi sumarlo al cumulado
            if finish != -1:
                if is_part_number(motor_open, indexx, start, finish):
                    part_number += int(number)
                number = ''
                start = -1
                finish = -1
    return part_number

print(part_finder('inputreto03-1.txt'))
