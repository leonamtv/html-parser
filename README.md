# HTMLParser Leonam

Analisador léxico de HTML para a disciplina de compiladores da engenharia de computação CEFET-MG Timóteo.

## Instruções de execução

Dê permissão para executar o script:

```bash
chmod +x hp.sh
```

Execute os testes já programados (com os html's da pasta `./samples`):

```bash
./hp.sh --test
```

Execute com seu arquivo de preferência:

```bash
./hp.sh <arquivo>
```

Caso queira visualizar uma representação simples da árvore gerada (caso não haja nenhum erro no html), passe o argumento `-v` ou `--verbose`, assim:

```bash
./hp.sh <arquivo> -v
ou
./hp.sh <arquivo> --verbose
```