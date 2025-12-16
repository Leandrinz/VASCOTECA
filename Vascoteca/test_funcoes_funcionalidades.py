from Registro_Vasco.funcoes.funcionalidades import *
from unittest.mock import patch, call
import pathlib

# 1: --- TESTE LINHA ---

# 1.1 Teste padrão e especializado
def test_linha():
    assert "-"  in linha()
    assert "-"  in linha(20) 


# 2: --- TESTE LEIAINT ---

# 2.1 Teste de Entrada válida
@patch('builtins.input', return_value='5')
def test_leiaint_valida(mock_input):
    assert leiaint() == 5

# 2.2 Teste de Entrada Inválida (String)
@patch('builtins.input', side_effect=['nao_e_numero', '', '10'])
def test_leiaint_invalida(mock_input):
    assert leiaint() == 10

# 2.3 Teste de KeyboardInterrupt
@patch('builtins.input', side_effect=[KeyboardInterrupt, '10'])
def test_leiaint_keyboard_interrurpt(mock_input):
    assert leiaint() == 10

# 3: --- TESTE CABEÇALHO --- 

# 3.1 Teste Básico de Formatação e Chamadas
def test_cabecalho_formato_padrao(tmp_path:pathlib.Path, capsys):
    """
    Testa se o cabeçalho funciona
    """
    cabeçalho("Vasco")
    saida = capsys.readouterr().out

    assert "Vasco" and "-" in saida
