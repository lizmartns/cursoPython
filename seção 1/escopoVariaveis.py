# Escopo de variáveis = limitação de algo 
"""
1- variáveis globais:seu escopo cocmpreende todo o programa
2- variáveis locais: são reconhecidas apenas no bloco onde foram declaradas.

Para declarar variáveis em python fazemso :
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela. Este tipo é indeferido ao atribuírmos o valor à mesma.
"""
numero = 42 #exemplo de variável global
print(numero)
print(type(numero))

numero = 'geek'
print(numero)
print(type(numero))

numero = 32
novo = 0
if numero >10:
    novo = numero + 10 # a variável novo está declarada localmente dentro do bloco do if
    print(novo)

print(novo)
