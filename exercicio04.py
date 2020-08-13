"""Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço do produto e retorne o troco a ser dado."""

class Troco():
    def valor_troco(self, valor, preco):
        calcula = valor - preco
        print("O valor do troco é: ", calcula)

calculaTroco = Troco()

valor = int(input("Digite o a quantia que você deu ao operador caixa. "))
preco = int(input('Digite o preço do produto. '))

calculaTroco.valor_troco(valor, preco)
