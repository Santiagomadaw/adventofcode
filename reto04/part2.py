def open_split(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def card_organize(card_pile):
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
    pile_points = 0
    cards = open_split(file_path)
    pile = card_organize(cards)
    pile_register ={}
    for card in pile:
        pile_register[card[0]] = 1
        
        
    for card in pile:
        card_points = 0
        for number in card[2]:
            if number in card[1]:
                for repet in range(pile_register[card[0]]):
                    if card_points == 0:
                        card_points =1
                    else:
                        card_points +=1
                    for i in range(1,card_points+1):
                        pile_register[card[0]+i] +=1
                
        pile_points += card_points
    return pile_points


                

print(cards_scratch('/home/santiagomadaw/repositorios/adventofcode/reto04/input_reto_4.txt'))