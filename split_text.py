"""
Running this function will split the text in output.txt into a list of sentences (to present chunk-by-chunk in PCIBex Controller).
"""

import nltk
# nltk.download('punkt')
import helper


def split_text(file):
    text = helper.read_file(file)
    token = nltk.tokenize.sent_tokenize(text)
    print(token)
