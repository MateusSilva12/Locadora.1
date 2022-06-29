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
            if filme.getCodigo() == codigo:
                return filme
        return None

    def atualizar(self, filme: Filme):
        pass
        # self._buscar(filme.getCodigo())
        # if

    def Getlistar(self, filme):
        return self._filme
