from core.token import must_be_inside, self_closing_tags, limited_tokens

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
    
    def check_hierarchy ( self ) :
        if self.nome in must_be_inside :
            return must_be_inside[self.nome]
        return []

    def require_closing ( self ) :
        return not self.nome in self_closing_tags

    def check_if_limited ( self ) :
        return self.nome in limited_tokens