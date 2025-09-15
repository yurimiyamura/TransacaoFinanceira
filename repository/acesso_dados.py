from models.conta_saldo import ContasSaldo
from repository.irepository import IRepositorioContas

"""
Classe responsável por simular o acesso a dados (repositório em memória).
- get_saldo: retorna o saldo de acordo com o id da conta
- atualizar: atualiza o saldo da conta caso ele seja alterado, substituindo a versão anterior
"""

class AcessoDados(IRepositorioContas):
    #Implementação em memória do repositório de contas

    def __init__(self):
        self.tabela_saldos = [
            ContasSaldo(938485762, 180),
            ContasSaldo(347586970, 1200),
            ContasSaldo(2147483649, 0),
            ContasSaldo(675869708, 4900),
            ContasSaldo(238596054, 478),
            ContasSaldo(573659065, 787),
            ContasSaldo(210385733, 10),
            ContasSaldo(674038564, 400),
            ContasSaldo(563856300, 1200),
        ]

    def get_saldo(self, conta_id: int) -> ContasSaldo:
        return next((x for x in self.tabela_saldos if x.conta == conta_id), None)

    def atualizar(self, dado: ContasSaldo) -> bool:
        try:
            self.tabela_saldos = [x for x in self.tabela_saldos if x.conta != dado.conta]
            self.tabela_saldos.append(dado)
            return True
        except Exception as e:
            print(e)
            return False
