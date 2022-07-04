from operacao import Operacao


class Reserva(Operacao):
    def __init__(self, prioridade):
        self._prioridade = int()

    def setPrioridade(self, prioridade):
        self._prioridade = int()

    def getPrioridades(self, prioridades):
        return self._prioridade
