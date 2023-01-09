"""
Use this script to strip a string from certain BBCode-Tags and turn Bold tags into HTML tags.

Write the string you want to convert into the BBCODE_TO_HTML input file.
The output will be written into the BBCODE_TO_HTML output file.
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
no_size = remove_tags('\[SIZE=.*?]', '\[/SIZE]', no_font)
no_space = clean_spaces(no_size)

# convert bold tags
fin = replace_bold_with_html(no_space)

# write to file and format text
helper.write_to_file(BBCODE_TO_HTML_OUT, fin)

#helper.write_to_file(BBCODE_TO_HTML_OUT, split_text.string_with_seperator(BBCODE_TO_HTML_OUT, "|"))