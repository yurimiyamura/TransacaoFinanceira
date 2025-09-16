import pytest
from repository.acesso_dados import AcessoDados
from services.executar_transacao import ExecutarTransacaoFinanceira

def setup_executor():
    #Cria repositório e executor para cada teste
    repositorio = AcessoDados()
    executor = ExecutarTransacaoFinanceira(repositorio)
    return repositorio, executor

# Testa uma transferência de sucesso
def test_transferencia_sucesso(capsys):
    repositorio, executor = setup_executor()
    executor.transferir(1, 938485762, 2147483649, 50)

    origem = repositorio.get_saldo(938485762)
    destino = repositorio.get_saldo(2147483649)

    assert origem.saldo == 130
    assert destino.saldo == 50

    captured = capsys.readouterr()
    assert "foi efetivada com sucesso" in captured.out

# Testa se a transferência é cancelada quando a conta de origem não existe
def test_transferencia_conta_origem_inexistente(capsys):
    _, executor = setup_executor()
    executor.transferir(2, 999999999, 2147483649, 50)

    captured = capsys.readouterr()
    assert "conta de origem não encontrada" in captured.out

# Testa se a transferência é cancelada quando a conta de destino não existe
def test_transferencia_conta_destino_inexistente(capsys):
    _, executor = setup_executor()
    executor.transferir(3, 938485762, 999999999, 50)

    captured = capsys.readouterr()
    assert "conta de destino não encontrada" in captured.out

def test_transferencia_saldo_insuficiente(capsys):
    repositorio = AcessoDados()
    executor = ExecutarTransacaoFinanceira(repositorio)

    executor.transferir(4, 938485762, 2147483649, 1000)

    captured = capsys.readouterr()
    assert "cancelada: saldo insuficiente" in captured.out 

    conta_origem = repositorio.get_saldo(938485762)
    conta_destino = repositorio.get_saldo(2147483649)
    assert conta_origem.saldo == 180
    assert conta_destino.saldo == 0



# Testa se a transferência é cancelada quando o valor é inválido (<= 0)
def test_transferencia_valor_invalido(capsys):
    _, executor = setup_executor()
    executor.transferir(5, 938485762, 2147483649, -50)

    captured = capsys.readouterr()
    assert "valor inválido" in captured.out
