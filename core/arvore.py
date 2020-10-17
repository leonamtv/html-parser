from core.node.node import Node
from core.token.token import Token
from core.token.token_comentario import TokenComentario
from core.token.token_abertura import TokenAbertura
from core.token.token_fechamento import TokenFechamento
from core.token.token_dado import TokenDado
from core.token.token_declaracao import TokenDecl

class Arvore : 
    """
    Classe Arvore. Constrói uma árvore que representa a estrutura hie-
    rárquica do HTML através de uma lista de tokens recebida como pa-
    râmetro do construtor.
    """

    def __init__ ( self, tokens=[], verbose=False ) :
        """
        Construtor da classe Arvore. Recebe como parâmetros uma lista
        de tokens.
        """
        if len ( tokens ) > 0 :
            generalTag = Token('documento')
            self.root = Node(generalTag, children=[], parent=None)
            try:
                self.build_from_tokens(tokens)
                if verbose :
                    self.print_arvore()
            except Exception as e :
                print('Erro: ' + str(e))
        else :
            print('Lista de tokens vazia.')
            
    def build_from_tokens ( self, tokens ) :
        """
        Este método constrói iterativamente uma árvore n-ária através 
        de uma fila de tokens HTML. O método itera sobre a fila de to-
        kens, verifica de qual tipo eles são, e de acordo com isso, a-
        diciona os nós à árvore.

        O método também verifica os erros do tipo:

            - Abertura de tags sem fechamento;
            - Fechamento de tags sem abertura;
            - Hierarquia de tags anatômicas;
            - Contagem de tags que podem ser abertas somente uma vez.
        """

        # Mapa utilizado para verificação de hierarquia de tags anatômicas
        tags_map = {}
        # Mapa utilizado para verificação do número de vezes que determina-
        # das tags foram abertas.
        limited_tags_count = {}

        # Nó atual da árvore
        current_node = self.root

        # Pilha utilizada para armazenar os nós abertos
        pilha = [ ]

        def verify_limit ( token ) :
            """
            Essa função verifica se o token recebido por parâmetro atra-
            vés de um método da classe Token (check_if_limited), e caso
            seja limitado, verifica no mapa 'limited_tags_count' se ele
            já foi ou não aberto. Caso seja aberto mais de uma vez, uma
            exceção é disparada.
            """
            if token.check_if_limited () :
                if token.nome in limited_tags_count :
                    if limited_tags_count[token.nome] > 1 :
                        raise Exception('O token ' + str(token) + ' não pode ser aberto mais de uma vez.')

        def verify_anatomy ( token ) :
            """
            Essa função verifica se o token recebido por parâmetro requer
            estar dentro de outras tags específicas do html (head precisa
            estar dentro de html, body precisa estar dentro de html etc.).
            Caso seja verdadeiro, utilizamos o mapa 'tags_map' para veri-
            ficar se estamos atualmente dentro de uma dessas tags pai.
            """
            hierarchy = token.check_hierarchy()
            if not any([ tags_map[name] > 0 for name in hierarchy if name in tags_map ]) :
                if len(hierarchy) > 1 :
                    raise Exception ( 'Tag ' + str(token.nome) + ' deve ser declarada dentro de uma dessas tags: ' + str(hierarchy) )
                elif len(hierarchy) == 1:
                    raise Exception ( 'Tag ' + str(token.nome) + ' deve ser declarada dentro da tag ' + str(hierarchy[0]) )

        def update_closing ( token ) :
            """
            Função auxiliar do método 'verify anatomy'. Através deste mé-
            todo, atualizamos o mapa 'tags_map' com a tag de fechamento.
            """
            if token.nome in tags_map :
                if tags_map[token.nome] > 0 :
                    tags_map[token.nome] -= 1    
            else :
                raise Exception('Tag ' + str(token) + ' fechada e não aberta')

        def update_opening ( token ) :
            """
            Função auxiliar dos métodos 'verify_anatomy' e 'verify_limit'. 
            Ela atualiza ambos os mapas 'limited_tags_count' e 'tags_map'
            com o token de abertura de tag recebido por parâmetro.
            """
            if token.nome in limited_tags_count :
                limited_tags_count[token.nome] += 1
            else :
                limited_tags_count[token.nome] = 1
            if token.nome in tags_map :
                tags_map[token.nome] += 1
            else :  
                tags_map[token.nome] = 1

        for i, token in enumerate(tokens) :
            # Verifica se a tag atual respeita a hierarquia
            verify_anatomy(token)
            if isinstance(token, TokenAbertura) :
                # Caso a tag seja do tipo abertura
                update_opening(token)
                verify_limit(token)
                new_node = Node(token, [], current_node)
                current_node.addChild(new_node)
                current_node = new_node
                if not token.require_closing() and current_node.parent != None:
                    current_node = current_node.parent
                if token.require_closing():
                    pilha.append(token)
            elif isinstance(token, TokenFechamento) :
                # Caso a tag seja do tipo fechamento
                update_closing(token)
                if not token.require_closing () :
                    continue
                if len(pilha) > 0 :
                    if not token.require_closing () :
                        pilha.pop()
                    elif pilha[-1].isComplemento(token)  :
                        pilha.pop()
                    elif not pilha[-1].isComplemento(token) :
                        if not any([ tok.isComplemento(token) for tok in pilha ]) :
                            raise Exception(str(token) + ': tag fechada e não aberta')
                        else :
                            raise Exception(str(pilha[-1]) + ': tag aberta e não fechada')
                    else :
                        raise Exception(str(pilha[-1]) + ': tag aberta e não fechada')
                if current_node.parent != None :
                    current_node = current_node.parent
            elif isinstance(token, TokenDado) :
                # Caso a tag seja do tipo dado
                current_node.addChild(token)
            elif isinstance(token, TokenDecl) :
                # Caso a tag seja do tipo declaração
                current_node.addChild(token)

    def print_arvore (self) :
        """
        Método para printar a árvore. A impressão acontecerá assim:

        Pai_1 -> { filho_1, filho_2, ... }
        Pai_2 -> { filho_1, filho_2, ... }
        ...

        """
        self._print_arvore(self.root)

    def _print_arvore ( self, node ) :
        """
        Método recursivo auxiliar do método 'print_arvore'. Este 
        método que faz a impressão de fato.
        """
        if len(node.children) > 0 :
            for child in node.children :
                self._print_arvore(child)
            print(str(node) + ' -> { ', end='')
            for child in node.children :
                print(str(child) + ' ', end='')
            print(' }')
        else :
            print(str(node) + ' -> { }')


