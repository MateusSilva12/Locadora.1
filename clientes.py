class Cliente:
    def __init__(self,cpf):
        self._cpf=cpf
        self._nome=str()
        self._endereco=str()
    def setCpf(self,cpf):
        self._cpf= cpf
    def getCpf(self,cpf):
        return self._cpf
    def setNome(self,nome):
        self._nome=nome
    def getNome(self,nome):
        return self._nome
    def setEndereco(self,endereco):
        self._endereco=endereco
    def getEndereco(self,endereco):
        return self._endereco
    def imprimir(self):
        print("nome:{},endereco:{}".format(self._nome,self._endereco))
