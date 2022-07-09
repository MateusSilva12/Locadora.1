import locacao
import reserva
from locacao import Locacao
from operacao import Operacao
from reserva import Reserva


class RepositorioOperacao:
    def __init__(self):
        self._operacoes = []

    def cadastrar(self, operacao: Operacao):
        if self.buscarReserva(Operacao):
            if Operacao.isativo(True):
                return Reserva
        if self.buscarLocacoes(Operacao):
            if Operacao.isativo(True):
                return Locacao

    def buscarReserva(self, cpf: str):
        reserva = list()
        for reserva in self._operacoes:
            if isinstance(reserva, Reserva):
                if Operacao.getCpf() == cpf:
                    if Operacao.isativo() is True:
                        if isinstance(reserva,Operacao):
                            reserva.append(Operacao)
        return reserva

    def buscarLocacoes(self, cpf: str):
        locacao = list()
        for locacao in self._operacoes:
            if isinstance(locacao, Locacao):
                if Operacao.getCpf() == cpf:
                    if Operacao.isativo() is True:
                        if isinstance(Operacao, Locacao):
                            locacao.append(Operacao)
        return locacao

    def deletarReserva(self, cpf: str, codigo: int):
        for reserva in self._operacoes:
            if isinstance(reserva, Reserva):
                if reserva.getCpf() == cpf:
                    if reserva.getCodigo() == codigo:
                        reserva.setAtivo(False)

    def deletarLocacao(self, cpf: str, codigo: int):
        for locacao in self._operacoes:
            if isinstance(locacao,Locacao):
                if locacao.getCpf()==cpf:
                    if locacao.getCodigo()==codigo:
                        locacao.set_Ativo(False)


    def listarLocacao(self, cpf: str):
        locacoes=list()
        for locacao in self._operacoes:
            if isinstance(locacao,Locacao):
                if locacao.getCpf()==cpf:
                    locacoes.append(locacao)
        return locacoes

    def numeroLocacoes(self, cpf: str):
        cont=0
        for operacao in self._operacoes:
            if operacao.getCpf()==cpf:
                cont +=1
        return cont

    def numeroLocacao(self, codigo: int):
        cont=0
        for operacao in self._operacoes:
            if operacao.getCodigo()==codigo:
                cont+=1
        return cont






    def numerolocacaoAivas(self, cpf: str):
        pass

    def numeroLocacaoAtivas(self, codigo: int):
        pass

    def numeroReserva(self, codigo: int):
        pass
