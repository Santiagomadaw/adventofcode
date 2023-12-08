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
    
def trace_finder(seeds,mapper):
    result =[]
  
  
    for seeds_start, seeds_scroll in seeds:
        seeds_finish = seeds_start + seeds_scroll -1
        
        interjection =[]
        for destination, source, ammount in mapper:
            finish=source+ammount-1
            scrool = destination-source
            if seeds_finish<source or seeds_start> finish:
                continue
            interjection_start = max(source, seeds_start)
            interjection_finish = min(finish,seeds_finish)
            interjection.append((interjection_start, interjection_finish))
            result.append((interjection_start+scrool, interjection_finish-interjection_start))
            #ya he añadido los intervalos donde ambos 
            # conjuntos tienen elementos comunes transformados.
            # Ahora añado sin transformar aquellos que no tienen
            # elementos comunes. Primero delante y detras delos comunes
        if not interjection:
            result.append((seeds_start, seeds_scroll))
            continue
        interjection.sort()
        if seeds_start < interjection[0][0]:
            result.append((seeds_start-1,interjection[0][0]-seeds_start))
        if seeds_finish > interjection[-1][1]:
            result.append((interjection[-1][1]+1, seeds_finish-interjection[-1][1]))
        for i in range(len(interjection)-1):
            _, finish1 = interjection[i]
            start2, _ = interjection[i+1]
            if finish1 + 1  < start2:
                result.append((finish1+1,start2-(finish1+1)-1))
                      
                    
                  
                
            
    return result



def seed_trace2(file):
    data = open_file(file)
    procesed_data= tokenize(data)
    seeds = procesed_data['seeds'][0]
    ###################################################################
    interval_seeds = []
    for index  in range(0, len(seeds),2):
                interval_seeds.append([seeds[index],seeds[index+1]])
    ###################################################################            
    current_seeds = interval_seeds
    for element in procesed_data:
        if element == 'seeds':
            continue
        
        result_seeds=trace_finder(current_seeds,procesed_data[element])
        current_seeds = result_seeds
           
    closer = min(current_seeds)[0]         
    return closer

print(seed_trace2('/home/santiagomadaw/repositorios/adventofcode/reto05/input_reto_5.txt'))
