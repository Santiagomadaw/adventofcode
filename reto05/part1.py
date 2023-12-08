def tokenize(raw):
    separated_maps = raw.strip().split('\n\n')
    dictio = {}
    for element in separated_maps:
        categories = element.split(':')
        category = categories[0].replace(' ','').replace('-','_')
        mapped = categories[1].strip().split('\n')
        mappedlist=[]
        for element in mapped:
            data = element.split()
            numeral =[]
            for num in data:
                numeral.append(int(num))
            mappedlist.append(numeral)
            dictio[category]=mappedlist
    return dictio

def open_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def trace_finder(seed,mapper):
   
    for final, start, ammount in mapper:
        fin=start+ammount-1
        if int(seed) in range(start,fin):
            return int(seed) - start + final
    return int(seed)

def seed_trace(file):
    data = open_file(file)
    procesed_data= tokenize(data)
    seeds = procesed_data['seeds'][0]
    for element in procesed_data:
        traced = []
        if element=='seeds':
            pass
        else:
            for seed in seeds:
                traced.append(trace_finder(seed,procesed_data[element]))
            seeds = traced
    closer =traced[0]
    for ubication in traced:
        if ubication< closer:
            closer= ubication
    return closer

    

print(seed_trace('/home/santiagomadaw/repositorios/adventofcode/reto05/input_reto_5.txt'))
