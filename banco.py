from time import sleep
from typing import List

from models.cliente import Cliente
from models.conta import Conta

print('\033[107;30;4mBanco feito por: Fernando de Souza Batista\033[40;97;0m')
print('\033[107;30;4mLinkedin: https://www.linkedin.com/in/fernando-batista-208048207/\033[40;97;0m')

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print(f"\033[97m{'=' * 40}")
    print(f"{'Caixa Eletrônico':-^40}")
    print(f"{'FSBANCO':-^40}")
    print(f"{'=' * 40}")

    print('Selecione uma opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome: ')
    email: str = input('E-mail: ')
    cpf: str = input('CPF: ')
    data_nasc: str = input('Data de nascimento: ')
    print()

    cliente: Cliente = Cliente(nome, cpf, email, data_nasc)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('\033[38;5;11mConta criada com sucesso!\033[97m\n')
    print('Dados da conta:')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:  # Verifica se há contas cadastradas.
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = listar_conta_por_id(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta de número: {numero}.')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = listar_conta_por_id(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta de número: {numero}.')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))

        conta_o: Conta = listar_conta_por_id(numero_o)
        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino: '))

            conta_d: Conta = listar_conta_por_id(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_o.transferir(conta_d, valor)
            else:
                print(f'Não foi encontrada a conta de número: {conta_d}.')
        else:
            print(f'Não foi encontrada a conta de número: {conta_o}.')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas:')

        for conta in contas:
            print(conta)
            print(f"{'-' * 10}")
            sleep(0.5)
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def listar_conta_por_id(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
