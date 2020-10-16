from core.node.node import Node
from core.token.token import Token
from core.token.token_comentario import TokenComentario
from core.token.token_abertura import TokenAbertura
from core.token.token_fechamento import TokenFechamento
from core.token.token_dado import TokenDado

class Arvore : 

    def __init__ ( self, tokens=[] ) :
        if len ( tokens ) > 0 :
            generalTag = Token('documento')
            self.root = Node(generalTag, children=[], parent=None)
            try:
                self.build_from_tokens(tokens)
                self.print_arvore()
            except Exception as e :
                print('Erro: ' + str(e))
            
    def build_from_tokens ( self, tokens ) :
        
        tags_map = {}
        limited_tags_count = {}

        current_node = self.root

        pilha = [ ]

        def verify_limit ( token ) :
            if token.check_if_limited () :
                if token.nome in limited_tags_count :
                    if limited_tags_count[token.nome] > 1 :
                        raise Exception('O token ' + str(token) + ' não pode ser aberto mais de uma vez.')

        def verify_anatomy ( token ) :
            hierarchy = token.check_hierarchy()
            if not any([ tags_map[name] > 0 for name in hierarchy if name in tags_map ]) :
                if len(hierarchy) > 1 :
                    raise Exception ( 'Tag ' + str(token.nome) + ' deve ser declarada dentro de uma dessas tags: ' + str(hierarchy) )
                elif len(hierarchy) == 1:
                    raise Exception ( 'Tag ' + str(token.nome) + ' deve ser declarada dentro da tag ' + str(hierarchy[0]) )

        def update_closing ( token ) :
            if token.nome in tags_map :
                if tags_map[token.nome] > 0 :
                    tags_map[token.nome] -= 1    
            else :
                raise Exception('Tag ' + str(token) + ' fechada e não aberta')

        def update_opening ( token ) :
            if token.nome in limited_tags_count :
                limited_tags_count[token.nome] += 1
            else :
                limited_tags_count[token.nome] = 1
            if token.nome in tags_map :
                tags_map[token.nome] += 1
            else :  
                tags_map[token.nome] = 1

        # update_opening(self.root.token)

        if len(tokens) > 1 :
            for i, token in enumerate(tokens) :
                verify_anatomy(token)
                if isinstance(token, TokenAbertura) :
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
                    current_node.addChild(token)

    def print_arvore (self) :
        self._print_arvore(self.root)

    def _print_arvore ( self, node ) :
        if len(node.children) > 0 :
            for child in node.children :
                self._print_arvore(child)
            print(str(node) + ' -> { ', end='')
            for child in node.children :
                print(str(child) + ' ', end='')
            print(' }')
        else :
            print(str(node) + ' -> { }')


