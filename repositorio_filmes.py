from filme import Filme


class RepositorioFilme:
    def __init__(self):
    self._filmes = []

    def cadastrar(self, filme: Filme):
        filme = self.buscar(Filme.getCodigo())
        if filme:
            print("filme ja possui cadastro")
        else:
            self._filme_append(Filme)

    def buscar(self, codigo: int):
        for filme in self._filmes:
            if filme.getCodigo()==codigo:
                return filme
            else:
                return None
    def atualizar(self,filme:Filme):
        filme=self._buscar(filme.getCodigo())
        if filme is not None:
            filme.setTitulo(filme.getTitulo())
            filme.setGenero(filme.getGenero())
            filme.setDataLancamento(filme.getDataLancamento())
            filme.setDirector(filme.getDirector())
            filme.setSinopse(filme.getSinopse())
            filme.setProdutores(filme.getProdutores())
            filme.setprecolocacao(filme.getPrecolocacao())
            filme.setnumeroCopias(filme.getnumeroCopias())
        else:
            print("filme nao foi encontrado")
    def deletar(self,codigo:int):
        for filme self._filmes:
            if filme.getCodigo()==codigo
                self._filmes.pop(self._filmes.index(filme))

     def Getlistar(self, filme):
        return self._filme
