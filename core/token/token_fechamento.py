from core.token.token import Token

class TokenFechamento(Token):
    """
    Classe que modela um token de 
    fechamento de tags.
    """

    def __init__ (self, nome):
        """
        Construtor com apenas o nome
        da tag.
        """
        Token.__init__(self, nome)

    def __str__ (self):
        """
        Monta string com o nome da tag
        """
        return '< FECHA TAG: ' + self.nome + ' >'
