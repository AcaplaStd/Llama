# Llama - list-oriented programming language
# (C) Acapla Studios

import sys
import Lexer
import common
import Parser.Parser


__end_word = 'end'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        with open(fileName) as f:
            text = f.readlines()
            text = '\n'.join(text)

            T = Lexer.lexer(text)
            for t in T:
                t.sstr__()
    else:
        common.ERROR('No filename found', 228)
        # Tm_A_T wants code to be done after each Enter pushed
        # But I can't do it!
        # Plz, Tm_A_T, do all your own ideas for yourself
