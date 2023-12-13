def open_file(file_path):
    """
    The `play_camel` function reads a file containing hands of cards, calculates the points for each
    hand, and prints the hands in order of their points value along with their corresponding position
    and cumulative score.

    :param file_path: The `file_path` parameter is a string that represents the path to the file that
    contains the hands of cards
    :return: The code does not explicitly return anything. However, it prints the length of the ordered
    hands, the ordered hands themselves, and the result.
    """
    with open(file_path, "r") as file:
        return file.read()


def tokenize(string_hands):
    """
    The `tokenize` function takes a string of hands, splits it into a list of hands, and then creates a
    dictionary where the keys are the first word of each hand and the values are the second word of each
    hand.

    :param string_hands: The `string_hands` parameter is a string that contains multiple lines of text.
    Each line represents a hand and consists of two parts separated by a space. The first part is the
    name of the hand, and the second part is the value of the hand
    :return: The function `tokenize` returns a dictionary `dict_hands` where the keys are the first word
    of each line in `string_hands` and the values are the second word of each line.
    """
    list_hands = string_hands.strip().split("\n")
    dict_hands = {}
    for hand in list_hands:
        dict_hands[hand.split()[0]] = hand.split()[1]

    return dict_hands


def cart_counter(cards):
    """
    The function `cart_counter` takes a list of cards as input and returns the number of cards in the
    list.
    
    :param cards: The `cards` parameter is a list of strings representing different items in a shopping
    cart. Each string represents an item in the cart
    """

    card_values = {
        "A": "e",
        "K": "d",
        "Q": "c",
        "J": "b",
        "T": "a",
        "9": "9",
        "8": "8",
        "7": "7",
        "6": "6",
        "5": "5",
        "4": "4",
        "3": "3",
        "2": "2",
    }
    new_dict = {}
    hand_value = ""
    for char in cards:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
        hand_value += card_values[char]
    return new_dict, hand_value


def points_hand(hand):
    """
    The function `points_hand` calculates the points for a given hand of cards based on the number of
    occurrences of each card value.

    :param hand: The `hand` parameter is a list of cards in a hand. Each card is represented as a string
    :return: a string that represents the points value of a hand in a card game.
    """
    games_value = {
        "7": "7",
        "6": "6",
        "5": "5",
        "4": "3",
        "3": "4",
        "2": "2",
        "0": "1",
    }

    result = 0
    hand_dict, hand_value = cart_counter(hand)
    for key, value in hand_dict.items():
        if value == 5:
            result = 7
        elif value == 4:
            result = 6
        elif value == 3:
            result += 3
        elif value == 2:
            result += 2
        elif value == 1:
            result += 0
    return games_value[str(result)] + hand_value


def play_camel(file):
    """
    The function `play_camel` takes a file as input, tokenize the contents of the file, assigns points
    to each hand, orders the hands based on their points, and calculates a result based on the order and
    points of the hands.

    :param file: The `file` parameter in the `play_camel` function is the name or path of the file that
    contains the hands to be played in the game of Camel
    """
    play_hands = tokenize(open_file(file))

    valued_hands = {}
    for hand in play_hands:
        valued_hands[hand] = points_hand(hand)
    ordered_hands = valued_hands.items()
    ordered_hands = sorted(ordered_hands, key=lambda item: item[1])
    print(len(ordered_hands))
    result = 0
    for i in range(len(ordered_hands)):
        print((i + 1), ordered_hands[i])
        result += (i + 1) * int(play_hands[ordered_hands[i][0]])
    return result


print(play_camel("/home/santiagomadaw/repositorios/adventofcode/reto07/input.txt"))
