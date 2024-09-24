menu = """

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
        print("Depósito")

    elif option == "2":
        print("Saque")

    elif option == "3":
        print("Extrato")
    elif option == "0":
        break

    else:
        print(
            "Operação inválida, por favor selecione novamente "
            "a operação desejada."
        )
