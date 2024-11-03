"""
Tipo string
em python um dado é considerado do tipo string sempre que estiver dentro de aspas simples, aspas duplas, aspas triplas e duplas triplas
"""
nome = 'Geek University'
print(nome.upper())
print(nome.lower())
print(nome.split()) #transforma em uma lista de string
print(nome[0:15]) # slice de string
print(nome[5:15])
print(nome.split()[0])
print(nome.split()[1])
print(nome[::-1]) # comece do primeiro elemento, vá até o último elemento e invert
print(nome.replace('G', 'P'))
print(nome.replace('e', 'i'))

texto = 'socorram me subino onibus em marrocos' #palíndromo
print(texto)

print(texto[::-1])
