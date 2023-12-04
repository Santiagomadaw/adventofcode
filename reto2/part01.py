def format_game(game):
    splited_code = game.split(':')
    game_number = int(splited_code[0].split()[1])
    hands= splited_code[1].split(';')
    hands = separe_hands(hands)
    return [game_number, hands]
    
    
def separe_hands(hands):
    list_of_hands=[]
    for hand in hands:
        formated_hands = dict()
        cubes = hand.split(',')
        for color in cubes:
            color= color.split()
            formated_hands[color[1]]=int(color[0])
        list_of_hands.append(formated_hands) 
    return list_of_hands

def valid_game_code_sum(file):
    
    max_hand = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    acum=0
    
    with open(file, 'r') as rawcodes:
        games = rawcodes.read().split('\n')
        
    for game in games:
        all_right = True
        game = format_game(game)
        for hands in game[1]:
            for color in hands:
                if hands[color]>max_hand[color]:
                    all_right = False
                    break
            if not all_right:
                break
        if all_right:       
            acum += int(game[0])
        
def power_cubes(file):
    
    
    
    sum=0
    
    with open(file, 'r') as rawcodes:
        games = rawcodes.read().split('\n')
        
    for game in games:
        acum=1
        max_hand = dict()
        game = format_game(game)
        for hands in game[1]:
           
            for color in hands:
      
                if color in max_hand:
               
                    max_hand[color] = max(hands[color],max_hand[color])
                else:
                    max_hand[color] = hands[color]
              
            
        for color in max_hand:      
            acum *= max_hand[color]
        sum += acum
       
    return sum
print(power_cubes('inputreto02-2.txt'))


    
