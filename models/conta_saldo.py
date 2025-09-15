class ContasSaldo:
    #Entidade de domínio: Conta com regras de débito e crédito

    def __init__(self, conta: int, saldo: float):
        self.__conta = conta
        self.__saldo = saldo

    @property
    def conta(self) -> int:
        return self.__conta

    @property
    def saldo(self) -> float:
        return self.__saldo

    def debitar(self, valor: float) -> bool:
        #Debita um valor, se houver saldo suficiente
        if valor <= 0:
            raise ValueError("O valor do débito deve ser positivo")

        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False

    def creditar(self, valor: float):
        #Credita um valor na conta
        if valor <= 0:
            raise ValueError("O valor do crédito deve ser positivo")

        self.__saldo += valor
