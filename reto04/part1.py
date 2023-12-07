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
    '''Revisa cada carta comprueba los puntos ganados teniendo encuenta
    quue el primero numero vale 1 punto pero los siguientes multiplican
    los puntos que tienes por 2. [1 coincidencia 1 punto,2 coincidencias 4,
    3 coincidencias 8...]. Devuelve la cantidad total de cartas
    que tienes cuando terminas con todo el mazo'''
    pile_points = 0
    cards = open_split(file_path)
    pile = card_organize(cards)
    for card in pile:
        finded = 0
        for number in card[2]:
            if number in card[1]:
                finded+=1
        if finded:
            pile_points += 2**(finded-1)
    return pile_points


                

print(cards_scratch('/home/santiagomadaw/repositorios/adventofcode/reto04/input_reto_4.txt'))