# estruturas lógicas : and, or, not, is
# operadores unários : not, is
# operadores binários : and, or

# and - ambos precisam ser True
# or - um ou outro precisam ser True
# not - o valor do booleano é invertido

ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta.')

if not ativo:
    print('Voce precisa ativar sua conta, cheque seu e-mail')
else:
    print('Bem-vindo usuário !')

print(not False)