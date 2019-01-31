# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

from libcpp cimport bool

cdef list digits = [ch for ch in "1234567890"]
cdef list letters = [ch for ch in "abcdefghijklmnopqrstuvwxyz"]
