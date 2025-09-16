import pytest
from repository.acesso_dados import AcessoDados
from models.conta_saldo import ContasSaldo

# Testa se o repositório retorna uma conta existente corretamente
def test_get_saldo_existente():
    repo = AcessoDados()
    conta = repo.get_saldo(938485762)
    assert conta is not None
    assert conta.conta == 938485762

# Testa se o repositório retorna None quando a conta não existe
def test_get_saldo_inexistente():
    repo = AcessoDados()
    conta = repo.get_saldo(999999999)
    assert conta is None

# Testa se a atualização de saldo realmente substitui o valor anterior
def test_atualizar_saldo():
    repo = AcessoDados()
    conta = ContasSaldo(938485762, 5000)    
    sucesso = repo.atualizar(conta)

    assert sucesso is True
    conta_atualizada = repo.get_saldo(938485762)
    assert conta_atualizada.saldo == 5000