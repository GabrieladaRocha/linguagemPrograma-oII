""" 1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
Receba os dados pela console e chame este método."""
listStudent = []

class Estudante:
    def __init__(self,name,notas):
        self.name = name
        self.notas = notas

class AgeValidator:

    def students(self, nomeEstudante, notasAluno):
        self.notas = notasAluno
        self.name = nomeEstudante

    def calc(self):
        for x in range(5):
            students = listStudent[x]
            aux = 0
            total = 0
            for i in range(3):
                total = aux + students.notas[i]
                aux = total

            media = total / 3

            if media >= 7:
                print("aluno ", students.name, " está aprovado com media: ", media)
            else:
                print("aluno ", students.name, " não está aprovado, media: ", media)



    def input_students(self):
        instance = AgeValidator()
        for x in range(5):
            notas = []
            name = input("Nome do aluno: ")
            for i in range(3):
                nota = float(input("Digite a nota "))
                notas.append(nota)

            student = Estudante(name, notas)
            listStudent.append(student)

        instance.calc()


aplicacao = AgeValidator()
aplicacao.input_students()
