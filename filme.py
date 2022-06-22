from datetime import date


class Filme:
    def __init__(self,codigo,titulo):
        self._codigo=int()
        self._titulo=str()
        self._genero=list()
        self._dataLancamento=date
        self._director=str()
        self._atores=list()
        self._sinopse=str()
        self._produtores=list()
        self._precoLocacao=float()
        self._numeroCopias=int()
    def setCodigo(self,codigo):
        self._codigo=codigo
    def getCodigo(self,codigo):
        return self._codigo
    def setTitulo(self,titulo):
        self._titulo=titulo
    def getTitulo(self,titulo):
        return self._titulo
    def setGenero(self,genero):
        self._genero=list()
    def getGenero(self,genero):
        return self._genero
    def addGenero(self,genero):
        self._genero=str()
    def setDataLancamento(self,date):
        self._dataLancamento=date
    def getDataLancamento(self,date):
        return self._dataLancamento
    def setDirector(self,director):
        self._director=director
    def getDirector(self,director):
        return self._director
    def setAtores(self,atores):
        self._atores=list()
    def getAtores(self,atores):
        return self._atores
    def addAtor(self,ator):
        self._ator=str()
    def setSinopse(self,sinopse):
        self._sinopse=sinopse
    def getSinopse(self,sinopse):
        return self._sinopse
    def setProdutores(self,produtores):
        self._produtores=list()
    def getProdutores(self,produtores):
        return self._produtores
    def addProdutor(self,produtor):
        self._produtor=str()
    def setPrecolocacao(self,precolocacao):
        self._precoLocacao=float()
    def getPrecolocacao(self,precolocacao):
        return self._precoLocacao
    def setNumeroCopias(self,numerocopias):
        self._numeroCopias=int()
    def getNumeroCopias(self,numerocopias):
        return self._numeroCopias



