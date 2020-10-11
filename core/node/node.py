from core.token.token import Token

class Node :

    def __init__ ( self, token, children=[], parent=None ) :
        self.children = children
        self.parent   = parent
        self.token    = token
        self.aberta   = True
        self.fechada  = True
        self.visitado = False

    def addChild ( self, child ) :
        if isinstance ( child, Token ) :
            self.children.append(Node(child, [], self))
        elif isinstance ( child, Node ) :
            self.children.append(child)

    def __str__ ( self ) :
        return '[ ' + str(self.token) + ' ]'

    def __repr__ ( self ) :
        return str(self)