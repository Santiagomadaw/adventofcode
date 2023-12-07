def open_split(file_path):
    
    '''Lee un archivo en la ruta proporcionada, elimina los espacios en blanco al principio
    y al final, y divide su contenido en una lista de cadenas utilizando el carácter de nueva línea.'''
    
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')


def card_organize(card_pile):
    
    '''Recibe una lista de cadenas, cada una correspondiente a una carta, y formatea
    cada carta en una lista. El primer elemento es el ID de la carta, el segundo es una
    lista de números ganadores y el tercero es una lista de números que se juegan.'''
    

    pile = []

    for card in card_pile:

        card_read = card.split(':')
        card_id = card_read[0].split()[1]
        winning_numbers_str = card_read[1].split('|')[0]
        playing_numbers_str = card_read[1].split('|')[1]
        winning_numbers = winning_numbers_str.split()
        playing_numbers = playing_numbers_str.split()
        pile.append([card_id, winning_numbers, playing_numbers])

    return pile


def cards_scratch(file_path):
    
    '''Revisa cada carta, calcula los puntos obtenidos considerando que el
    primer número coincidente vale 1 punto y las coincidencias siguientes
    duplican los puntos (1 coincidencia: 1 punto, 2 coincidencias: 4 puntos,
    3 coincidencias: 8 puntos...). Devuelve la cantidad total de puntos
    obtenidos después de procesar toda la pila de cartas.'''
    
    pile_points = 0
    cards = open_split(file_path)
    pile = card_organize(cards)
    for card in pile:
        finded = 0
        for number in card[2]:
            if number in card[1]:
                finded += 1
        if finded:
            pile_points += 2**(finded-1)
    return pile_points


print(cards_scratch(
    '/home/santiagomadaw/repositorios/adventofcode/reto04/input_reto_4.txt'))
