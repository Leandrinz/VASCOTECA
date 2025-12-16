cores = {
    'limpa': '\033[0m',         # Resetar estilos
    'titulo': '\033[1;30;47m',  # Títulos: preto negrito com fundo branco
    'mensagem': '\033[1;0;37m',     # Mensagens básicas: branco negrito sem fundo
    'aviso': '\033[1;31m',      # Avisos: vermelho forte
    'erro': '\033[1;37;41m',    # Erros: branco negrito com fundo vermelho
    'input': '\033[1;36m',      # Entradas do usuário: ciano negrito
    'sucesso': '\033[1;32m',    # Sucesso: verde negrito
    'info': '\033[90m'          # Informações secundárias: cinza suave
}



def linha(tam = 42):
    return(f'{cores["mensagem"]}- {cores["limpa"]}' * tam)


def leiaint(msg = 0):
    while True:
        try:
            msg = int(input(f"{cores['input']}Sua opção: {cores['limpa']}"))
        except ValueError:
            print(f"{cores['erro']}Erro! Digite um valor inteiro!!!{cores['limpa']}")
        except KeyboardInterrupt:
            print(f"{cores['aviso']}O usuário não digitou o número!{cores['limpa']}")
        else:
            return msg



def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho(f"{cores["titulo"]}CONHEÇA A HISTÓRIA DO GIGANTE DA COLINA{cores['limpa']}".center(42))
    c = 1
    for item in lista:
        print(f"{cores["mensagem"]}{c} - {item}{cores['limpa']}")
        c += 1
    print(linha())
    opc = leiaint()
    return opc
