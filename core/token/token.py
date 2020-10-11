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