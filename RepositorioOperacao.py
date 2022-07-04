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
        Reserva = list()
        for reserva in self._operacoes:
            if isinstance(reserva, Reserva):
                if Operacao.getCpf() == cpf:
                    if Operacao.isativo() is True:
                        if isinstance(reserva,Operacao):
                            reserva.append(Operacao)
        return reserva

    def buscarLocacoes(self, cpf: str):
        Locacao = list()
        for Locacao in self._operacoes:
            if isinstance(locacao, Locacao):
                if Operacao.getCpf() == cpf:
                    if Operacao.isativo() is True:
                        if isinstance(Operacao, Locacao):
                            Locacao.append(Operacao)
        return Locacao

    def deletarReserva(self, cpf: str, codigo: int):
        for reserva in self._operacoes:
            if isinstance(reserva, Reserva):
                if reserva.getCpf() == cpf:
                    if reserva.getCodigo() == codigo:
                        reserva.setAtivo(False)

    def deletarLocacao(self, cpf: str, codigo: int):
        for locacao in self._operacoes:
            if isinstance(locacao,Locacao):


    def listarLocacao(self, cpf: str):
        pass

    def numeroLocacao(self, cpf: str):
        pass

    def numeroLocacao(self, codigo: int):
        pass

    def numerolocacaoAivas(self, cpf: str):
        pass

    def numeroLocacaoAtivas(self, codigo: int):
        pass

    def numeroReserva(self, codigo: int):
        pass
