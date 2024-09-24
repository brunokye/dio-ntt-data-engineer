menu = """
Use apenas números durante toda interação com o sistema.
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

balance = 0
limit = 500
extract = ""
number_of_withdrawals = 0
LIMIT_OF_WITHDRAWALS = 3

while True:
    option = input(menu)

    if option == "1":
        value = float(input("Informe o valor do depósito: "))

        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif option == "2":
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
            extract += f"Saque: R$ {value:.2f}\n"
            number_of_withdrawals += 1
            print("Saque realizado com sucesso!")

    elif option == "3":
        print("\n================ EXTRATO ================")
        print(
            "Não foram realizadas movimentações." if not extract else extract
        )
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")

    elif option == "0":
        break

    else:
        print(
            "Operação inválida, por favor selecione novamente "
            "a operação desejada."
        )
