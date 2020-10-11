self_closing_tags = [ 'area', 'base', 'br', 'col', 'embed', 'hr', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'command', 'keygen', 'menuitem']

class Token:
    """
    Classe genérica de tokens.
    """

    def __init__(self, nome: str):
        """
        Construtor com apenas o nome
        da tag.
        """
        self.nome = nome
    
    def __str__(self):
        """
        Retorna o nome do token.
        """
        return self.nome
    
    def require_closing ( self ) :
        return not self.nome in self_closing_tags