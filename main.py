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
        # text = ''
        # e = ''
        # while e != __end_word:
        #     e = input()
        #     text += e + '\n'
        # text = text[:-1]