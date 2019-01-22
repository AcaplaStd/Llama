# Llama - list-oriented programming language
# (C) Acapla Studios

import os
import re

def ERROR(string, code=1):
    os.system('color c')
    print('\n', 'ERROR ', code, ': ', string, '\n', sep='')
    print('[Exiting program]', '\n')
    exit(code)
