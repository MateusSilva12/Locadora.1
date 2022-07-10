from locacao import Locacao
from operacao import Operacao
from reserva import Reserva


class RepositorioOperacao:
    def __init__(self):
        self._operacoes = []

    def cadastrar(self, operacao: Operacao):
        if self.buscarReserva(operacao):
            if Operacao.isativo(True):
                return Reserva
        if self.buscarLocacoes(operacao):
            if Operacao.isativo(True):
                return Locacao

    def buscarReserva(self, cpf: str):
        reservas = list()
        for reserva in self._operacoes:
            if isinstance(reserva, Reserva):
                if reserva.getCpf() == cpf:
                    if reserva.isativo() is True:
                            reservas.append(reserva)
        return reservas

    def buscarLocacoes(self, cpf: str):
        locacoes = list()
        for locacao in self._operacoes:
            if isinstance(locacao, Locacao):
                if locacao.getCpf() == cpf:
                    if locacao.setAtivo() is True:
                            locacoes.append(locacao)
        return locacoes

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
        cont=0
        for operacao in self._operacoes:
            if operacao.getCpf()==cpf:
                if operacao.setAtivo()==True:
                    cont+=1
        return cont
    def numeroLocacaoAtivas(self, codigo: int):
        cont=0
        for operacao in self._operacoes:
            if operacao.getCodigo()==codigo:
                if operacao.setAtivo()==True:
                    cont+=1
        return cont

    def numeroReserva(self, codigo: int):
        cont=0
        for reserva in self._operacoes:
            if reserva.getCodigo()==codigo:
                if reserva.setAtivo()==True:
                    cont+1
        return cont
