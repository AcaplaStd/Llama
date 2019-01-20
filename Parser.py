# Llama - list-oriented programming language
# (C) Acapla Studios

import common

ast = []


class _node_for:
    """
    for <name of new var> : <expression from> to <expression to> step <expression step>
    {
        <inside>
    }
    """
    def __init__(self):
        self.inside = []
        self.moment = 0

    def _add_token(self, _token):
        if self.moment == 0:
            if hasattr(_token, 'value') and common.is_normal_name(_token.value):
                self.moment = 1
            else:
                common.ERROR(
                    "You need to input new variable name before \":\" symbol")
        elif self.moment == 1:
            if _token.ttype == 34:  # :
                self.moment = 2
            else:
                common.ERROR(
                    "After new variable name you need to set \":\" symbol")




def _parse(T):
    for _token in  T:
        if _token.ttype == 44: # For
            pass
