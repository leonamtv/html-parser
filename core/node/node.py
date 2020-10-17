from core.token.token import Token

class Node :
    """
    Classe Node que modela os nós da class Arvore.
    """

    def __init__ ( self, token, children=[], parent=None ) :
        """
        Construtor que inicializa os atributos.
        """
        self.children = children
        self.parent   = parent
        self.token    = token

    def addChild ( self, child ) :
        """
        Adiciona um nó filho nos filhos.
        """
        if isinstance ( child, Token ) :
            self.children.append(Node(child, [], self))
        elif isinstance ( child, Node ) :
            self.children.append(child)

    def __str__ ( self ) :
        """
        Método toString()
        """
        return '[ ' + str(self.token) + ' ]'

    def __repr__ ( self ) :
        """
        Método que retorna como o obj será representado.
        """
        return str(self)