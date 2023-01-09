"""
Running the first function will split the text in output.txt into a list of sentences (to present chunk-by-chunk in PCIBex Controller).
The second function separates the sentences with the given separator.
"""
import nltk
# nltk.download('punkt')
import helper


def split_text(file):
    text = helper.read_file(file)
    token = nltk.tokenize.sent_tokenize(text)
    return token


def string_with_separator(file, separator):
    token = split_text(file)
    string = separator.join(token)
    return string
