
def text_to_number(numberString:int):
    translator = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
    acum = '0'
    index = 0
    while index<len(numberString):
        if numberString[index].isdigit():
            acum += numberString[index]
        else:    
            for number, value in translator.items():
                if numberString[index:index + len(number)] == number :
                    acum += str(value)
                    break
        index +=1
    acum=str(int(acum))
    return int(acum[0]+acum[-1])

from functools import reduce

def decode(codes:list[str]):
    number_codes = list(map(lambda x: text_to_number(x), codes))
    lastcode= reduce(lambda accum, z: accum + z, number_codes, 0)
    return lastcode
    
def decode_machine(file):
    with open (file, 'r') as opened_file:
        contain = opened_file.read()

    list_contain = contain.split('\n')
    return decode(list_contain)

print(decode_machine('input2.txt'))
