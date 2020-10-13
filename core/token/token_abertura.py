from core.token.token import Token
from core.token.token_fechamento import TokenFechamento

class TokenAbertura(Token):
    """
    Classe que modela um token de 
    abertura de tags.
    """

    def __init__( self, nome: str, attrs ):
        """
        Inicializa o objeto com o nome 
        e os atributos.
        """
        Token.__init__(self, nome)
        self.attrs = attrs

    def __str__ ( self ):
        """
        Monta uma string com o nome da
        tag e seus atributos, caso haja
        algum.
        """
        result = self.nome
        for attr in self.attrs:
            if attr[0] != None :
                result += " | " + attr[0]
            if attr[1] != None :
                result += " = " + attr[1]
        return '< ABRE TAG: ' + result + ' >'

    def isComplemento ( self, token ) :
        if not isinstance ( token, TokenFechamento ) :
            return False
        if token.nome != self.nome :
            return False
        return True

   