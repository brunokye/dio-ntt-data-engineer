# Simulador de Sistema Bancário v2

Este projeto simula o funcionamento de um sistema bancário utilizando Python. O programa permite a criação de usuários, contas correntes e a realização de operações básicas como depósitos, saques e visualização de extratos. Todas as interações são feitas através do terminal.

## Funcionalidades

- **Criar Usuário**: Permite adicionar um novo usuário ao sistema, solicitando nome, CPF e endereço.
- **Login**: Permite que um usuário existente faça login utilizando seu CPF.
- **Criar Conta Corrente**: O usuário logado pode criar até três contas correntes.
- **Depósito**: Permite adicionar valores ao saldo da conta, desde que o valor seja maior que zero.
- **Saque**: Possibilita retirar valores do saldo, respeitando as seguintes regras:
  - O valor do saque não pode exceder o saldo disponível.
  - O valor não pode ser negativo.
  - Existe um limite diário de saque de R$ 500,00.
  - Há um limite máximo de três saques por dia.
- **Extrato**: Exibe todas as movimentações realizadas (depósitos e saques) e o saldo atual:
  - Há um limite no sistema de 10 transações por dia (incluindo depósitos e saques).
- **Sair**: Encerra o programa.

## Estrutura do Código

### Variáveis Globais
- `clients`: Dicionário que armazena os usuários cadastrados, usando o CPF como chave.
- `current_client`: Armazena o usuário que está atualmente logado.
- `account_number`: Controla o número das contas correntes a serem criadas.

### Classes
- `Transaction`: Classe abstrata que define o método `register` para registrar transações.
- `Deposit`: Implementa a operação de depósito, atualizando o saldo e o histórico de transações.
- `Withdrawal`: Implementa a operação de saque, respeitando as regras definidas.
- `History`: Armazena o histórico de transações realizadas em uma conta.
- `Account`: Classe abstrata que define a estrutura básica de uma conta bancária.
- `CheckingAccount`: Implementa a conta corrente, permitindo depósitos e saques.
- `Client`: Classe base para gerenciar usuários do sistema.
- `PhysicalPerson`: Extensão da classe `Client`, representando um cliente físico.

### Funções
- `create_user()`: Cria um novo usuário, solicitando informações necessárias.
- `login_user()`: Realiza o login de um usuário existente através do CPF.
- `create_checking_account(client, number)`: Cria uma conta corrente para o usuário logado.
- `select_account(client)`: Permite ao usuário selecionar uma conta corrente para realizar operações.
- `main()`: Controla o fluxo principal do programa, exibindo o menu e gerenciando as interações do usuário.
