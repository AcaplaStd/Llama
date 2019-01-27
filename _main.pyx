# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

import Lexer
import common
from Parser.Parser import parse, debug


__end_word = 'end'

cdef void _main(list argv):
    if len(sys.argv) > 1:
        cdef str fileName = argv[1]
        with open(fileName) as f:
            cdef str text = f.readlines()
            text = '\n'.join(text)

            cdef list T = Lexer.lexer(text)
            # For lexer tests
            # for t in T:
            #     t.printIt()
            cdef list AST = parse(T, "main")
            debug(AST)
    else:
        common.ERROR('No filename found', 228)
        # Tm_A_T wants code to be done after each Enter pushed
        # But I can't do it!
        # Plz, Tm_A_T, do all your own ideas for yourself
