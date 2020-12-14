from abc import ABCMeta, abstractmethod


class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, camera):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass
