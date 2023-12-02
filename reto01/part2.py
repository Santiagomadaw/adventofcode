
def text_to_number(numberString):
    translator = {
    'one': 1,
    'two': 2,
    'thr': 3,
    'fou': 4,
    'fiv': 5,
    'six': 6,
    'sev': 7,
    'eig': 8,
    'nin': 9
}
    print(numberString)
    acum = '0'
    for index in range(len(numberString)):
        if numberString[index].isdigit():
            acum += numberString[index]
        else:
            capable = numberString[index:index+3]
    
            if capable in translator:
                acum += str(translator[numberString[index:index+3]])
    acum=str(int(acum))
    print(int(acum[0]+acum[-1]))
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
