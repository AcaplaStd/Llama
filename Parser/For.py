# Llama - list-oriented programming language
# (C) Acapla Studios

import common

class node_for:
    """
    for <name of new var> : <expression from> to <expression to> step <expression step>
    {
        <inside>
    }
    """

    def __init__(self):
        self.step = None
        self.to = None
        self._from = None
        self.inside = []
        self.moment = 0

    def _add_token(self, token):
        if self.moment == 0:
            if token.ttype == 45:
                self.moment = 1
            else:
                common.ERROR(
                    "You need to input new variable name before \":\" symbol")
        elif self.moment == 1:
            if token.ttype == 6:  # =
                self.moment = 2
            else:
                common.ERROR(
                    "After new variable name you need to set \":\" symbol")
        elif self.moment == 2:
            if token.ttype == 42:  # to
                self.moment = 3
            else:
                self._from += token
        elif self.moment == 3:
            if token.ttype == 43:  # step
                self.moment = 4
            else:
                self.to += token
