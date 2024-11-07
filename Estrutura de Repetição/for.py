nomes = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

#Iterando uma string
for letra in nomes[0:5]: 
    print(letra)

# iterando uma lista 
for numero in lista:
    print(numero)

# iterando um range
for numero in range (1,11):
    print(numero)

for i, v in enumerate(nomes):
    print(nomes[i])

for _, letra in enumerate(nomes):
    print(letra)

'''for n in range (1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f' A soma é {soma}')'''

nome = 'Geek University'
for letra in nome :
    print(letra, end='')

#Original : U+1F60D
#Modificado : U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D'*num)