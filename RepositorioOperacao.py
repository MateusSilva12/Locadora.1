from locacao import Locacao
from operacao import Operacao
from reserva import Reserva
class RepositorioOperacao:
    def __init__(self):
        self.operacao=[]
    def cadastrar(self,operacao:Operacao):
        pass
    def buscarReserva(self,cpf:str):
        pass
    def buscarLocacoes(self,cpf:str):
        pass
    def deletarReserva(self,cpf:str,codigo:int):
        pass
    def deletarLocacao(self,cpf:str,codigo:int):
        pass
    def listarLocacao(self,cpf:str):
        pass
    def numeroLocacao(self,cpf:str):
        pass
    def numeroLocacao(self,codigo:int):
        pass
    def numerolocacaoAivas(self,cpf:str):
        pass
    def numeroLocacaoAtivas(self,codigo:int):
        pass
    def numeroReserva(self,codigo:int):
        pass

