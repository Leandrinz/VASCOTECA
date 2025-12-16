from Registro_Vasco.funcoes.arquivo import *
import pathlib
from unittest.mock import MagicMock, mock_open, patch
import builtins
import pytest
import os

# 1 - ARQUIVO_EXISTE

# A fixture "tmp_path" é fornecida pelo pytest e cria um diretório temporário, deixando os testes mais seguros.

def test_arquivo_existe_retorna_true_se_existe(tmp_path: pathlib.Path):
    """
    Testa se a função retorna true quando o arquivo realmente existe
    """
    # 1. Preparação
    # Cria um arquivo temporário dentro do diretório tmp_path
    nome_arquivo = tmp_path / "teste_existente.txt"
    nome_arquivo.write_text("Conteúdo do teste")

    # 2. Ação
    # Chama a função com o caminho do arquivo temporário

    resultado = arquivoExiste(nome_arquivo) 

    # 3. Assert
    # Verifica se o resultado é True
    assert resultado is True


def test_arquivo_existe_retorna_false_se_arquivo_nao_existe(tmp_path: pathlib.Path):
    """
    Testa se a função retorna False caso o arquivo não exista
    """
    # 1. Preparação
    # Cria um caminho para um arquivo que não existe no diretório temporário
    nome_arquivo_inexistente = tmp_path / "Arquivo_inexistente.txt"

    # 2. Ação
    # Chama a função
    resultado = arquivoExiste(nome_arquivo_inexistente)

    # 3. Assert 
    # Verifica se o resultado é false
    assert resultado is False



# 2 - CRIAR_ARQUIVO

# O fixture capsys é usado para capturar a saída do console (print)

def test_criar_arquivo_cria_o_arquivo_e_imprime_sucesso(tmp_path: pathlib.Path, capsys):
    """
    Testa se a função realmente cria o arquivo e se imprime a mensagem do usuário
    """
    # 1. Preparação
    nome_arquivo = "Teste_novo.txt"
    # Monta o caminho completo no diretório temporário
    caminho_completo = tmp_path / nome_arquivo

    # 2. Ação 
    CriarArquivo(caminho_completo)

    # Captura o que foi impresso no console (stdout)
    saida_capturada = capsys.readouterr()

    # 3. Assert

    # a) Verifica se o caminho foi criado com sucesso usando o método is_file()
    assert caminho_completo.is_file() is True

    # b) Verifica se a mensagem de sucesso foi impressa corretamente
    f"Arquivo {caminho_completo} criado com sucesso!\n" in saida_capturada.out

def test_criar_arquivo_nao_cria_retorna_false(tmp_path: pathlib.Path, capsys):
    """
    Testa se a função retorna false quando o arquivo não é criado
    """
    # 1. Preparação
    nome_arquivo =  "/caminho_proibido_do_sistema_de_teste/erro_teste.txt"

    caminho_completo = tmp_path / nome_arquivo

    # 2. Ação
    CriarArquivo(caminho_completo)

    # Captura o que foi impresso no console (stdout)
    
    saida_capturada = capsys.readouterr()

    # 3. Assert

    # Verifica se o caminho deu erro na criação
    assert caminho_completo.is_file() is False

    # Verifica a mensagem de erro foi impressa
    mensagem_esperada = "Houve um erro na criação do arquivo!"
    assert mensagem_esperada in saida_capturada.out



# 3 - CADASTRAR TÍTULOS

def test_cadastrar_titulo_com_sucesso(tmp_path: pathlib.Path, capsys):
    """
    Testa se cadastrarTítulos escreve o título formatado corretamente e imprime corretamente
    """
   
    nome_arquivo = tmp_path / "titulos.txt"
    titulo_teste = "Libertadores"
    ano_teste = 1998

    cadastrarTitulos(nome_arquivo, titulo_teste, ano_teste)
    saida_capturada = capsys.readouterr()

    mensagem_esperada = f"Novo registro de {titulo_teste} adicionado."
    assert mensagem_esperada in saida_capturada.out


def test_cadastrar_titulo_com_erro(tmp_path: pathlib.Path, capsys):
    """
    Testa se cadastrarTítulos escreve o aviso de erro programado ao encontrar um erro no cadastro
    """

    nome_errado_arquivo = tmp_path / "/caminho/impossivel/de/abrir" # Nome errado do arquivo que o usuário digitou
    titulo_teste = "Copa do Brasil"
    ano_teste = 2025

    cadastrarTitulos(nome_errado_arquivo, titulo_teste, ano_teste)
    saida_capturada = capsys.readouterr()

    mensagem_esperada = "Houve um erro na abertura do arquivo"

    assert mensagem_esperada in saida_capturada.out


# 4 - LERHINO

