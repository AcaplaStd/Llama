# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

from libcpp cimport bool

from sys import setrecursionlimit

import common
from Parser.For import node_for

setrecursionlimit(2147483647)  # Если кто захочет снести, я не возражаю

# ------------flags-segment--------------------------------------------------------------------------------
cdef bool in_for = False  # Is busy
# ------------flags-segment--------------------------------------------------------------------------------


cdef list parse(list T):
    cdef list ast = []  # This is recursively function
    for token in T:
        if in_for:
            if ast[-1]._add_token(token):
                in_for = False  # Exit from node_for

                # TODO: recursively browse
                # How can i do it?
                # I can use THIS def and call it for everyone node component
                # Returned ast will be appended into node component's container

        else:  # Normal situation. All node checks are there
            if token.ttype == 44:  # For
                in_for = True
                ast.append(node_for())  # new node would be at the end of list
    return ast
