def open_file(file_path):
    """
    The function `open_file` reads the contents of a file and returns it as a string, removing any
    leading or trailing whitespace.

    :param file_path: The file path is the location of the file that you want to open and read. It
    should be a string that specifies the path to the file, including the file name and extension. For
    example, "C:/Users/username/Documents/file.txt" or "data/file.csv"
    :return: the contents of the file as a string, with leading and trailing whitespace removed.
    """
    with open(file_path, "r") as file:
        return file.read().strip()
    
def mcm(num1, num2):
    """
    The function calculates the least common multiple (LCM) of two numbers using the Euclidean
    algorithm.
    
    :param num1: The first number for which you want to find the least common multiple (LCM)
    :param num2: The second number (num2) is the second integer input for which you want to find the
    least common multiple (LCM)
    :return: the least common multiple (LCM) of the two input numbers.
    """

    high_number = max(num1, num2)
    low_number = min(num1, num2)
    while low_number!=0:
        mcd = low_number
        low_number = high_number%low_number
        high_number = mcd

    mcm = num1* num2 / mcd
    return mcm

def string_to_dictionary(tabla):
    """
    The function `string_to_dictionary` takes a string input and converts it into a dictionary by
    splitting it into key-value pairs.

    :param tabla: The `tabla` parameter is a string that represents a table of data. Each line in the
    table represents a key-value pair, where the key and value are separated by " = ". The values are
    enclosed in square brackets and separated by commas
    :return: a dictionary called "clear_data" which contains key-value pairs.
    """
    clear_data = {}
    raw_files = tabla.split("\n")
    for file in raw_files:
        key, raw_values = file.split(" = ")
        clear_data[key] = raw_values[1:-1].split(", ")
    return clear_data


def haunted_wasteland(file):
    """
    The function `haunted_wasteland` takes in a file as input, reads the data from the file, processes
    the data according to certain rules, and returns a result.
    
    :param file: The `file` parameter is the name or path of the file that contains the raw data for the
    haunted wasteland
    :return: the result, which is the minimum common multiple (mcm) of the counters_list.
    """
    raw_data = open_file(file)
    directions_translate = {"L": 0, "R": 1}
    directions, raw_table = raw_data.split("\n\n")
    index = 0
    counter = 0
    format_data = string_to_dictionary(raw_table)
    pointers = list(filter(lambda x: x[2] == "A", list(format_data)))
    counters_list = []
    for pointer in pointers:
        while pointer[2] != "Z":
            counter += 1
            pointer = format_data[pointer][directions_translate[directions[index]]]
            
            if index == len(directions) - 1:
                index = 0
            else:
                index += 1
        counters_list.append(counter)
        counter = 0
        result = counters_list[0]
        
    for index in range(1, len(counters_list)):
        result = mcm(result, counters_list[index])
    return result



print(
    haunted_wasteland("/home/santiagomadaw/repositorios/adventofcode/reto08/input.txt")
)
