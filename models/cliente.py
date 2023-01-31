from datetime import date

from utils.helper import date_para_str, str_para_date


class Cliente:

    contador: int = 1  # Id do cliente.

    def __init__(self: object, nome: str, cpf: str, email: str, data_nasc: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__email: str = email
        self.__data_nasc: date = str_para_date(data_nasc)
        self.__data_cadastro: date = date.today()  # Data que o cliente fez o cadastro.
        Cliente.contador += 1


    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self:object) -> str:
        return self.__cpf

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def data_nasc(self: object) -> str:
        return date_para_str(self.__data_nasc)

    @property
    def data_cadastro(self: object) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f'CÓDIGO: {self.codigo}\n' \
               f'NOME: {self.nome}\n' \
               f'DATA DE NASCIMENTO: {self.data_nasc}\n' \
               f'DATA DE CADASTRO: {self.data_cadastro}\n'

