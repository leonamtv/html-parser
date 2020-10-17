import tracemalloc

tracemalloc.start()

import contextlib
from io import StringIO
import unittest

from core.tokenizer import Tokenizer
from core.arvore import Arvore

class testAll ( unittest.TestCase ) :
    """
    Classe com os casos de teste realizado.
    """

    def teste_a ( self ) :
        nome = './samples/teste1.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """Erro: O token < ABRE TAG: html > não pode ser aberto mais de uma vez."""
        
        self.assertEqual( output, expected_output )
  
    def teste_b ( self ) :
        nome = './samples/teste2.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """Erro: Tag li deve ser declarada dentro de uma dessas tags: ['ul', 'ol']"""
        
        self.assertEqual( output, expected_output )
  
    def teste_c ( self ) :
        nome = './samples/teste3.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """[ < ABRE TAG: link > ] -> { }
[ < ABRE TAG: head > ] -> { [ < ABRE TAG: link > ]  }
[ < DADO: Teste > ] -> { }
[ < ABRE TAG: p > ] -> { [ < DADO: Teste > ]  }
[ < DADO: asdasd > ] -> { }
[ < ABRE TAG: h1 > ] -> { [ < DADO: asdasd > ]  }
[ < ABRE TAG: body > ] -> { [ < ABRE TAG: p > ] [ < ABRE TAG: h1 > ]  }
[ < ABRE TAG: html > ] -> { [ < ABRE TAG: head > ] [ < ABRE TAG: body > ]  }
[ documento ] -> { [ < ABRE TAG: html > ]  }"""
        
        self.assertEqual( output, expected_output )
  
    def teste_d ( self ) :
        nome = './samples/teste4.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """[ < ABRE TAG: link > ] -> { }
[ < ABRE TAG: head > ] -> { [ < ABRE TAG: link > ]  }
[ < DADO: Teste > ] -> { }
[ < ABRE TAG: p > ] -> { [ < DADO: Teste > ]  }
[ < DADO: asdasd > ] -> { }
[ < ABRE TAG: h1 > ] -> { [ < DADO: asdasd > ]  }
[ < ABRE TAG: body > ] -> { [ < ABRE TAG: p > ] [ < ABRE TAG: h1 > ]  }
[ < ABRE TAG: html > ] -> { [ < ABRE TAG: head > ] [ < ABRE TAG: body > ]  }
[ documento ] -> { [ < ABRE TAG: html > ]  }"""
        
        self.assertEqual( output, expected_output )
  
    def teste_e ( self ) :
        nome = './samples/teste5.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """Erro: < ABRE TAG: p >: tag aberta e não fechada"""
        
        self.assertEqual( output, expected_output )
  
    def teste_f ( self ) :
        nome = './samples/teste6.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """Erro: Tag < FECHA TAG: p > fechada e não aberta"""
        
        self.assertEqual( output, expected_output )
  
    def teste_g ( self ) :
        nome = './samples/teste7.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """[ < DECL TAG: doctype html > ] -> { }
