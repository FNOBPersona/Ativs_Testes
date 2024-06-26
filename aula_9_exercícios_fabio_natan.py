# -*- coding: utf-8 -*-
"""Aula 9 Exercícios-Fabio_natan

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pIoF78N6_Z_yYP9t0khIhWkur3gTUvHh
"""

#Exercício 1
print('Exercício 1.')
Chaves = [                               #Aqui eu crio a variável "Chaves" que será o verso a ser repetido
    "Volta o cão arrependido",
    "Com suas orelhas tão fartas",
    "Com seu osso roído",
    "E com o rabo entre as patas",
]
n = 0                                    #A variável "n" serve apenas como um contador para a repetição

while n < 44:
  print(Chaves)
  n += 1                                 #Aqui o código irá repetir a variável "Chaves" que contem o verso até o contador chegar no número 44, encerrando assim o loop


#Exercício 2
print('Exercício 2.')
for i in range(-1,9):
    print(f'Tabuada do {i+1}')             #Aqui o loop "for" será responsável em fazer a tabuada em si, da tabuada do zero até chegar a tabuada do 9
    for j in range(10):
      print(f'{i+1} x {j+1} = {(i+1) * (j+1) }')  #Este "for" será para executar as linhas da tabuada, da variável "i" irá multiplicar do 1 até o 10


#Exercício 3
print('Exercício 3.')
lista = []
for i in range(10):                                        #Crio um Loop para o algoritmo mandar ao usuário escrever 10 números inteiros
  num = int(input("Caro usuário, digite um numero: "))
  lista.append(num)
print('O maior numero digitado foi: {} '.format(max(lista)))
print('O menor numero digitado foi: {} '.format(min(lista)))   #Após a conclusão do loop, essas duas linhas de código irão pegar o que o usuário registrou e irão mostrar apenas o número de maior e menor valor dos 10 que o usuário registrou


#Exercício 4
print('Exercício 4.')
lista = [2, 12, 20, 0, 1, 3, 40, 7, 5, 10]
lista.sort()              #Aqui utilizo a função sort para organizar os números da lista
print(lista)