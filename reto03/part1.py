

def last_char(stringList, x, y):
    return not y < len(stringList[x])-1


def first_one(index, reference=0):

    return max(0, index-1)
def is_valid_simbol(char):
    return not char.isdigit() and char != '.'

def open_split(motor):
    with open(motor, 'r'):
        return motor.read().split('\n')


def is_part_number(listOfstrings, x, starty, finishy):

    startx = (max(0, x-1))
    finishx = (min(x+1, len(listOfstrings)-1))
    for i in range(startx, finishx+1):

        for j in range(starty, finishy+1):

            if is_valid_simbol(listOfstrings[i][j]):
                return True
    return False


def part_finder(file):
    motor_debug = open_split(file)
 
    part_number = 0
    for indexx in range(len(motor_debug)):
        number = ''
        start = -1
        finish = -1
        for indexy in range(len(motor_debug[indexx])):

            if motor_debug[indexx][indexy].isdigit():

                number += motor_debug[indexx][indexy]
                if start == -1:
                    start = first_one(indexy)
                else:
                    if last_char(motor_debug, indexx, indexy):

                        finish = indexy
                        print(number)
            else:

                if start != -1:
                    finish = indexy

                    print('numero', number)

            if finish != -1:
                if is_part_number(motor_debug, indexx, start, finish):
                    part_number += int(number)
                number = ''
                start = -1
                finish = -1
    return part_number

print(part_finder('inputreto03-1.txt'))
