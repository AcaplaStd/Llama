# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

from .Lexer.Lexer import lexer
import common
from .Parser.Parser import parse, debug


__end_word = 'end'

cdef void main(list argv):
    cdef str fileName
    cdef str text
    cdef list T
    cdef list AST
    if len(argv) > 1:
        fileName = argv[1]
        with open(fileName, "r", "utf=8") as f:
            text = f.read()

            T = lexer(text)
            # For lexer tests
            # for t in T:
            #     t.printIt()
            AST = parse(T, "main")
            debug(AST)
    else:
        common.ERROR('No filename found', 228)
        # Tm_A_T wants code to be done after each Enter pushed
        # But I can't do it!
        # Plz, Tm_A_T, do all your own ideas for yourself
