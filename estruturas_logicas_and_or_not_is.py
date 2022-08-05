"""
Estruturas logicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', amobos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True.
Para o 'is' o valor é comparado com um segundo.
"""
ativo = False
logado = False

# Se não estiver ativo
if ativo:
    print('Você precisa ativar a sua conta. Por favor cheque seu e-mail')
else:
    print('Bem-vindo usuário')

# ativo é True?
print(ativo is True)
