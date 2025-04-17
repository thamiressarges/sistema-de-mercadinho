from produto import Produto
from datetime import datetime

class Venda:
    def __init__(self, itensVendidos : Produto, vendedor, comprador, quantidadeVendida, data = datetime.now()):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data
