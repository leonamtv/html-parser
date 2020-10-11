from core.token.token import Token

class TokenComentario ( Token ):
    """
    Classe que modela um token de 
    comentário.
    """

    def __init__(self, dado):
        """
        Construtor com o nome da tag 
        e o dado.
        """
        Token.__init__(self, 'comentário')
        self.dado = dado
    
    def __str__ (self):
        """
        Monta string com o dado do
        comentário.
        """
        return '< COMENTÁRIO: ' + self.dado + ' >'