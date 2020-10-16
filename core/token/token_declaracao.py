from core.token.token import Token

class TokenDecl(Token):
    """
    Classe que modela um token de 
    declaração.
    """

    def __init__( self, nome: str ):
        """
        Inicializa o objeto com o nome 
        e os atributos.
        """
        Token.__init__(self, nome)

    def __str__ ( self ):
        """
        Monta uma string com o nome da
        tag.
        """
        return '< DECL TAG: ' + self.nome + ' >'
   