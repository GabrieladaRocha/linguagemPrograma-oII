"""Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo)"""

class Validator():
    def is_positive(self, number):
        if number >= 0:
            print('Este número é positivo')
        else:
            print("Este número é Negativo")

validatorNumber = Validator()
number = int(input("Digite o Número que você deseja valdiar: "))
validatorNumber.is_positive(number)
