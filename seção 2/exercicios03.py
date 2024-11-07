# Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
num : int = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'O numero {num} e par.')
else: 
    print(f'O numero {num} e impar.')