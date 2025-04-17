from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario,self).__init__(nome, telefone, cpf, email, endereco)
