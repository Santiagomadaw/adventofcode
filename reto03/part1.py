
def last_char(stringList, x, y):
    return not y < len(stringList[x]) - 1

def is_valid_simbol(char):
    return not char.isdigit() and char != '.'

def open_split(motor):
    with open(motor, 'r') as rawfile:
        return rawfile.read().strip().split('\n')


def is_part_number(listOfstrings, x, starty, finishy):
    startx = max(0, x-1)
    finishx = min(x+1, len(listOfstrings)-1)+1
    for i in range(startx, finishx):
        for j in range(starty, finishy):
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
                    start = max(0, indexy-1)
                else:
                    if last_char(motor_debug, indexx, indexy):

                        finish = indexy +1
            else:

                if start != -1:
                    finish = indexy+1


            if finish != -1:
                if is_part_number(motor_debug, indexx, start, finish):
                    part_number += int(number)
                number = ''
                start = -1
                finish = -1
    return part_number

print(part_finder('inputreto03-1.txt'))
