# Definição da superclasse
class Integrante_IFRN:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibirMensagem(self):
        print(f"Integrante_IFRN: Seja bem-vindo(a) ao IFRNI!!")


# Definição da subclasse Professor
class Professor(Integrante_IFRN):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibirMensagem(self):
        print(f"Professor {self.nome}: Meus alunos são os melhores!!!")


# Definição da subclasse Aluno
class Aluno(Integrante_IFRN):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def exibirMensagem(self):
        print(f"Aluno {self.nome}: Vou estudar pra tirar 100 em P00")


# Testando as classes
integrante = Integrante_IFRN("eloiza", 17)
professor = Professor("João", 40, "Matemática")
aluno = Aluno("Maria", 20, "Engenharia")

# Chamando os métodos
integrante.exibirMensagem()
professor.exibirMensagem()
aluno.exibirMensagem()
