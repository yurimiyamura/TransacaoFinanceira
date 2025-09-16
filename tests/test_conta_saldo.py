import pytest
from models.conta_saldo import ContasSaldo

# Testa se o débito funciona corretamente quando há saldo suficiente
def test_debitar_com_saldo_suficiente():
    conta = ContasSaldo(123, 100)
    resultado = conta.debitar(50)
    assert resultado is True
    assert conta.saldo == 50

# Testa se o débito é rejeitado quando não há saldo suficiente
def test_debitar_com_saldo_insuficiente():
    conta = ContasSaldo(123, 40)
    resultado = conta.debitar(100)
    assert resultado is False
    assert conta.saldo == 40  

# Testa se o crédito de um valor positivo funciona corretamente
def test_creditar_valor_positivo():
    conta = ContasSaldo(123, 100)
    conta.creditar(50)
    assert conta.saldo == 150      

# Testa se o débito com valor negativo gera erro (regra de domínio)
def test_debitar_valor_negativo_dispara_erro():
    conta = ContasSaldo(123, 100)
    with pytest.raises(ValueError):
        conta.debitar(-10)

# Testa se o crédito com valor negativo gera erro (regra de domínio)
def test_creditar_valor_negativo_dispara_erro():
    conta = ContasSaldo(123, 100)
    with pytest.raises(ValueError):
        conta.creditar(-5)
