# -*- coding: utf-8 -*-
"""Aula4_FabioNatan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DX_LMDvueDRGsbANpGQLGBaA9VRQgDq1
"""

nota1 = float(input("Informe a nota 1:"))
nota2 = float(input("Informe a nota 2:"))

media = (nota1 + nota2) / 2

print("Média final: ", media)
print(media >= 5.75)

#Questão 1)
x = float(input("Digite o número que representará a incógnita 'x': "))
y = float(input("Digite o número que representará a incógnita 'y': "))

soma = float(x + y)
subtracao = float(x - y)
divisao = float(x / y)
multiplicacao = float(x * y)
print("Resultado da soma : ", soma)
print("Resultado da subtração: ", subtracao)
print("Resultado da divisão: ", divisao)
print("Resultado da multiplicação: ", multiplicacao)

#Questão 2)
distancia_total = float(input("Digite a distância total da viagem: "))
combL_gasto = float(input("Digite o combustível gasto durante a viagem: "))

cons_med = float(distancia_total / combL_gasto)
print("Sua média de consumo de combustível é: ", cons_med)

#Questão 3)
vendedor = input("Digite o código/nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
vendas = float(input("Digite as vendas do mês: "))
comissao = 0.15

salario_do_mes = salario_fixo + (vendas * comissao)

tex_resultado = "O salário de {} será de R$ {} este mês.".format(vendedor, salario_do_mes)
print(tex_resultado)

#Questão 4)
a = input("Digite um valor para ""A"":")
b = input("Agora digite um valor para ""B"":")

print("O valor de A é: ", a)
print("E o valor de B é: ", b)

c = a
a = b
b = c

print("Agora o valor de ""A"" é: ", a)
print("e o valor de ""B"" é: ", b)

#Questão 5
real = float(input("Digite quantos reais você possui: "))
cotacao = float(input("Digite a cotação do dólar atual: "))

conversao = (real / cotacao)

money_disp = "Você possui U$${} dólares disponveis em sua conta.".format(conversao)
print(money_disp)

#Questão 6
deposito = float(input("Digite o valor depositado para a simulação de rendimento: "))
mes = 1
juros = 0.07

rendimento = mes * (deposito * juros)

print("O seu rendimento após 1 mês é de: ", rendimento)

#Questão 7
produto = float(input("Caro cliente, digite o valor do produto ($): "))
prestacao = (produto / 5)

print("Durante os 5 meses você deverá pagar R$",prestacao,"de prestação")