"""Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, e mostre-o por extenso.
Este número deverá variar entre 1 e 5. Se o usuário introduzir um número que não pertença a este intervalo, mostre a frase “número inválido”."""

number = int(input('Digite um número de 1 a 5: '))

if number == 1:
    print('Número Um')
elif number == 2:
    print('Número Dois')
elif number == 3:
    print('Número Três')
elif number == 4:
    print('Número Quatro')
elif number == 5:
    print('Número Cinco')
else:
    print('Número inválido!!')
