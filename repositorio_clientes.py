from clientes import Cliente
class RepositorioCliente:
    def __init__(self):
        self._clientes=[]
    def cadastrar(self,cliente:Cliente):
        cliente=self.buscar(cliente.getCpf())
        if cliente:
            print('cpf ja cadastrado')
        else:
            self._clientes.append(cliente)
    def buscar(self,cpf:str):
        for cliente in self._Clientes:
            if cliente.getCpf()==cpf:
                return cliente
            else:
                return None

    def atualizar(self,cliente:Cliente):
        cliente=self.buscar(cliente.getCpf())
        if cliente is not None:
            cliente.setNome(cliente.getNome())
            cliente.setEndereco(cliente.getEndereco)


    def deletar(self,cpf:str):
        if Cliente in self._clientes:
            self._clientes.pop(self._clientes.index(Cliente))

        else:
            print('cliente nao encontrado')

    def listar(self,cliente):
        return self._Clientes


