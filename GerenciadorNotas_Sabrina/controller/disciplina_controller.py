from dao.disciplina_dao import DisciplinaDAO
from model.Disciplina import Disciplina


class DisciplinaController:

    def __init__(self):
        self.dao = DisciplinaDAO()

    def salvar(self, nome, professor):

        disciplina = Disciplina(
            nome,
            professor
        )

        self.dao.inserir(disciplina)

    def listar(self):
        return self.dao.listar()

    def atualizar(self, disciplina):
        self.dao.atualizar(disciplina)

    def excluir(self, id_disciplina):
        self.dao.excluir(id_disciplina)