# Llama - list-oriented programming language
# (C) Acapla Studios

import sys
import Lexer

__end_word = 'end'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        with open(fileName) as f:
            text = f.readlines()
            text = '\n'.join(text)
    else:
        print('\nERROR!\n')
        # Tm_A_T wants code to be done after each Enter pushed
        # But I can't do it!
        # Plz, Tm_A_T, do all your own ideas for yourself

    T = Lexer.lexer(text)
