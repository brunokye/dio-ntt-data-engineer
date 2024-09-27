# Simulador de Sistema Bancário

Este projeto simula o funcionamento de um sistema bancário utilizando Python. O programa permite a criação de usuários, contas correntes e a realização de operações básicas como depósitos, saques e visualização de extratos. Todas as interações são feitas através do terminal.

## Funcionalidades

- **Criar Usuário**: Permite adicionar um novo usuário ao sistema, solicitando nome, CPF e endereço.
- **Login**: Permite que um usuário existente faça login utilizando seu CPF.
- **Criar Conta Corrente**: O usuário logado pode criar até três contas correntes.
- **Depósito**: Permite adicionar valores ao saldo da conta, desde que o valor seja maior que zero.
- **Saque**: Possibilita retirar valores do saldo, respeitando as seguintes regras:
  - O valor do saque não pode exceder o saldo disponível.
  - O valor não pode ser negativo.
  - Existe um limite diário de saque (R$ 500,00).
  - Há um limite máximo de três saques por dia.
- **Extrato**: Exibe todas as movimentações realizadas (depósitos e saques) e o saldo atual:
  - Há um limite no sistema de 10 transações por dia (incluindo depósitos e saques).
- **Sair**: Encerra o programa.

## Estrutura do Código

### Variáveis Globais
- `users`: Dicionário que armazena os usuários cadastrados.
- `accounts`: Lista que armazena as contas correntes criadas.
- `current_user`: Armazena o CPF do usuário logado.
- `account_number`: Controla o número das contas correntes.

### Funções
- `show_menu()`: Exibe o menu principal para o usuário.
- `create_user()`: Cria um novo usuário.
- `login_user()`: Realiza o login de um usuário.
- `create_checking_account()`: Cria uma conta corrente para o usuário logado.
- `deposit(account)`: Realiza um depósito na conta selecionada.
- `withdraw(account)`: Realiza um saque da conta selecionada.
- `show_extract(account)`: Exibe o extrato da conta selecionada.
- `select_account()`: Permite ao usuário selecionar uma conta corrente para operações.
- `run_atm()`: Controla o fluxo principal do programa, permitindo ao usuário realizar operações.
