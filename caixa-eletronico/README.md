# Simulador de Caixa Eletrônico

Este é um projeto simples que simula o funcionamento de um caixa eletrônico utilizando Python. O programa permite realizar operações básicas, como depósitos, saques, visualização de extrato e saída do sistema. Todas as interações com o programa são feitas através do terminal.

## Funcionalidades

- **Depósito**: Permite adicionar valores ao saldo da conta, desde que o valor seja maior que zero.
- **Saque**: Possibilita retirar valores do saldo, respeitando as seguintes regras:
  - O valor do saque não pode exceder o saldo disponível.
  - O valor não pode ser negativo.
  - Existe um limite diário de saque (R$ 500,00).
  - Há um limite máximo de três saques por dia.
- **Extrato**: Exibe todas as movimentações realizadas (depósitos e saques) e o saldo atual.
- **Sair**: Encerra o programa.
