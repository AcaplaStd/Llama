# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

from libcpp cimport bool

import common
from Parser.For import node_for

cdef list ast = []

# ------------flags-segment--------------------------------------------------------------------------------
cdef bool in_for = False
# ------------flags-segment--------------------------------------------------------------------------------


cdef list _parse(list T):
    global ast
    for token in T:
        if token.ttype == 44:  # For
            pass
    return ast

def parse(T):
    return _parse(T)