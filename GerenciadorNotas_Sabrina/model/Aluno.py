from .Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, matricula, email="", id=None):
        super().__init__(nome)
        self.id = id
        self.matricula = matricula
        self.email = email
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_dados(self):
        return f"Aluno: {self.nome}\nMatrícula: {self.matricula}\nE-mail: {self.email}"
