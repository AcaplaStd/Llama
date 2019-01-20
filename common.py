# Llama - list-oriented programming language
# (C) Acapla Studios

import os
import re

def ERROR(string, code=1):
    os.system('color c')
    print('\n', 'ERROR ', code, ': ', string, '\n', sep='')
    print('[Exiting program]', '\n')
    exit(code)

def is_normal_name(name):
    if (name is str) and re.fullmatch(r'[\w_][\w\d_]*', name):
        return True