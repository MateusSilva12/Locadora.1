from repositorio_filmes import RepositorioFilme
from repositorio_clientes import RepositorioCliente
from RepositorioOperacao import RepositorioOperacao
from filme import Filme
from reserva import Reserva
from clientes import Cliente
class Locadora:
    def __init__(self,clientes:RepositorioCliente,filmes:RepositorioFilme,operacoes:RepositorioOperacao):
        self._filmes=filmes
        self._clientes=clientes
        self._operacao=operacoes
    def cadastrarCliente(self,cliente:Cliente):
        self._clientes.cadastrar(cliente)
    def buscarCliente(self,cpf:str):
        self._clientes.buscar(cpf)
    def atualizarCadastroCliente(self,cliente:Cliente):
        self._clientes.atualizar(cliente)
    def removerCliente(self,cpf:str):
        self._clientes.deletar(cpf)
    def cadastrarFilme(self,filme:Filme):
        self._filmes.cadastrar(filme)
    def buscarFilme(self,codigo:int):
        self._filmes.buscar(codigo)
    def atualizarCadastroFilme(self,filme:Filme):
        self._filmes.atualizar(filme)
    def removerFilme(self,codigo:int):
        self._filmes.deletar(codigo)
    def reservaFilme(self,cpf:str,codigo:int):
       reserva=Reserva(cpf,codigo)
       if self.buscarCliente(cpf) is not None and self.buscarFilme(codigo):
                  if self._operacao.numeroLocacoes()==Filme.getnumeroCopias():
                      self._operacao.cadastrar(reserva)

    def finalizarReservafilme(self,cpf:str,codigo:int):
        reserva=Reserva(cpf,codigo)
        if self.reservaFilme(cpf,codigo) is True:
            self._operacao.deletarReserva(reserva)

    def locarFilme(self):
        pass
    def devolverFilme(self):
        pass
    def imprimirHistoricoLocacoes(self):
        pass
    def imprimirFilmesLocados(self):
        pass

