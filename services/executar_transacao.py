from repository.irepository import IRepositorioContas
from services.iservico_transacao import IServicoTransacao

"""
Classe que executa a transação financeira através de uma sequência condicional
- transferir: Executa a transferência entre duas contas
        Características:
        - A transação falha se a conta de origem não existir.
        - A transação falha se a conta de destino não existir.
        - A transação falha se não houver saldo suficiente.
        - Caso contrário, os valores são debitados/creditados e salvos.
"""

class ExecutarTransacaoFinanceira(IServicoTransacao):
    #Serviço que orquestra transferências financeiras

    def __init__(self, repositorio: IRepositorioContas):
        self.repositorio = repositorio

    def validar_transferencia(self, correlation_id: int, conta_origem, conta_destino, valor: float) -> bool:
        #Valida regras de negócio antes de executar a transferência

        if conta_origem is None:
            print(f"Transação {correlation_id} cancelada: conta de origem não encontrada!")
            return False

        if conta_destino is None:
            print(f"Transação {correlation_id} cancelada: conta de destino não encontrada!")
            return False

        if valor <= 0:
            print(f"Transação {correlation_id} cancelada: valor inválido ({valor}).")
            return False

        if conta_origem.saldo < valor:
            print(f"Transação {correlation_id} cancelada: saldo insuficiente.")
            return False

        return True

    def transferir(self, correlation_id: int, conta_origem_id: int, conta_destino_id: int, valor: float):
        conta_saldo_origem = self.repositorio.get_saldo(conta_origem_id)
        conta_saldo_destino = self.repositorio.get_saldo(conta_destino_id)

        # Se falhar em qualquer validação, não continua
        if not self.validar_transferencia(correlation_id, conta_saldo_origem, conta_saldo_destino, valor):
            return

        # Execução (regras encapsuladas na entidade)
        conta_saldo_origem.debitar(valor)
        conta_saldo_destino.creditar(valor)

        # Persistência
        self.repositorio.atualizar(conta_saldo_origem)
        self.repositorio.atualizar(conta_saldo_destino)

        print(f"Transação {correlation_id} foi efetivada com sucesso! "
              f"Novos saldos: Conta Origem:{conta_saldo_origem.saldo} | Conta Destino:{conta_saldo_destino.saldo}")