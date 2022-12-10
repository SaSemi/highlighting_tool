"""
Use this script to strip a string from certain BBCode-Tags and turn Bold tags into HTML tags.

Write the string you want to convert into the BBCODE_TO_HTML file.
The output will be written into the same file.
Additionally a version with split sentences will be printed out.
"""

import re
import helper
import split_text

BBCODE_TO_HTML_IN = "bb_to_html_input"
BBCODE_TO_HTML_OUT = "bb_to_html_output"


def remove_tags(begginning, closing, s):
    clean = re.sub(begginning, "", s)
    clean = re.sub(closing, "", clean)
    return clean


def replace_bold_with_html(s):
    pattern = r'\[B](.*?)\[/B]'
    replacement = r'<b>\1</b>'
    clean = re.sub(pattern, replacement, s)
    return clean


def clean_spaces(s):
    clean = re.sub(" ", " ", s)
    return clean


s = helper.read_file(BBCODE_TO_HTML_IN)
# remove tags
no_color = remove_tags('\[COLOR=.*?]', '\[/COLOR]', s)
no_font = remove_tags('\[FONT=.*?]', '\[/FONT]', no_color)
no_space = clean_spaces(no_font)

# convert bold tags
fin = replace_bold_with_html(no_space)
print(fin)

# write to file and split text
helper.write_to_file(BBCODE_TO_HTML_OUT, fin)
split_text.split_text(BBCODE_TO_HTML_OUT)
