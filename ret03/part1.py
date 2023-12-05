

def open_split(motor):
    with open(motor,'r'):
        return motor.read().split('\n')
    
def is_part_number(listOfstrings, x, starty, finishy):
    if x==0:
        startx=0
    else:
        startx = x - 1
        
    if x == len(listOfstrings)-1:
        finishx = x
    else:
        finishx = x +1
        
    if starty == 0:
        starty = starty
    else:
        starty = starty-1
    if finishy == len(listOfstrings[x]):
        finishy = len(listOfstrings[x])-1
    else:
        finishy = finishy
    for indexx in range(startx,finishx+1):
        for indexy in range(starty,finishy+1):
            
            if not listOfstrings[indexx][indexy].isdigit() and listOfstrings[indexx][indexy] !='.':
                return True
    return False
            

def part_finder():
    codes='''467..12
.........(
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
  
    motor_debug = codes.split('\n')
    number = ''
    start = -1
    finsh = -1
    part_number = []
    for indexx in range(len(motor_debug)):
        
        for indexy in range(len(motor_debug[indexx])):
            if motor_debug[indexx][indexy].isdigit():
                
                
                number += motor_debug[indexx][indexy]
                if start == -1:
                    start = indexy
                
            if number != '' and((motor_debug[indexx][indexy].isdigit() and indexy==len(motor_debug[indexx])) or not motor_debug[indexx][indexy].isdigit()):
                  
                if start!=-1:
                    finsh = start + len(number)
                res= is_part_number(motor_debug, indexx, start,finsh)
                if res:
                    part_number.append(number)
                number = ''
                start = -1
                finsh = -1
    print(part_number)


part_finder()
                
            
                
    