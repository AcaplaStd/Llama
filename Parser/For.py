# Llama - list-oriented programming language
# (C) Acapla Studios

import common

class node_for:
    """
    for <name of new var> = <expression from> to <expression to> step <expression step>
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
            if token.ttype == 45:  # WORD
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
            elif token.ttype == 27:  # {
                self.moment = 5
            else:
                self.to += token
        elif self.moment == 4:
            if token.ttype == 27:  # {
                self.moment = 5
            else:
                self.step += token
        elif self.moment == 5:
            if token.ttype == 28: # }
                # self.moment = 6 # the end!
                return True
            else:
                self.inside += token