def test_ler_hino(tmp_path: pathlib.Path, capsys):
    """
    Testa se lerHino abre corretamente o arquivo, toca a música (simulada)
    e imprime as linhas completas do Hino do Vasco.
    """

    # 1. Preparação
    nome_arquivo = tmp_path / "hino_teste.txt"
    hino_completo = """Vamos todos cantar de coração
    A Cruz de Malta é o meu pendão
    Tu tens o nome do heroico português
    Vasco da Gama, a tua fama assim se fez

    Tua imensa torcida é bem feliz
    Norte-Sul, Norte-Sul deste Brasil
    Tua estrela, na terra a brilhar
    Ilumina o mar

    No atletismo, és um braço
    No remo, és imortal
    No futebol, és um traço
    De união Brasil-Portugal

    No atletismo, és um braço
    No remo, és imortal
    No futebol, és um traço
    De união Brasil-Portugal

    Vamos todos cantar de coração
    A Cruz de Malta é o meu pendão!
    Tu tens o nome do heroico português
    Vasco da Gama, a tua fama assim se fez

    Tua imensa torcida é bem feliz
    Norte-Sul, Norte-Sul deste Brasil
    Tua estrela, na terra a brilhar
    Ilumina o mar

    No atletismo, és um braço
    No remo, és imortal
    No futebol, és um traço
    De união Brasil-Portugal

    No atletismo, és um braço
    No remo, és imortal
    No futebol, és um traço
    De união Brasil-Portugal
    """
    nome_arquivo.write_text(hino_completo, encoding="utf-8")

    # 2. Mocks para não tocar música nem esperar tempo
    with (
        patch("Registro_Vasco.funcoes.arquivo.pygame.mixer.init"),
        patch("Registro_Vasco.funcoes.arquivo.pygame.mixer.music.load"),
        patch("Registro_Vasco.funcoes.arquivo.pygame.mixer.music.play"),
        patch("Registro_Vasco.funcoes.arquivo.time.sleep", return_value=None),
        patch("Registro_Vasco.funcoes.arquivo.cabeçalho", side_effect=lambda x: print(x))
    ):
        lerHino(nome_arquivo)

    # 3. Captura o que foi impresso
    saida = capsys.readouterr().out

    # 4. Asserts
    assert "HINO DO VASCO" in saida
    assert "Vamos todos cantar de coração" in saida
    assert "De união Brasil-Portugal" in saida


# 5 - LERARQUIVO

def test_ler_arquivo_existente(tmp_path: pathlib.Path, capsys):
    """
    Testa se a função lê corretamente um arquivo válido e imprime o conteúdo formatado
    """
    # 1. Preparação
    nome_arquivo = tmp_path / "titulos.txt"
    nome_arquivo.write_text("Libertadores:1998\nCopa do Brasil:2011\n", encoding="utf-8")

    # 2. Mock do cabeçalho
    with patch("Registro_Vasco.funcoes.arquivo.cabeçalho", side_effect=lambda x: print(f"CAB:{x}")):
        lerArquivo(nome_arquivo)
    
    # 3. Captura da saída
    saida = capsys.readouterr().out

    # 4. Assert
    assert "CAB:" in saida
    assert "Libertadores" in saida
    assert "1998" in saida
    assert "Copa do Brasil" in saida
    assert "2011" in saida


def test_ler_arquivo_inexistente(capsys):
    """
    Testa se a função imprime a mensagem de erro quando o arquivo não existe
    """
    nome_invalido = "arquivo_que_nao_existe.txt"

    lerArquivo(nome_invalido)

    saida = capsys.readouterr().out
    assert "Houve um erro ao ler o arquivo" in saida
    assert "No such file or directory" in saida or "não encontrado" in saida.lower()


# 6 - LER TABELA_IDOLOS_TITULOS
def test_ler_tabela_brasileirao_exibe_formatacao_correta(monkeypatch, tmp_path: pathlib.Path, capsys):
    """
    Testa se lerTabela_Idolos_Titulos imprime corretamente os dados formatados
    quando o arquivo é o da Posição_Brasileirão_Vasco.txt
    """
    # 1. Preparação
    nome_arquivo = tmp_path / "Posição_Brasileirão_Vasco.txt"
    conteudo = "1:Vasco:100\n2:Flamengo:85\n"
    nome_arquivo.write_text(conteudo, encoding="utf-8")

    # 2. Muda o diretório atual pro tmp_path
    monkeypatch.chdir(tmp_path)

    # 3. Mock do cabeçalho
    with patch("Registro_Vasco.funcoes.arquivo.cabeçalho", side_effect=lambda x: print(f"CAB: {x}")):
        lerTabela_Idolos_Titulos("Posição_Brasileirão_Vasco.txt")

    # 4. Captura de saída
    saida = capsys.readouterr().out

    # 5. Assert
    assert "CAB:" in saida
    assert "POS" in saida and "TIME" in saida and "PONTOS" in saida
    assert "Vasco" in saida
    assert "Flamengo" in saida


