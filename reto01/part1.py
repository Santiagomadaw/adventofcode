from functools import reduce

def decode(codes:list[str]):
    
    def number_code(x):
        
        digits= ''.join(filter(lambda y: y.isdigit(), x))
        return digits if digits else '0'                            
    
    number_codes = list(map(lambda x: int(number_code(x)[0]+number_code(x)[-1]), codes))
    
  
    lastcode= reduce(lambda accum, z: accum + z, number_codes, 0)
    return lastcode
    
def decode_machine(file):
    with open (file, 'r') as opened_file:
        contain = opened_file.read()
    
    list_contain = contain.split('\n')
    return decode(list_contain)

print(decode_machine('input.txt'))
