def open_split(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def card_organize(card_pile):
    
    '''recibe una lista de cadenas cada una correspondiente
    a una carta y la devuelve formateadndo cada carta en una
    lista, la primera el id de la carta, el segundo una lista
    de numeros ganadores y el tercero una lista de numeros con 
    los que juegas'''
    
    pile = []
    for card in card_pile:
        card_read = card.split(':')
        card_id = card_read[0].split()[1]
        winning_numbers_str = card_read[1].split('|')[0]
        playing_numbers_str = card_read[1].split('|')[1]
        winning_numbers = winning_numbers_str.split()
        playing_numbers = playing_numbers_str.split()
        
        pile.append([card_id,winning_numbers,playing_numbers])
    return pile

def cards_scratch(file_path):
    '''Revisa cada carta y añade una carta extra a cada una de las
    cartas siguientes del mazo. Devuelve la cantidad total de cartas
    que tienes cuando terminas con todo el mazo'''
   
    cards = open_split(file_path)
    pile = card_organize(cards)
    pile_register ={}
    
    # Crea un diccionario donde guarda la cantidad de cartas que
    # hay inicialmente para cada carta
    
    for card in pile:
        pile_register[card[0]] = 1
        
    # Para cada carta del mazo comprueba cuantos numeros ganadores
    # hay y despues añade una carta extra a las siguentes si de al
    # carta actual tengo X iguales a cada una de las siguietes les
    # pongo X cartas.
    
    for card in pile:
        card_points = 0
        for number in card[2]:
            if number in card[1]:
                    if card_points == 0:
                        card_points =1
                    else:
                        card_points +=1
        for i in range(1,card_points+1):
            newcard= str(int(card[0])+i)
            if int(newcard)<len(pile)+1:
                pile_register[newcard] +=pile_register[card[0]]
    total_cards =0       
    for element in pile_register:
        total_cards+=pile_register[element]
            
    return total_cards


                

print(cards_scratch('/home/santiagomadaw/repositorios/adventofcode/reto04/input_reto_4.txt'))