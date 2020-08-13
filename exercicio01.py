""" 1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
Receba os dados pela console e chame este método."""

class AgeValidator:

    def age_validator(self, idade):
        if idade >= 18:
            print('Esta pessoa é maior de idade.')
        else:
            print("Esta pessoa é menor de idade.")

maioridade = AgeValidator()
age = int(input('Digite a Idade: '))
maioridade.age_validator(age)
