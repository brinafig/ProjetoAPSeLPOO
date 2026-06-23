from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.__nome = nome

    # GETTER
    @property
    def nome(self):
        return self.__nome

    # SETTER
    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor.strip()

    @abstractmethod
    def exibir_dados(self):
        pass

    def __str__(self):
        return self.exibir_dados()

