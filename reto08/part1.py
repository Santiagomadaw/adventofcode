def open_file(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


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
    The function `haunted_wasteland` takes a file as input, reads the data from the file, and uses the
    data to navigate through a haunted wasteland until reaching a specific location, counting the number
    of steps taken.
    
    :param file: The `file` parameter is the name or path of the file that contains the raw data for the
    haunted wasteland
    :return: the value of the counter variable.
    """
    raw_data = open_file(file)
    directions_translate = {"L": 0, "R": 1}
    directions, raw_table = raw_data.split("\n\n")
    index = 0
    counter = 0
    format_data = string_to_dictionary(raw_table)
    pointer = "GSA"
    print(pointer)
    while pointer != "SPZ":
        counter += 1
        
        pointer = format_data[pointer][directions_translate[directions[index]]]
        if index == len(directions) - 1:
            index = 0
        else:
            index += 1  
    return counter


print(
    haunted_wasteland("/home/santiagomadaw/repositorios/adventofcode/reto08/input.txt")
)
