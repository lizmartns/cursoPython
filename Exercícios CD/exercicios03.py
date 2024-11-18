"""Crie um programa que leia o peso de uma carga em números inteiros. Se o peso for até 10kg, informe que o valor será de R$50,00. entre 11 e 20kg, informe que o valor será de R$ 80. Se for maior que 20 informe que o transporte não é aceito. teste vários pesos"""

peso = int(input("Insira o valor da carga: "))

if peso <=10 and peso >0:
    print("Valor R$50,00")
elif peso >=11 and peso <=20 :
    print("Valor R$80,00")
else :
    print("Transporte não é aceito")
