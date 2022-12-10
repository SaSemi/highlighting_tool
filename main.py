import input
import helper
import split_text

START_TAG = "<b>"
END_TAG = "</b>"


def process_text(kind, text_input):
    """
    Highlights text according to the chosen kind.
    :param kind: int (0 or 1)
    :param text_input: string
    :return: string (highlighted text)
    """
    highlighted_text = ""
    for word in text_input.split():
        highlighted_text += handle_word(kind, word) + " "
    return highlighted_text


def handle_word(kind, word):
    """
    Helper function that highlights a single word according to the chosen kind.
    :param kind: int
    :param word: string (word that should be marked)
    :return: string (marked word)
    """
    if (helper.remove_punctuation(word)).isnumeric():
        return word
    if word.__contains__("-"):
        return handle_hyphen_word(kind, word, "-")
    if word.__contains__("—"):
        return handle_hyphen_word(kind, word, "—")

    chars = [x for x in word]
    beginning = helper.check_punctuation(chars, 0)
    end = helper.check_punctuation(chars, -1)

    marked_word = ""
    if beginning is not None:
        marked_word += beginning
    marked_word += add_tags(kind, helper.remove_punctuation(word))
    if end is not None:
        marked_word += end

    return marked_word


def handle_hyphen_word(kind, word, hyphen):
    """
    Handles words connected with hyphen.
    :param kind: int
    :param word: string
    :param hyphen: string (to deal with different kind of hyphens)
    :return: string (marked word)
    """
    word_l = word.split(hyphen)
    marked_word = ""
    for w in word_l[:-1]:
        marked_word += handle_word(kind, w) + hyphen
    marked_word += handle_word(kind, word_l[-1])
    return marked_word


def add_tags(kind, word):
    """
    Adds tags to a word depending of the chosen kind.
    :param kind: int
    :param word: string
    :return: string (marked word)
    """
    nb_to_mark = helper.compute_nb_of_bold_letters(len(word))
    if kind == input.MIDDLE:
        return mark_middle(word, nb_to_mark)
    elif kind == input.END:
        return mark_end(word, nb_to_mark)
    else:
        print("ERROR: WRONG KIND")
        exit()


def mark_middle(word, nb_to_mark):
    """
    Marks middle of a word.
    :param word: string
    :param nb_to_mark: int (number of characters to mark)
    :return: string (marked word)m
    """
    halved = int(nb_to_mark / 2)
    middle = int(len(word) / 2)
    first_p = word[:middle]
    second_p = word[middle:]

    if len(first_p) > 1:
        first_p = first_p[:-halved] + START_TAG + first_p[-halved:]
    else:
        first_p = first_p[-halved:] + START_TAG

    marked_word = first_p + (
            second_p[:nb_to_mark - halved] + END_TAG + second_p[nb_to_mark - halved:])
    return marked_word


def mark_end(word, nb_to_mark):
    """
    Marks end of word.
    :param word: string
    :param nb_to_mark: int (number of characters to mark)
    :return: string (marked word)
    """
    first_p = word[:-nb_to_mark]
    second_p = word[-nb_to_mark:]
    marked_word = first_p + START_TAG + second_p + END_TAG
    return marked_word


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kind = input.ask_for_kind()

    # for debugging:
    # input_string = input.ask_for_string()

    print("Marking contents of input file...")
    input_string = helper.read_file(helper.INPUT_FILE)
    output = process_text(kind, input_string)
    helper.write_to_file(helper.OUTPUT_FILE, output)
    print("Highlighted text was written to output file.")

    print("Printing splitted text:")
    split_text.split_text(helper.OUTPUT_FILE)
