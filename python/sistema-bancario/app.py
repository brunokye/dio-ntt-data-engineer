from datetime import datetime

users = {}
accounts = []
current_user = None
account_number = 1


def show_menu():
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
    return input(menu)


def create_user():
    nome = input("\nInforme o nome do usuário: ")
    cpf = input("Informe o CPF do usuário (apenas números): ")

    if cpf in users:
        print("Operação falhou! Já existe um usuário cadastrado com esse CPF.")
        return

    endereco = input(
        "Informe o endereço (logradouro, número - "
        "bairro - cidade/sigla estado): "
    )

    users[cpf] = {
        "nome": nome,
        "endereco": endereco,
    }

    print(f"Usuário {nome} criado com sucesso!")


def login_user():
    global current_user
    cpf = input("\nInforme o CPF do usuário para login: ")
    if cpf in users:
        current_user = cpf
        print(f"Usuário {users[cpf]['nome']} logado com sucesso!")
    else:
        print("Operação falhou! Usuário não encontrado.")


def create_checking_account():
    global current_user, account_number

    if current_user is None:
        print(
            "\nNenhum usuário logado. Por favor, crie ou selecione um usuário."
        )
        return

    if (
        current_user in users
        and "contas" in users[current_user]
        and len(users[current_user]["contas"]) >= 3
    ):
        print("\nUsuário já possui o número máximo de contas!")
        return

    account = {
        "agency": "0001",
        "number": account_number,
        "user": current_user,
        "balance": 0,
        "extract": "",
        "number_of_transactions": 0,
        "number_of_withdrawals": 0,
        "LIMIT_OF_TRANSACTIONS": 10,
        "LIMIT_OF_WITHDRAWALS": 3,
        "limit": 500,
    }

    if current_user in users:
        if "contas" not in users[current_user]:
            users[current_user]["contas"] = []
        users[current_user]["contas"].append(account)

    accounts.append(account)
    print(
        "\nConta corrente criada com sucesso! "
        f"Número da conta: {account_number}"
    )
    account_number += 1


def deposit(account):
    value = float(input("Informe o valor do depósito: "))

    if value > 0:
        account["balance"] += value
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        account["extract"] += f"Depósito: R$ {value:.2f} - {timestamp} \n"
        account["number_of_transactions"] += 1
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


def withdraw(account):
    value = float(input("Informe o valor do saque: "))

    if value > account["balance"]:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif value < 0:
        print("Operação falhou! O valor informado é inválido.")
    elif value > account["limit"]:
        print("Operação falhou! O valor do saque excede o limite diário.")
    elif account["number_of_withdrawals"] >= account["LIMIT_OF_WITHDRAWALS"]:
        print("Operação falhou! Número máximo de saques diários atingido.")
    else:
        account["balance"] -= value
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        account["extract"] += f"Saque: R$ {value:.2f} - {timestamp} \n"
        account["number_of_transactions"] += 1
        account["number_of_withdrawals"] += 1
        print("Saque realizado com sucesso!")


def show_extract(account):
    print("\n================ EXTRATO ================")
    print(
        "Não foram realizadas movimentações."
        if not account["extract"]
        else account["extract"]
    )
    print(f"\nSaldo: R$ {account['balance']:.2f}")
    print("==========================================")


def select_account():
    global current_user
    if current_user is None:
        print("\nNenhum usuário logado.")
        return None

    user_accounts = users[current_user].get("contas", [])
    if not user_accounts:
        print("Nenhuma conta encontrada para o usuário.")
        return None

    print("\nSelecione a conta:")
    for i, acc in enumerate(user_accounts):
        print(f"[{i + 1}] Agência: {acc['agency']}, Conta: {acc['number']}")

    selected_index = int(input("Digite o número da conta desejada: ")) - 1
    if 0 <= selected_index < len(user_accounts):
        return user_accounts[selected_index]
    else:
        print("Opção inválida.")
        return None


def run_atm():
    global current_user
    while True:
        option = show_menu()

        if option == "1":
            create_user()

        elif option == "2":
            login_user()

        elif option == "3":
            create_checking_account()

        elif option == "4":
            account = select_account()
            if account is not None:
                deposit(account)

        elif option == "5":
            account = select_account()
            if account is not None:
                withdraw(account)

        elif option == "6":
            account = select_account()
            if account is not None:
                show_extract(account)

        elif option == "0":
            break

        else:
            print(
                "Operação inválida, por favor selecione "
                "novamente a operação desejada."
            )


run_atm()
