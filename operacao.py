from datetime import date


class Operacao:
    def __init__(self,cpf,codigo):
        self._data=date
        self._cpf=str()
        self.codigo=int()
        self.ativo=bool()
    def setData(self,data):
        self._data=date
    def getData(self,data):
        return self._data
    def setCpf(self,cpf):
        self._cpf=str()
    def getCpf(self,cpf):
        return self._cpf
    def setCodigo(self,codigo):
        self._codigo=int()
    def getCodigo(self,codigo):
        return self._codigo
    def setAtivo(self,ativo):
        self._ativo=bool()
    def isativo(self):
        return self._ativo
