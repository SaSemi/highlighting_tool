"""
Running this script will split the text in output.txt into a list of sentences (to present chunk-by-chunk).
"""
import nltk
# nltk.download('punkt')
import helper

SPLIT_FILE = "split.txt"

def split_text():
    text = helper.read_file(helper.OUTPUT_FILE)
    token = nltk.tokenize.sent_tokenize(text)
    print(token)

