from .Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, titulo, id=None):
        super().__init__(nome)
        self.id = id
        self.titulo = titulo

    def exibir_dados(self):
        return f"{self.titulo} {self.nome}"
