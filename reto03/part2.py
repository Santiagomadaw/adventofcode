
def last_char(stringList, x, y):
    '''Devuelve su un valor es el ultimo de la cadena'''
    return not y < len(stringList[x]) - 1


def open_split(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')


def is_obelix(list_of_strings, x, start_y, finish_y):
    '''Devuelve si un numero linda con un "Asterix"'''
    start_x = max(0, x-1)
    finish_x = min(x+1, len(list_of_strings)-1)+1
    for i in range(start_x, finish_x):
        for j in range(start_y, finish_y):
            if list_of_strings[i][j]== '*':
                return True
    return False


def index_part(motor_debug):
    '''Transroma la cadena original en una lista de dicionarios
    En cada entrada de la lista se guarda un diccionario donde 
    cada numero es una clave y como valor guarda el rango de accion
    de este. si encuentra un numero XXX en la posicion 2,3,4 de su fila
    este guardariacomo valor (1,5)'''

    indexed_motor = []
    for index_x in range(len(motor_debug)):

        number = ''
        start = -1
        finish = -1
        indexed_numbers = {}
        for index_y in range(len(motor_debug[index_x])):
            if motor_debug[index_x][index_y].isdigit():
                number += motor_debug[index_x][index_y]

                # si encuentra un digito lo acumula en number si era el
                # primero da valor a start, de lo contrario mira si es
                # el ultimo de la fila antes de ver si el numero tiene
                # mas digitos

                if start == -1:
                    start = max(0, index_y-1)
                else:
                    if last_char(motor_debug, index_x, index_y):
                        finish = index_y +1           
            else:

                # Si no encuientra un digito comprueba si start tiene valor,
                # de ser asi da valor a finish.En caso contrario sigue su
                # busqueda

                if start != -1:
                    finish = index_y+1

            # Si hay un finish valido procedo a mirar si tiene un asterisco
            # colindante y de sere asi acumilarlo en el diccionario de su fila
            if finish != -1:
                if is_obelix(motor_debug, index_x, start, finish):
                    suscess_save = False
                    # En caso de ya haber un numero igual en el diccionario se
                    # le van añadiendo ceros delante hasta lograr encontrar una
                    # clave libre, mas adelante al ser transformado en entero
                    # para su uso esos ceros de mas desapareceran
                    while not suscess_save:
                        if number in indexed_numbers:
                            number= '0' + number
                        else:
                            indexed_numbers[number]=(start,finish)
                            suscess_save = True
                # Al haber un finish y haber tratado ya el numero resetea para
                # buscar el siguiente de la linea
                number = ''
                start = -1
                finish = -1
        # Al llegar al final de la linea guardo el dicionario dentro de la lista.
        # No compruebo si esta vacia porque me interesa que se mantenga la relacion
        # entre la el index de la cadena y del diccionario
        indexed_motor.append(indexed_numbers)

    return indexed_motor


def gear_finder(file):
    '''Busca asteriscos, cuando encuentra 1 mira en la fila inmediatamente superior e inmediatamente inferior
    en busca de 2 numeros cuyo rango comprenda el valor de su posicion en la cadena, si los encuentra acumula
    el resultado de la multiplicacion de ambos numeros'''
    motor_open = open_split(file)
    pasts_catalog = index_part(motor_open)
    result = 0
    for indexx in range(len(motor_open)):
        for indexy in range(len(motor_open[indexx])):
            if motor_open[indexx][indexy]=='*':
                start = max(0, indexx -1)  
                finish = min(indexx+1, len(motor_open)-1)+1
                obelix = []
                for x in range(start,finish):
                    for element in pasts_catalog[x]:
                        part_range = pasts_catalog[x][element]
                        if indexy in range(part_range[0],part_range[1]):
                            obelix.append(int(element))
                    if len(obelix)>1:
                        result += obelix[0]*obelix[1]
                        obelix = []
    return result
print(gear_finder('inputreto03-1.txt'))
