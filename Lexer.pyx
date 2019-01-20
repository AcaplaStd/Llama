# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

from libcpp cimport bool

import re
import common

cdef str _symbols = ';:.,%?^{}()[]'  # You can't use these symbols with others
cdef str _com_sym = '=+-*/!<>|&'     # These symbols can be combined with others
cdef str _quotes = "\"'"
cdef str _spaces = ' \n\t\v\r\f'
cdef dict _token_types = {'INT': 0, 'FLOAT': 1, 'STR': 2, 'BOOL': 40, 'WORD': 45,
                '//': 3, '/*': 4, '*/': 5, '=': 6, '==': 7, '+': 8, '+=': 9, '++': 10, '-': 11, '-=': 12, '--': 13,
                '*': 14, '*=': 15, '/': 16, '/=': 17, '!': 18, '!=': 19, '^': 20, '<': 21, '<=': 22, '>': 23, '>=': 24,
                '||': 25, '&&': 26, '{': 27, '}': 28, '(': 29, ')': 30, '[': 31, ']': 32, ';': 33, ':': 34,
                '.': 35, ',': 36, '%': 37, '?': 38, 'print': 39, 'for': 44, 'while': 41, 'to': 42, 'step': 43}


cdef list tokens = []


class Token:
    def __init__(self, ttype, value=None):
        self.ttype = _token_types[ttype]
        if value is not None:
            self.value = value

    def printIt(self):
        if hasattr(self, 'value'):
            print("ttype = "+str(self.ttype)+", value = " + str(self.value))
        else:
            print("ttype = "+str(self.ttype))


cdef void check(str word):
    global tokens

    cdef list simple_syms = ['//', '/*', '*/', '=', '==', '+', '+=', '++', '-', '-=', '--', '*', '*=', '/', '/=', '!', '!=',
                   '^', '<', '<=', '>', '>=', '||', '&&', '{', '}', '(', ')', '[', ']',
                   ';', ':', '.', ',', '%', '?', '^', 'print', 'for', 'while', 'to', 'step']

    for x in simple_syms:
        if word == x:
            tokens.append(Token(x))
            break
    else:
        if re.fullmatch('[-^+]?[\d^0]+', word):
            tokens.append(Token('INT', int(word)))
        elif re.fullmatch('[-^+]?[\d^0]+\.\d+', word):
            tokens.append(Token('FLOAT', float(word)))
        elif len(word) >= 2 and word[0] == word[-1] == "'" and word[1:-1].count("'") == 0:  # \
            tokens.append(Token('STR', word[1:-1]))                                         #  \ This is VERY UGLY variant for STR
        elif len(word) >= 2 and word[0] == word[-1] == '"' and word[1:-1].count('"') == 0:  #  / Plz make it normally
            tokens.append(Token('STR', word[1:-1]))                                         # /
        elif word == 'true':
            tokens.append(Token('BOOL', True))
        elif word == 'false':
            tokens.append(Token('BOOL', False))

        else:
            if word[0].isdigit():
                common.ERROR('Illegal word ' + word, 111)
            else:
                tokens.append(Token('WORD', word))


cdef list _lexer(str text):
    global tokens
    tokens = []
    cdef str buff = ''
    cdef int i = 0
    cdef bool string = False
    cdef bool combine = False
    cdef str quote = ''
    while i < len(text):
        c = text[i]
        if string:
            buff += c
            if c == quote:
                check(buff)
                buff = ''
                string = False
        elif combine:
            if c == '-':
                check(buff)
                buff = c
            elif c in _com_sym:
                buff += c
            else:
                check(buff)
                buff = c
                combine = False
        else:
            if c in _spaces:
                check(buff)
                buff = ''
            elif c in _quotes:
                string = True
                buff += c
            elif c in _symbols:
                check(buff)
                tokens.append(Token(c))
                buff = ''
            elif c in _com_sym:
                combine = True
                check(buff)
                buff = c
            else:
                buff += c
            i += 1
    return tokens

def lexer(text):
    return _lexer(text)