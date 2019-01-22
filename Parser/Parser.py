# Llama - list-oriented programming language
# (C) Acapla Studios

import common
from Parser.For import node_for

ast = []


def _parse(T):
    for _token in  T:
        if _token.ttype == 44: # For
            pass
