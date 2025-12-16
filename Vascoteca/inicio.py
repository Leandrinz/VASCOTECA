import Registro_Vasco.funcoes.arquivo as rv
import Registro_Vasco.funcoes.funcionalidades as func
cores = {
    'limpa': '\033[0m',         # Resetar estilos
    'titulo': '\033[1;30;47m',  # Títulos: preto negrito com fundo branco
    'mensagem': '\033[1;0;37m', # Mensagens básicas: branco negrito sem fundo
    'aviso': '\033[1;31m',      # Avisos: vermelho forte
    'erro': '\033[1;37;41m',    # Erros: branco negrito com fundo vermelho
    'input': '\033[1;36m',      # Entradas do usuário: ciano negrito
    'sucesso': '\033[1;32m',    # Sucesso: verde negrito
    'info': '\033[90m'          # Informações secundárias: cinza suave
}


while True:

    resposta = func.menu(["Ver títulos", "Ver Jogadores do elenco atual", "Ver ídolos", "Ver Hino do time", "Ver posição atual do time no Brasileirão", "Cadastrar títulos", "Cadastrar Jogadores", "Cadastrar ídolos", "Atualizar posição do time no Brasileirão", "Sair do programa"])
    match resposta:
        case 1:
            
            arq = 'Títulos_Vasco.txt'

            # Cria o arquivo de títulos caso não exista ainda
            if (rv.arquivoExiste(arq)) == False:
                rv.CriarArquivo(arq)
            rv.lerArquivo(arq)

    
    
        case 2:
            
            arq = 'ElencoAtual.txt'

            # Cria o arquivo do elenco atual caso não exista ainda
            if not rv.arquivoExiste(arq):
                rv.CriarArquivo(arq)
            rv.lerArquivo(arq)



    
    
        case 3:
            
            arq = 'Ídolos_Vasco.txt'

            # Cria o arquivo de ídolos caso não exista ainda
            if not rv.arquivoExiste(arq):
                rv.CriarArquivo(arq)
            rv.lerTabela_Idolos_Titulos(arq)

    
    
        case 4:
            
            arq = 'Hino_Vasco.txt'
            
            # Cria o arquivo do hino do vasco caso não exista ainda
            if not rv.arquivoExiste(arq):
                rv.CriarArquivo(arq)
            rv.lerHino(arq)


    
    
        case 5:
            
            arq = 'Posição_Brasileirão_Vasco.txt'
            
            # Cria o arquivo da posição atual caso não exista ainda
            if not rv.arquivoExiste(arq):
                rv.CriarArquivo(arq)
            rv.lerTabela_Idolos_Titulos(arq)
        


        case 6:

            arq = 'Títulos_Vasco.txt'

            # Cadastra Títulos e ano de conquista
            titulo = str(input(f"{cores['input']}Título:{cores['limpa']} "))
            ano = int(input(f"{cores['input']}Ano de conquista - {titulo}: {cores['limpa']} "))
            rv.cadastrarTitulos(arq, titulo, ano)
        

        case 7:
            arq = 'ElencoAtual.txt'

            # Cadastra Jogador e sua posição
            Nome = str(input(f"{cores['input']}Nome do Jogador:{cores['limpa']} "))
            Posicao = input(f"{cores['input']}Posição:{cores['limpa']} ")
            rv.cadastrarJogadores(arq, Nome, Posicao)
        

        case 8:
            arq = 'Ídolos_Vasco.txt'

            # Cadastrar Ídolos
            Nome = str(input(f"{cores['input']}Nome do ídolo:{cores['limpa']} "))
            Gols = str(input(f"{cores['input']}Gols feitos:{cores['limpa']} "))
            Jogos = int(input(f"{cores['input']}Número de jogos:{cores['limpa']} "))
            Posicao = str(input(f"{cores['input']}Posição:{cores['limpa']} "))
            rv.cadastrarIdolos(arq, Nome, Gols, Jogos, Posicao)

        
        case 9:

            # Atualiza tabela do brasileirão
            arq = 'Posição_Brasileirão_Vasco.txt'
            rv.atualizarPosição(arq)


        case 10:
            print(f"{cores["mensagem"]}SAINDO DO PROGRAMA...{cores['limpa']}")
            break

    
