from abc import ABC, abstractmethod
from models.conta_saldo import ContasSaldo


class IRepositorioContas(ABC):
    #Interface para repositórios de contas

    @abstractmethod
    def get_saldo(self, conta_id: int) -> ContasSaldo:
        pass

    @abstractmethod
    def atualizar(self, dado: ContasSaldo) -> bool:
        pass
