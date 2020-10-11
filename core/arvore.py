from core.node.node import Node
from core.token.token import Token
from core.token.token_comentario import TokenComentario
from core.token.token_abertura import TokenAbertura
from core.token.token_fechamento import TokenFechamento
from core.token.token_dado import TokenDado

class Arvore : 

    def __init__ ( self, tokens=[] ) :
        if len ( tokens ) > 0 :
            self.root = Node(tokens[0], children=[], parent=None)
            self.build_from_tokens(tokens)
            self.print_arvore()
            
    def build_from_tokens ( self, tokens ) :
        current_node = self.root
        print(self.root)
        if len(tokens) > 1 :
            for token in tokens[1:] :
                if isinstance(token, TokenAbertura) :
                    new_node = Node(token, [], current_node)
                    current_node.addChild(new_node)
                    current_node = new_node
                elif isinstance(token, TokenFechamento) :
                    if current_node.parent != None :
                        current_node = current_node.parent
                elif isinstance(token, TokenDado) :
                    if current_node.parent != None :
                        current_node.addChild(token)
                        current_node = current_node.parent

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
            print(node)           

