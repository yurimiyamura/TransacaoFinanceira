# TransacaoFinanceira
Case de refatoração

Passos a implementar:
1. Corrija o que for necessario para resolver os erros de compilação.
2. Execute o programa para avaliar a saida, identifique e corrija o motivo de algumas transacoes estarem sendo canceladas mesmo com saldo positivo e outras sem saldo sendo efetivadas.
3. Aplique o code review e refatore conforme as melhores praticas(SOLID,Patterns,etc).
4. Implemente os testes unitários que julgar efetivo.
5. Crie um git hub e compartilhe o link respondendo o ultimo e-mail.


------------------------

1. Vamos entender o código
- O código busca criar um sistema de transação entre contas;
- Executa as transações com base no saldo da conta origem e imprime o resultado;
- Se tiver saldo: transfere o valor;
- Se não tiver saldo: cancela a transação.

2. Trancrever o código para Python 
- Classes
    - ContaSaldo: Representa a classe de criação de uma conta bancária, para guardar as informações financeiras do cliente
    - AcessaDados: Funciona como um banco de dados das contas
    - ExecutarTransacaoFinanceira: Classe que realiza a transferência entre as contas, herdando as características da classe "AcessaDados"

- Métodos
    - get_saldo: Retorna o saldo da conta de acordo com o "conta_id", caso não encontre, retorna None
    - atualizar: Atualiza a conta dentro da tabela de saldos
    - transferir: Verifica se a conta existe (se não, exibe um erro) e, se existir, verifica se possui saldo suficiente (se não, cancela a transação) e efetua a transferência
