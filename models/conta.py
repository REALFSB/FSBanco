from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:

    codigo: int = 1000  # Codigo da conta

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0  # Todo cliente que criar uma conta no banco vai ter R$100,00 de limite
        self.__saldo_total: float = self.calcula_saldo_total  # Saldo + limite
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero}\n' \
               f'Cliente: {self.cliente.nome}\n' \
               f'Saldo total: {formata_float_str_moeda(self.saldo_total)}\n'

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self.calcula_saldo_total
            print('Depósito efetuar com sucesso!')
        else:
            print('Erro ao efetuar o depósito. Tente novamente.')

    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
            print('Saque efetuado com sucesso!')
        else:
            print('Erro ao efetuar o saque. Tente novamente.')

    def transferir(self: object, destino: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self.calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.calcula_saldo_total
            print('Transferência realizada com sucesso!')

        else:
            print('Transferência não realizada. Tente Novamente!')
