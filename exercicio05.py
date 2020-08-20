"""Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo)"""

class Validator():
    def is_positive(self, number):
        if (number % 2) == 0:
            print('Este número é par')
        else:
            print("Este número é impar")

validatorNumber = Validator()
number = int(input("Digite o Número que você deseja valdiar: "))
validatorNumber.is_positive(number)
