"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia de PEP8 é que possamos escrever códigos Python de forma Pythonica.

[1] - Ultilize Camel Case para nomes de classes;

[2] - Ultilize nomes em minúsculo, separados por undeline para funções ou variáveis;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

[3] - Ultilize 4 espaços para identação!(NÃO USE TAB)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco

[5] - Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em ultilizar

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça

algo(1)

# Não faça

dict ['chave'] = lista [indice]

# Faça

dict['chave'] = lista[indice]

# Não faça

x              = 1
y              = 3
variavel_longa = 5

#Faça

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma intrução com uma nova linha
"""
import this
