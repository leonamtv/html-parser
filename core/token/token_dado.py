from core.token.token import Token

class TokenDado (Token):    
    """
    Classe que modela um token de 
    dados.
    """
    
    def __init__ ( self, dado ):
        """
        Construtor com o nome da 
        tag e o dado desta.
        """
        Token.__init__(self, 'dado')
        self.dado = dado

    def __str__ ( self ):
        """
        Monta string com o dado.
        """
        return '< DADO: ' + self.dado + ' >'