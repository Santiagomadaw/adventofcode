from functools import reduce
data ='''Time:        60     94     78     82
Distance:   475   2138   1015   1650'''



def race_calc(time_distance):
    ''' recive una tabla de tiempos y  distancias y calcula las diferentes
    convinaciones de tiempo de carga tiempo de carrera que superan en distancia
    a la que hay en la tabla'''
   
    time, distance = time_distance
    option= filter(lambda x:(time -x)*x > distance, range(time))
    return len(list(option))


    
def multiplicator(table):
    '''Recive una tabla de tiempos distancia en texto sin formato,
    transforma la la cadena en una lista de duplas y devueve el producto
    de convinaciones ganadoras de cada tabla'''
    times = map(int, table.strip().split('\n')[0].split(':')[1].strip().replace(' ','').split())
    distances =map(int,table.strip().split('\n')[1].split(':')[1].strip().replace(' ','').split())

    nl  = list(zip(times,distances))
   
    result = reduce(lambda result, x:result*race_calc(x),nl,1)
 
    return result
print(multiplicator(data))

