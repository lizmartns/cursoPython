#3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
valor1 : int = int(input(f'Informe o primeiro valor: '))
valor2 : int = int(input(f'Informe o segundo valor: '))
valor3 : int = int(input(f'Informe o terceiro valor: '))

quadrado : int = (valor1*valor1) + (valor2*valor2) + (valor3*valor3)

print(f'A soma do quadrado dos valores e: {quadrado}')