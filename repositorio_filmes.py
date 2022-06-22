from filme import Filme
class RepositorioFilme:
    def __init__(self,filme:Filme):
        self._filme=[]
    def cadastrar(self,filme:Filme):
        pass
    def buscar(self,codigo:int):
        pass
    def atualizar(self,filme:Filme):
        pass
    def Getlistar(self,filme):
        return self._filme