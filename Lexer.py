# Llama - list-oriented programming language
# (C) Acapla Studios

import re

_symbols = ';:,|&%#'    # You can't use these symbols with others
# _com_sym = '=+-*/!<>?\' # These symbols can be combined with others
_quotes = '"' + "'"
_spaces = ' \n\t\v\r'
_token_types = {'//': 0, '/*': 1, '*/': 2,
                'INT': 3, 'FLOAT': 4, 'STR': 5,
                ';': 6}
tokens = []


class Token:
    def __init__(self, type, value = None):
        self.type = _token_types[type]
        if value is not None:
            self.value = value


def check(word):
    global tokens
    if word == '//':
        tokens.append(Token('//'))
    elif word == '/*':
        tokens.append(Token('/*'))
    elif word == '*/':
        tokens.append(Token('*/'))

    elif word.isdigit():
        tokens.append(Token('INT', int(word)))
    elif re.fullmatch('[\d^0]+\.\d+', word):
        tokens.append(Token('FLOAT', float(word)))
    # There should be case for STR



def lexer(text: str):
    buffer = ''
    i = 0
    string = False
    quote = ''
    while i < len(text):
        c = text[i]
        if string:
            buffer += c
            if c == quote:
                check(buffer)
                buffer = ''
                string = False
        else:
            if c in _spaces:
                check(buffer)
                buffer = ''
            elif c in _quotes:
                string = True
                buffer += c

            else:
                buffer += c
