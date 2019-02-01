# cython: language_level=3
# distutils: language = c++

# Llama - list-oriented programming language
# (C) Acapla Studios

from libcpp cimport bool

import common
from .For import node_for

cdef list parse(list T, str mode):
    cdef list ast = []  # This is recursively function

    # ------------flags-segment--------------------------------------------------------------------------------
    cdef bool in_for = False  # Is busy
    # ------------flags-segment--------------------------------------------------------------------------------

    for token in T:
        if in_for:
            if ast[-1]._add_token(token):
                in_for = False  # Exit from node_for

                ast[-1]._from = parse(ast[-1]._from, "for_from")
                ast[-1].to = parse(ast[-1].to, "for_to")
                ast[-1].step = parse(ast[-1].step, "for_step")
                ast[-1].inside = parse(ast[-1].inside, "for_inside")
        else:  # Normal situation. All node checks are there
            if token.ttype == 44:  # For
                in_for = True
                ast.append(node_for())  # new node would be at the end of list
    return ast

cdef void debug(list AST, int level=1):
    if level == 1:
        print("<root>")

    cdef list node_result
    cdef str node_name
    cdef str param_appending
    cdef bool was_name_writen

    for node in AST:
        node_result = node.debug()
        node_name = node_result[0]
        param_appending = ""
        was_name_writen = False
        for params in node_result[1:]:
            if params[0]:
                param_appending += (" " + params[1] + "=\"" + str(params[2]) + "\"")
            else:
                if not was_name_writen:
                    was_name_writen = True
                    print(((level*4)*" ") + "<" + node_name + param_appending + ">")
                print(((level*4+2)*" ") + "<" + params[1] + ">")
                debug(params[2], level + 1)
                print(((level*4+2)*" ") + "</" + params[1] + ">")
        print(((level*4)*" ") + "</" + node_name + ">")

    if level == 1:
        print("</root>")
