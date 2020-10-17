#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "Você precisa de passar algum argumento"
else
    case "$1" in
    --test) 
        python3 -m unittest -v test.teste_all
        ;;
    --*) 
        printf -- '-%.0s' $(seq 100); echo ""
        echo "Atributo não reconhecido: $1"
        printf -- '-%.0s' $(seq 100); echo ""
        ;;
    *) 
        python3 main.py $@
        ;;
    esac
fi
exit 0
