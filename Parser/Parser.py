# Llama - list-oriented programming language
# (C) Acapla Studios

import common
from Parser.For import node_for

ast = []

# ------------flags-segment--------------------------------------------------------------------------------
in_for = False
# ------------flags-segment--------------------------------------------------------------------------------


def parse(T):
    global ast
    for token in T:
        if token.ttype == 44:  # For
            pass
    return ast
