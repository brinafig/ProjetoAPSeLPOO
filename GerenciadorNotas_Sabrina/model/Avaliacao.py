class Avaliacao:
    def __init__(self, nome, peso, data="", disciplina_id=None, id=None):
        self.id = id
        self.disciplina_id = disciplina_id
        self.nome = nome
        self.peso = peso
        self.data = data
