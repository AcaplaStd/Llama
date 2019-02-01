# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

from libcpp cimport bool

from .Lexer_settings import token_types

cdef class Token:
    def __init__(self, ttype, value=None):
        self.ttype = token_types[ttype]
        if value is not None:
            self.value = value

    def printIt(self):
        if hasattr(self, 'value'):
            print("ttype = "+str(self.ttype)+", value = " + str(self.value))
        else:
            print("ttype = "+str(self.ttype))
