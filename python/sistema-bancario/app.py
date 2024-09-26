from datetime import datetime


def mostrar_menu():
    menu = """
    Use apenas números durante toda interação com o sistema.
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    """
    return input(menu)


def deposit(balance, extract, number_of_transactions):
    value = float(input("Informe o valor do depósito: "))

    if value > 0:
        balance += value
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extract += f"Depósito: R$ {value:.2f} - {timestamp} \n"
        number_of_transactions += 1
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return balance, extract, number_of_transactions


def withdraw(
    balance,
    extract,
    number_of_transactions,
    number_of_withdrawals,
    limit,
    LIMIT_OF_WITHDRAWALS,
):
    value = float(input("Informe o valor do saque: "))

    if value > balance:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif value < 0:
        print("Operação falhou! O valor informado é inválido.")
    elif value > limit:
        print("Operação falhou! O valor do saque excede o limite diário.")
    elif number_of_withdrawals >= LIMIT_OF_WITHDRAWALS:
        print("Operação falhou! Número máximo de saques diários atingido.")
    else:
        balance -= value
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extract += f"Saque: R$ {value:.2f} - {timestamp} \n"
        number_of_transactions += 1
        number_of_withdrawals += 1
        print("Saque realizado com sucesso!")

    return balance, extract, number_of_transactions, number_of_withdrawals


def show_extract(balance, extract):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extract else extract)
    print(f"\nSaldo: R$ {balance:.2f}")
    print("==========================================")


def run_atm():
    balance = 0
    limit = 500
    extract = ""
    number_of_transactions = 0
    number_of_withdrawals = 0
    LIMIT_OF_TRANSACTIONS = 10
    LIMIT_OF_WITHDRAWALS = 3

    while True:
        if number_of_transactions >= LIMIT_OF_TRANSACTIONS:
            print("Número máximo de transações diárias atingido.")
            break

        option = mostrar_menu()

        if option == "1":
            balance, extract, number_of_transactions = deposit(
                balance, extract, number_of_transactions
            )

        elif option == "2":
            balance, extract, number_of_transactions, number_of_withdrawals = (
                withdraw(
                    balance,
                    extract,
                    number_of_transactions,
                    number_of_withdrawals,
                    limit,
                    LIMIT_OF_WITHDRAWALS,
                )
            )

        elif option == "3":
            show_extract(balance, extract)

        elif option == "0":
            break

        else:
            print(
                "Operação inválida, por favor selecione "
                "novamente a operação desejada."
            )


run_atm()
