# Llama - list-oriented programming language
# (C) Acapla Studios

import re

_symbols = ';:.,%?^'    # You can't use these symbols with others
_com_sym = '=+-*/!<>|&'  # These symbols can be combined with others
_quotes = '"' + "'"
_spaces = ' \n\t\v\r\f'
_token_types = {'INT': 0, 'FLOAT': 1, 'STR': 2,
                '//': 3, '/*': 4, '*/': 5, '=': 6, '==': 7, '+': 8, '+=': 9, '++': 10, '-': 11, '-=': 12, '--': 13,
                '*': 14, '*=': 15, '/': 16, '/=': 17, '!': 18, '!=': 19, '^': 20,
                '<': 21, '<=': 22, '>': 23, '>=': 24, '||': 25, '&&': 26}
tokens = []


class Token:
    def __init__(self, type, value=None):
        self.type = _token_types[type]
        if value is not None:
            self.value = value


def check(word):
    global tokens

    simple_syms = ['//', '/*', '*/', '=', '==', '+', '+=', '++', '-', '-=', '--', '*', '*=', '/', '/=', '!', '!=',
                   '^', '<', '<=', '>', '>=', '||', '&&']

    for x in simple_syms:
        if word == x:
            tokens.append(Token(x))
            break
    else:
        if word.isdigit():
            tokens.append(Token('INT', int(word)))
        elif re.fullmatch('[\d^0]+\.\d+', word):
            tokens.append(Token('FLOAT', float(word)))
        # There should be case for STR


def lexer(text: str):
    buffer = ''
    i = 0
    string = False
    combine = False
    quote = ''
    while i < len(text):
        c = text[i]
        if string:
            buffer += c
            if c == quote:
                check(buffer)
                buffer = ''
                string = False
        elif combine:
            if c in _com_sym:
                buffer += c
            else:
                check(buffer)
                buffer = c
                combine = False
        else:
            if c in _spaces:
                check(buffer)
                buffer = ''
            elif c in _quotes:
                string = True
                buffer += c
            elif c in _symbols:
                check(buffer)
                tokens.append(Token(_token_types[c]))
                buffer = ''
            elif c in _com_sym:
                combine = True
                check(buffer)
                buffer = c
            else:
                buffer += c
            i += 1
    return tokens
