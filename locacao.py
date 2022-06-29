from operacao import Operacao
class Locacao:
    def __init__(self,periodo):
        self._periodo=int()
    def setPeriodo(self,periodo:int):
        self._periodo=periodo
    def getPeriodo(self,periodo:int):
         return self._periodo

