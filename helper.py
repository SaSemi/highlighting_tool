PUNCTUATION = [",", ".", ';', "!", "?", ":", '"', '„', "“", "”"]

INPUT_FILE = "input"
OUTPUT_FILE = "output"


def check_punctuation(word_l, index):
    """
    Checks if specific index in a word (as list) is a punctuation
    :param word_l: list
    :param index: int
    :return: None when not punctuation, else punctuation as string
    """
    removed = ""
    while word_l[index] in PUNCTUATION:
        removed += word_l.pop(index)
    return (removed[::-1]) # needs to be reversed


def remove_punctuation(word):
    """
    Removes punctuation from word.
    :param word: string
    :return: string
    """
    for c in PUNCTUATION:
        word = word.replace(c, "")
    return word


def compute_nb_of_bold_letters(word_len):
    """
    Computes the number of letters that should be marked, depending on word length
    :param word_len: int
    :return: int
    """
    if word_len <= 3:
        return 1
    elif word_len == 4:
        return 2
    else:
        # If there are > 4 letters, 40% of all letters are bold
        return int(word_len * 0.4)


def read_input_file():
    """
    Reads in contents of input file.
    :return: string
    """
    with open(INPUT_FILE, mode="r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    string = ""
    for line in lines:
        line = line.replace("\n", " ")
        string += line

    return string


def write_to_output_file(output):
    """
    Writes output to output file.
    :param output: string
    """
    with open(OUTPUT_FILE, mode="w", encoding="utf-8") as output_file:
        output_file.write(output)
