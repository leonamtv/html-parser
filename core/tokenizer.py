from html.parser import HTMLParser
from collections import deque
from core.token.token_abertura import TokenAbertura
from core.token.token_fechamento import TokenFechamento
from core.token.token_dado import TokenDado
from core.token.token_comentario import TokenComentario

class Tokenizer (HTMLParser):
    """
    Classe filho de HTMLParser (nativo do python3)
    para lidar com os diferentes tipos de tokens 
    existentes num arquivo HTML passado através do
    método 'feed()'.
    """

    def __init__(self, ignore_comments: bool = True):
        """
        Chama o construtor da classe pai e inicia-
        liza a fila de tokens.

        Caso ignore_comments seja = False, adicio-
        na os comentários na fila.
        """
        HTMLParser.__init__(self)
        self.fila = deque()
        self.ignore_comments = ignore_comments
    
    def handle_starttag (self, tag, attrs):
        """
        Gerencia o processo de parsing do token de
        tag abrindo e seus atributos caso haja al-
        gum.

        Exemplo: <h1>, <p>, <input type='text'>
        """

        tag_token = TokenAbertura(tag, attrs)

        self.fila.append(tag_token)

    def handle_endtag (self, tag):
        """
        Gerencia o processo de parsing do token de 
        tag fechando.

        Exemplo: </h1>, <body>
        """

        tag_token = TokenFechamento(tag)

        self.fila.append(tag_token)

    def handle_data (self, data):
        """
        Gerencia o processo de parsing do token de 
        dado, como texto plano.
        """

        if not str(data).isspace():
            tag_token = TokenDado(data.lstrip().rstrip())

            self.fila.append(tag_token)

    def handle_comment(self, data):
        """
        Gerencia o processo de parsing do token de 
        comentários:

        Exemplo: <!-- comentário -->
        """
        
        if not self.ignore_comments:

            tag_token = TokenComentario(data)

            self.fila.append(tag_token)

    def get_fila (self):
        """
        Retorna a fila de tokens
        """

        return self.fila

    def __getitem__(self, index):
        """
        Magic Method para o interpretador python 
        chamar quando nos referimos a um objeto do
        tipo Tokenizer como vetor:

        Exemplo: 
            obj = Tokenizer()
            ...
            print(obj[2]) # chama o método atual
                          # com index = 2
        """
        try:
            return self.fila[index]
        except IndexError:
            print('Índice fora dos valores permitidos.')
    
    def __str__ (self):
        """
        Retorna a versão em string da fila de to-
        kens.
        """
        return ''.join([ ( str(token) + '\n' ) for token in self.fila ])