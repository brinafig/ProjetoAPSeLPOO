from dao.professor_dao import ProfessorDAO
from model.Professor import Professor


class ProfessorController:

    def __init__(self):
        self.dao = ProfessorDAO()

    def salvar(self, nome, titulo):

        professor = Professor(
            nome,
            titulo
        )

        self.dao.inserir(professor)

    def listar(self):
        return self.dao.listar()

    def atualizar(self, id_professor, nome, titulo):

        professor = Professor(
            nome,
            titulo,
            id_professor
        )

        self.dao.atualizar(professor)

    def excluir(self, id_professor):
        self.dao.excluir(id_professor)