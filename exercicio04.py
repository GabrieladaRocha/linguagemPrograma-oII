"""Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço do produto e retorne o troco a ser dado."""

class Troco():
    def valor_troco(self, preco, desconto):
        calcula = preco - (preco * (desconto/100))
        print("O valor do produto ficou: ", calcula)

calculaTroco = Troco()

preco = int(input('Digite o preço do produto: '))
desconto = int(input("Digite o desconto em %: "))

calculaTroco.valor_troco(preco, desconto)
