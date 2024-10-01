from abc import ABC, abstractmethod
from datetime import datetime


class Transaction(ABC):
    @abstractmethod
    def register(self, account):
        pass


class Deposit(Transaction):
    def __init__(self, value):
        self.value = value

    def register(self, account):
        if self.value > 0:
            account.balance += self.value
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            account.history.add_transaction(
                f"Depósito: R$ {self.value:.2f} - {timestamp}"
            )
            account.number_of_transactions += 1
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")


class Withdrawal(Transaction):
    def __init__(self, value):
        self.value = value

    def register(self, account):
        if self.value > account.balance:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif self.value > account.limit:
            print("Operação falhou! O valor do saque excede o limite diário.")
        elif account.number_of_withdrawals >= account.WITHDRAWAL_LIMIT:
            print("Operação falhou! Número máximo de saques diários atingido.")
        else:
            account.balance -= self.value
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            account.history.add_transaction(
                f"Saque: R$ {self.value:.2f} - {timestamp}"
            )
            account.number_of_transactions += 1
            account.number_of_withdrawals += 1
            print("Saque realizado com sucesso!")


class History:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


class Account(ABC):
    def __init__(self, number, client):
        self._balance = 0.0
        self.number = number
        self.agency = "0001"
        self.client = client
        self.history = History()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @abstractmethod
    def withdraw(self, value):
        pass

    @abstractmethod
    def deposit(self, value):
        pass


class CheckingAccount(Account):
    WITHDRAWAL_LIMIT = 3
    TRANSACTION_LIMIT = 10

    def __init__(self, number, client):
        super().__init__(number, client)
        self.limit = 500
        self.number_of_withdrawals = 0
        self.number_of_transactions = 0

    def withdraw(self, value):
        withdrawal = Withdrawal(value)
        self.client.perform_transaction(self, withdrawal)

    def deposit(self, value):
        deposit = Deposit(value)
        self.client.perform_transaction(self, deposit)


class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def perform_transaction(self, account, transaction):
        if len(account.history.transactions) < account.TRANSACTION_LIMIT:
            transaction.register(account)
        else:
            print("Limite de transações atingido!")

    def add_account(self, account):
        if len(self.accounts) < 3:
            self.accounts.append(account)
            print(f"\nConta corrente {account.number} criada com sucesso!")
        else:
            print("Usuário já possui o número máximo de contas!")


class PhysicalPerson(Client):
    def __init__(self, cpf, name, birth_date, address):
        super().__init__(address)
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date


clients = {}
current_client = None


def create_user():
    global clients
    name = input("\nInforme o nome do usuário: ")
    cpf = input("Informe o CPF do usuário (apenas números): ")

    if cpf in clients:
        print("Operação falhou! Já existe um usuário cadastrado com esse CPF.")
        return None

    address = input("Informe o endereço: ")
    birth_date = input("Informe a data de nascimento (dd/mm/yyyy): ")

    client = PhysicalPerson(cpf, name, birth_date, address)
    clients[cpf] = client
    print(f"Usuário {name} criado com sucesso!")
    return client


def login_user():
    global current_client, clients
    cpf = input("\nInforme o CPF do usuário para login: ")
    if cpf in clients:
        current_client = clients[cpf]
        print(
            f"Login realizado com sucesso! Bem-vindo(a), {current_client.name}"
        )
    else:
        print("Usuário não encontrado!")


def create_checking_account(client, number):
    if client:
        account = CheckingAccount(number, client)
        client.add_account(account)
        return account
    else:
        print("\nNenhum cliente disponível para criar conta.")
        return None


def select_account(client):
    if not client.accounts:
        print("\nNenhuma conta disponível para o cliente.")
        return None

    print("\nSelecione a conta:")
    for i, account in enumerate(client.accounts):
        print(f"[{i + 1}] Agência {account.agency}, Conta {account.number}")

    option = int(input("\nDigite o número da conta desejada: ")) - 1
    if 0 <= option < len(client.accounts):
        return client.accounts[option]
    else:
        print("Opção inválida.")
        return None


def main():
    global current_client
    account_number = 1
    menu = """
    Use apenas números durante toda interação com o sistema.
    [1] Criar Usuário
    [2] Login
    [3] Criar Conta Corrente
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [0] Sair

    """

    while True:
        option = input(menu)

        if option == "1":
            create_user()

        elif option == "2":
            login_user()

        elif option == "3":
            if current_client:
                create_checking_account(current_client, account_number)
                account_number += 1
            else:
                print("\nNenhum usuário logado!")

        elif option == "4":
            if current_client:
                account = select_account(current_client)
                if account:
                    value = float(input("\nInforme o valor do depósito: "))
                    account.deposit(value)
            else:
                print("\nNenhum usuário logado!")

        elif option == "5":
            if current_client:
                account = select_account(current_client)
                if account:
                    value = float(input("\nInforme o valor do saque: "))
                    account.withdraw(value)
            else:
                print("\nNenhum usuário logado!")

        elif option == "6":
            if current_client:
                account = select_account(current_client)
                if account:
                    print("\nExtrato")
                    for transaction in account.history.transactions:
                        print(transaction)
                    print(f"Saldo: R$ {account.balance:.2f}")
            else:
                print("\nNenhum usuário logado!")

        elif option == "0":
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()
