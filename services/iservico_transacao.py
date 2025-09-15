from abc import ABC, abstractmethod


class IServicoTransacao(ABC):
    #Interface para serviços de transação financeira

    @abstractmethod
    def transferir(self, correlation_id: int, conta_origem: int, conta_destino: int, valor: float):
        pass
