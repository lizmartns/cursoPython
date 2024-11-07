#Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

num1 =  input('Escreva o primeiro numero: ')
num2 =  input('Escreva o segundo numero: ')

if num1 > num2:
    print(f'{num1} e maior que {num2}.')
elif num1 ==  num2 :
    print(f'Os numeros {num1} e {num2} sao iguais.')
else:
    print(f'{num2} e maior que {num1}.')