def test_ler_idolos_exibe_formatacao_correta(monkeypatch, tmp_path: pathlib.Path, capsys):
    """
    Testa se lertabela_Idolos_Titulos imprime corretamente os dados formatados
    quando o arquivo é o do Ídolos_Vasco.txt
    """
    # 1. Preparação
    nome_arquivo = tmp_path / "Ídolos_Vasco.txt"
    conteudo = (
        "Dinamite:999:199\n"
        "Edmundo:140:240"
    )
    nome_arquivo.write_text(conteudo, encoding="utf-8")

    # 2. Muda o diretório atual pro tmp_path
    monkeypatch.chdir(tmp_path)

    # 3. Mock do Cabeçalho
    with patch("Registro_Vasco.funcoes.arquivo.cabeçalho", side_effect=lambda x: print(f"CAB: {x}")):
        lerTabela_Idolos_Titulos("Ídolos_Vasco.txt")
    
    # 4. Captura de saída
    saida = capsys.readouterr().out

    # 5. Assert
    assert "Dinamite" and "999" and "199" in saida
    assert "Edmundo" and "140" and "240" in saida


def test_ler_tabela_exibe_erro_quando_arquivo_inexistente(capsys):
    """
    Testa se a função imprime corretamente a mensagem de erro
    ao tentar ler um arquivo inexistente
    """

    nome_arquivo_inexistente = "arquivo_que_nao_existe"

    lerTabela_Idolos_Titulos(nome_arquivo_inexistente)
    saida = capsys.readouterr().out

    assert "Erro ao ler arquivo" in saida

# 7 - CADASTRAR JOGADORES
def test_cadastrar_jogadores_corretamente(tmp_path: pathlib.Path, capsys):
    """
    Testa se o cadastro de jogadores ocorre normalmente com 
    dados corretos.
    """
    # 1. Preparação
    nome_arquivo = tmp_path / "ElencoAtual.txt"
    jogador_teste = "Coutinho"
    posicao_teste = "Atacante"
    cadastrarJogadores(nome_arquivo, jogador_teste, posicao_teste)
    
    # 2. Saida
    saida = capsys.readouterr().out
    conteudo = nome_arquivo.read_text()

    # 3. Assert
    assert f"{jogador_teste}:{posicao_teste}" in conteudo
    assert f"{jogador_teste} adicionado - Posição: {posicao_teste}" in saida 


def test_cadastrar_jogadores_erro_caminho_invalido(tmp_path: pathlib.Path,capsys):
    """
    Testa se a saída de erro ocorre normalmente ao encontrar um caminho inválido
    """
    camimho_invalido = tmp_path / "caminho/invalido/erro/certeza.txt"

    cadastrarJogadores(camimho_invalido, "Vegetti", "Atacante")

    saida = capsys.readouterr().out

    assert "Houve um erro no registro" in saida


# 8 - CADASTRAR ÍDOLOS
def test_cadastrar_idolos_corretamente(tmp_path: pathlib.Path, capsys):
    """
    Testa se a função cadastrarIdolos cadastra com sucesso após entradas
    corretas
    """
    # 1. Preparação
    nome_arquivo = tmp_path / "Ídolos_Vasco"
    idolo_teste = "Dinamite"
    gols_teste = 1000
    jogos_teste = 999
    posicao_teste = "Atacante"

    cadastrarIdolos(nome_arquivo, idolo_teste, gols_teste, jogos_teste, posicao_teste)

    # 2. Captura saída
    saida = capsys.readouterr().out
    conteudo = nome_arquivo.read_text()

    # 3. Assert
    assert f"{idolo_teste} adicionado no Hall dos Ídolos!" in saida
    assert f"{idolo_teste}:{gols_teste} Gols :{jogos_teste} Jogos :{posicao_teste}" in conteudo


def test_cadastrar_idolo_com_erro(tmp_path: pathlib.Path, capsys):
    """
    Testa se o cadastrarIdolos exibe mensagem de erro
    quando um arquivo é inválido.
    """
    caminho_invalido = tmp_path / "caminho/invalido/certeza.txt"

    cadastrarIdolos(caminho_invalido, "Dinamite", 1000, 1020, "Atacante")

    saida = capsys.readouterr().out

    assert "Houve um erro no registro" in saida


# 9. ATUALIZAR POSIÇÃO
def test_atualizar_posicao_escreve_20_times(tmp_path, monkeypatch, capsys):
    """
    Testa se atualizarPosição escreve corretamente 20 linhas no arquivo e imprime a mensagem final.
    """
    nome_arquivo = tmp_path / "tabela.txt"

    # Cria 20 entradas simuladas (nomes e pontos)
    entradas = []
    for i in range(1, 21):
        entradas.append(f"Time{i}")   # nome do time
        entradas.append("10")         # pontos do time

    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    atualizarPosição(str(nome_arquivo))

    conteudo = nome_arquivo.read_text(encoding="utf-8")
    saida = capsys.readouterr().out

    # Verifica que há 20 linhas e contém partes esperadas
    linhas = conteudo.strip().split("\n")
    assert len(linhas) == 20
    assert "1:Time1:10" in conteudo
    assert "20:Time20:10" in conteudo
    assert "Tabela do Brasileirão atualizada" in saida


def test_atualizar_posicao_erro_arquivo_invalido(tmp_path: pathlib.Path, capsys):
    """
    Testa se a função atualizar_posicao retorna erro
    ao encontrar um arquivo inexistente.
    """
    arquivo_inexistente = tmp_path / "arquivo/inexistente/certeza.txt"

    atualizarPosição(arquivo_inexistente)

    saida = capsys.readouterr().out

    assert "Houve um erro na atualização" in saida