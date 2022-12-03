MIDDLE = 0
END = 1


def ask_for_kind():
    """
    Ask user where/how text should be highlighted.
    :return: int (0 or 1)
    """
    print("Where do you want your text to be highlighted?\n"
          "middle (m)\n"
          "end (e)")
    kind_input = input()
    kind_setting = process_kind_input(kind_input)
    return kind_setting


def process_kind_input(kind):
    """
    Process user input.
    :param kind: string (user input)
    :return: int (0 or 1)
    """
    if kind == "m" or kind == "middle":
        return MIDDLE
    elif kind == "e" or kind == "end":
        return END
    else:
        return incorrect_kind_input()


def incorrect_kind_input():
    """
    Deal with incorrect user input when setting kind of highlighting.
    :return: int 0 or 1
    """
    print("Input could not be processed. Please press keys 'm' or 'e'\n"
          "middle (m)\n"
          "end (e)")
    new_kind = input()
    return process_kind_input(new_kind)


# used for debugging
def ask_for_string():
    """
    Ask user for a string/text to highlight.
    :return: string (user input)
    """
    print("Please enter the text, that should be highlighted:")
    string = input()
    return string
