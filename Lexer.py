# Llama - list-oriented programming language
# (C) Acapla Studios

import re

_spaces = ' \n\t\v\r'
_token_types = {'//': 0, '/*': 1, '*/': 2,
                'INT': 3, 'FLOAT': 4, 'STR': 5}
tokens = []


class Token:
    def __init__(self, type):
        self.type = _token_types[type]

    def __init__(self, type, value):
        self.type = _token_types[type]
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
    while i < len(text):
        c = text[i]
        if c in _spaces:
            check(buffer)
            buffer = ''
        else:
            buffer += c