[ < ABRE TAG: meta | charset = utf-8 > ] -> { }
[ < ABRE TAG: link | href = https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap | rel = stylesheet > ] -> { }
[ < ABRE TAG: link | href = https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,600;0,700;0,800;1,300;1,400;1,600;1,700;1,800&display=swap | rel = stylesheet > ] -> { }
[ < DADO: Leonamtv > ] -> { }
[ < ABRE TAG: title > ] -> { [ < DADO: Leonamtv > ]  }
[ < ABRE TAG: base | href = https://leonamtv.github.io/leonamtv/ > ] -> { }
[ < ABRE TAG: meta | name = viewport | content = width=device-width, initial-scale=1 > ] -> { }
[ < ABRE TAG: link | rel = icon | type = image/x-icon | href = assets/favicon/favicon.ico > ] -> { }
[ < ABRE TAG: link | rel = apple-touch-icon | sizes = 180x180 | href = assets/favicon/apple-touch-icon.png > ] -> { }
[ < ABRE TAG: link | rel = icon | type = image/png | sizes = 32x32 | href = assets/favicon/favicon-32x32.png > ] -> { }
[ < ABRE TAG: link | rel = icon | type = image/png | sizes = 16x16 | href = assets/favicon/favicon-16x16.png > ] -> { }
[ < ABRE TAG: link | rel = stylesheet | href = styles.1a2dd1f7fc237001a3e3.css > ] -> { }
[ < ABRE TAG: head > ] -> { [ < ABRE TAG: meta | charset = utf-8 > ] [ < ABRE TAG: link | href = https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap | rel = stylesheet > ] [ < ABRE TAG: link | href = https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,600;0,700;0,800;1,300;1,400;1,600;1,700;1,800&display=swap | rel = stylesheet > ] [ < ABRE TAG: title > ] [ < ABRE TAG: base | href = https://leonamtv.github.io/leonamtv/ > ] [ < ABRE TAG: meta | name = viewport | content = width=device-width, initial-scale=1 > ] [ < ABRE TAG: link | rel = icon | type = image/x-icon | href = assets/favicon/favicon.ico > ] [ < ABRE TAG: link | rel = apple-touch-icon | sizes = 180x180 | href = assets/favicon/apple-touch-icon.png > ] [ < ABRE TAG: link | rel = icon | type = image/png | sizes = 32x32 | href = assets/favicon/favicon-32x32.png > ] [ < ABRE TAG: link | rel = icon | type = image/png | sizes = 16x16 | href = assets/favicon/favicon-16x16.png > ] [ < ABRE TAG: link | rel = stylesheet | href = styles.1a2dd1f7fc237001a3e3.css > ]  }
[ < DADO: Batata > ] -> { }
[ < ABRE TAG: p > ] -> { [ < DADO: Batata > ]  }
[ < ABRE TAG: img | src = asad > ] -> { }
[ < ABRE TAG: script | src = runtime-es2015.f8b979f66300b1e53384.js | type = module > ] -> { }
[ < ABRE TAG: script | src = runtime-es5.f8b979f66300b1e53384.js | nomodule | defer > ] -> { }
[ < ABRE TAG: script | src = polyfills-es5.854eca2125f3bf6856f8.js | nomodule | defer > ] -> { }
[ < ABRE TAG: script | src = polyfills-es2015.a2c1af2b1be41024173b.js | type = module > ] -> { }
[ < ABRE TAG: script | src = main-es2015.04368310fc69b15b5f08.js | type = module > ] -> { }
[ < ABRE TAG: script | src = main-es5.04368310fc69b15b5f08.js | nomodule | defer > ] -> { }
[ < ABRE TAG: body > ] -> { [ < ABRE TAG: p > ] [ < ABRE TAG: img | src = asad > ] [ < ABRE TAG: script | src = runtime-es2015.f8b979f66300b1e53384.js | type = module > ] [ < ABRE TAG: script | src = runtime-es5.f8b979f66300b1e53384.js | nomodule | defer > ] [ < ABRE TAG: script | src = polyfills-es5.854eca2125f3bf6856f8.js | nomodule | defer > ] [ < ABRE TAG: script | src = polyfills-es2015.a2c1af2b1be41024173b.js | type = module > ] [ < ABRE TAG: script | src = main-es2015.04368310fc69b15b5f08.js | type = module > ] [ < ABRE TAG: script | src = main-es5.04368310fc69b15b5f08.js | nomodule | defer > ]  }
[ < ABRE TAG: html | lang = en > ] -> { [ < ABRE TAG: head > ] [ < ABRE TAG: body > ]  }
[ documento ] -> { [ < DECL TAG: doctype html > ] [ < ABRE TAG: html | lang = en > ]  }"""
        
        self.assertEqual( output, expected_output )
  
    def teste_h ( self ) :
        nome = './samples/teste8.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """Erro: Tag img deve ser declarada dentro da tag html"""
        
        self.assertEqual( output, expected_output )
  
    def teste_i ( self ) :
        nome = './samples/teste9.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """[ < DECL TAG: DOCTYPE html > ] -> { }
[ < DADO: Titulo de nivel 1 > ] -> { }
[ < ABRE TAG: h1 > ] -> { [ < DADO: Titulo de nivel 1 > ]  }
[ < DADO: Titulo de nivel 2 > ] -> { }
[ < ABRE TAG: h2 > ] -> { [ < DADO: Titulo de nivel 2 > ]  }
[ < DADO: Titulo de nivel 3 > ] -> { }
[ < ABRE TAG: h3 > ] -> { [ < DADO: Titulo de nivel 3 > ]  }
[ < DADO: Titulo de nivel 4 > ] -> { }
[ < ABRE TAG: h4 > ] -> { [ < DADO: Titulo de nivel 4 > ]  }
[ < DADO: Titulo de nivel 5 > ] -> { }
[ < ABRE TAG: h5 > ] -> { [ < DADO: Titulo de nivel 5 > ]  }
[ < DADO: Titulo de nivel 6 > ] -> { }
[ < ABRE TAG: h6 > ] -> { [ < DADO: Titulo de nivel 6 > ]  }
[ < ABRE TAG: img | src = img_chania.jpg | alt = Flowers in Chania > ] -> { }
[ < ABRE TAG: html > ] -> { [ < ABRE TAG: h1 > ] [ < ABRE TAG: h2 > ] [ < ABRE TAG: h3 > ] [ < ABRE TAG: h4 > ] [ < ABRE TAG: h5 > ] [ < ABRE TAG: h6 > ] [ < ABRE TAG: img | src = img_chania.jpg | alt = Flowers in Chania > ]  }
[ documento ] -> { [ < DECL TAG: DOCTYPE html > ] [ < ABRE TAG: html > ]  }"""
        
        self.assertEqual( output, expected_output )
    
    def teste_j ( self ) :
        nome = './samples/teste10.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """Erro: O token < ABRE TAG: body > não pode ser aberto mais de uma vez."""
        
        self.assertEqual( output, expected_output )
    
    def teste_k ( self ) :
        print('Testando um arquivo vazio')
        tokenizer = Tokenizer()
        tokenizer.feed('')
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """Lista de tokens vazia."""
        
        self.assertEqual( output, expected_output )
    
    def teste_k ( self ) :
        nome = './samples/teste11.html'
        print('Testando o arquivo ' + nome)
        file = open(nome, 'r')
        html_content = file.read()
        file.close()

        tokenizer = Tokenizer()
        tokenizer.feed(html_content)
        tokens = tokenizer.get_fila()

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            _ = Arvore(tokens=list(tokens), verbose=True)

        output = temp_stdout.getvalue().strip()
        
        expected_output = """[ < DECL TAG: DOCTYPE html > ] -> { }
[ < ABRE TAG: meta | charset = UTF-8 > ] -> { }
[ < ABRE TAG: meta | name = viewport | content = width=device-width, initial-scale=1.0 > ] -> { }
[ < DADO: Document > ] -> { }
[ < ABRE TAG: title > ] -> { [ < DADO: Document > ]  }
[ < ABRE TAG: head > ] -> { [ < ABRE TAG: meta | charset = UTF-8 > ] [ < ABRE TAG: meta | name = viewport | content = width=device-width, initial-scale=1.0 > ] [ < ABRE TAG: title > ]  }
[ < DADO: Teste > ] -> { }
[ < ABRE TAG: h1 > ] -> { [ < DADO: Teste > ]  }
[ < DADO: Teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste
    teste teste teste teste teste teste teste teste teste teste > ] -> { }
[ < ABRE TAG: br > ] -> { }
[ < DADO: Teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste
    teste teste teste teste teste teste teste teste teste teste > ] -> { }
[ < ABRE TAG: body > ] -> { [ < ABRE TAG: h1 > ] [ < DADO: Teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste
    teste teste teste teste teste teste teste teste teste teste > ] [ < ABRE TAG: br > ] [ < DADO: Teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste teste
    teste teste teste teste teste teste teste teste teste teste > ]  }
[ < ABRE TAG: html | lang = en > ] -> { [ < ABRE TAG: head > ] [ < ABRE TAG: body > ]  }
[ documento ] -> { [ < DECL TAG: DOCTYPE html > ] [ < ABRE TAG: html | lang = en > ]  }"""
        
        self.assertEqual( output, expected_output )




        