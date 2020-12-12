"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
from operator import itemgetter
def abre_arquivo(arquivo_de_txt):
    return   open(f'{arquivo_de_txt}', 'r').read()



def retorna_dicionario(arquivo_de_txt):
    lista_strings = abre_arquivo(arquivo_de_txt).lower().split()
    lista_strings.sort()
    dicionario = {}
    palavra_igual = lista_strings[0]
    ocorrencia = 0
    for palavra in lista_strings:
      if palavra == palavra_igual:
          ocorrencia += 1
      else:
          dicionario[palavra_igual] = ocorrencia
          ocorrencia = 1
          palavra_igual = palavra
    dicionario[palavra_igual] = ocorrencia
    return dicionario


def imprime_dicionario(dicionario):
    for k, v in dicionario.items():
        print(f'{k} {v}')
    return

def imprime_lista(lista):
  for contador, v in enumerate(lista):
    print(f'{v[0]} {v[1]}')
    if contador == 20:
        break






def print_words(filename):
    dicionario = retorna_dicionario(filename)
    imprime_dicionario(dicionario)
    return

def print_top(filename):
    dicionario = retorna_dicionario(filename)
    dicionario_organizado = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
    return imprime_lista(dicionario_organizado)





# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
