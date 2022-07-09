from operacao import Operacao
class Locacao(Operacao):
    def __init__(self,periodo:int):
        super().__init__(self._cpf,self.codigo)
        self._periodo=int()
    def setPeriodo(self,periodo:int):
        self._periodo=periodo
    def getPeriodo(self,periodo:int):
         return self._periodo

