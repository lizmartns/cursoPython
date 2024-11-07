""" Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido. """

from math import sqrt

num = int(input('Digite um numero: '))

if num < 0:
    print('Número inválido.')
else: 
    print(f'A raiz quadrada de {num} é: {sqrt(num)}')