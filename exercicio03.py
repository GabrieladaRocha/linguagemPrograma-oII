"""Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
O usuário deve informar dois números e o programa deve fazer as quatro operações."""

class Calculadora():

    def soma(self, numero1, numero2):
        calculaSoma = numero1 + numero2
        print("O valor da soma é: ", calculaSoma + 1)

    def subtracao(self, numero1, numero2):
        calculaSubtracao = numero1 - numero2
        print('O valor da subtração é: ', calculaSubtracao+ 1)

    def multiplicacao(self, numero1, numero2):
        calculaMultiplicacao = numero1 * numero2
        print('O valor da multiplicação é: ', calculaMultiplicacao+ 1)

    def divisao(self, numero1, numero2):
        calculaDivisao = numero1 / numero2
        print('Ovalor da divisão é: ', calculaDivisao+ 1)

calcula = Calculadora()

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

calcula.soma(numero1, numero2)
calcula.subtracao(numero1, numero2)
calcula.multiplicacao(numero1, numero2)
calcula.divisao(numero1, numero2)
