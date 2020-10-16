import os
import argparse

from core.tokenizer import Tokenizer
from core.arvore import Arvore

parser = argparse.ArgumentParser(description="Analisador sintático para HTML. Leonam Teixeira de Vasconcelos.", add_help=False)

parser.add_argument('f', nargs='+', action='store', help='Lista de arquivos nos quais a análise sintática será realizada')
parser.add_argument('-h', '--help', action='help', help='Mostra essa mensagem e sai.')

args = parser.parse_args()

if args.f :
  for file in args.f :
    if not os.path.isfile ( file ) :
      print('Arquivo ' + str(file) + ' não encontrado.')
    html_content = open(file, 'r').read()
    
    tokenizer = Tokenizer()
    tokenizer.feed(html_content)
    tokens = tokenizer.get_fila()
    
    arvore = Arvore(tokens=list(tokens))
    
else :
  print('Você precisa de fornecer os arquivos para fazer a análisa sintática')
