# Recebendo código do usuário 

# entrada de dados
#print("Qual seu nome ?")
#nome = input () #input -> entrada
#Todo dado recebido via input é do tipo String
nome = input('Qual seu nome ?')

#Exemplo de print antigo
#print("Seja bem vindo(a) %s" % nome)

#exemplo de print moderno
#print ("Seja bem vindo(a) {0}".format(nome))

#exemplo de print mais atual
print(f'seja bem-vindo(a) {nome}')

#print("Qual sua idade ?")
#idade = input()
idade = int(input('Qual sua idade ?'))

# processamento

# saída de dados
#Exemplo de print antigo
#print("A %s tem %s anos" % (nome, idade))

#exemplo de print moderno
#print ("A {0} tem {1} anos" .format(nome, idade))
print(f'A {nome} tem {idade} anos.')

"""
 int (idade) => CAST
 Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2024 - idade}') 