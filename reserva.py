from operacao import Operacao


class Reserva(Operacao):
    def __init__(self,cpf,codigo,prioridade):
        super().__init__(cpf,codigo)
        self._prioridade = int()

    def setPrioridade(self, prioridade):
        self._prioridade = int()

    def getPrioridades(self, prioridades):
        return self._prioridade
