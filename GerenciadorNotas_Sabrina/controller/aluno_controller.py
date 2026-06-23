from dao.aluno_dao import AlunoDAO
from model.Aluno import Aluno


class AlunoController:

    def __init__(self):
        self.dao = AlunoDAO()

    def salvar(self, nome, matricula):

        aluno = Aluno(
            nome,
            matricula
        )

        self.dao.inserir(aluno)

    def listar(self):
        return self.dao.listar()

    def atualizar(self, id_aluno, nome, matricula):

        aluno = Aluno(
            nome,
            matricula,
            id_aluno
        )

        self.dao.atualizar(aluno)

    def excluir(self, id_aluno):
        self.dao.excluir(id_aluno)