from Registro_Vasco.funcoes.funcionalidades import *   
from Registro_Vasco import *
import pygame
import time


def arquivoExiste(nome):
    try:
        a = open(nome,"rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("\033[1;31mHouve um erro na criação do arquivo!\033[0m")
    else:
        print(f"\033[1;32mArquivo {nome} criado com sucesso!\033[0m")


def lerArquivo(nome):
    a = None
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except Exception as erro:
        print("\033[1;31mHouve um erro ao ler o arquivo:\033[0m ", erro)
    else:
        cabeçalho(f"{nome}")
        for linha in a:
            dado = linha.split(':')
            dado[1] = dado[1].replace('\n', '')
            print(f"\033[1;0;37m{dado[0]:<30}{dado[1]:>3}\033[0m")
    finally:     
        if a is not None:
            a.close()


def lerTabela_Idolos_Titulos(nome):
    a = None
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except Exception as erro:
        print(f"\033[1;31mErro ao ler arquivo: {erro}\033[0m")
    else:
        cabeçalho(f"{nome}")
        
        if nome == 'Posição_Brasileirão_Vasco.txt':
            print(f"{"POS":<5}| {"TIME":<17}| {"PONTOS":>5}")
            print("-" * 35)
            for linha in a:
                dado = linha.split(":")
                dado = [d.replace('\n', '') for d in dado]

                print(f"{dado[0]:<5} {dado[1]:<17} {dado[2]:>5}")


        if nome == 'Ídolos_Vasco.txt':
            print(f"{"NOME":<25}| {"GOLS":<17}| {"JOGOS":>5}")
            print("-" * 35)

            for linha in a:
                dado = linha.split(":")
                dado = [d.replace('\n', '') for d in dado]

                print(f"\033[1;0;37m{dado[0]:<25} {dado[1]:<17} {dado[2]:>5}\033[0m")
    
    finally:
        if a is not None:
            a.close()




def lerHino(nome):
    a = None
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except Exception as erro:
        print(f"\033[1;31mHouve um erro ao ler o arquivo: {erro}\033[0m")
    else:
        cabeçalho("HINO DO VASCO")
        pygame.mixer.init()
        pygame.mixer.music.load("ex021vasco.mp3")
        pygame.mixer.music.play()
        time.sleep(11.5)
        for linha in a:
            print(linha)
            time.sleep(2.8)
    finally:
        if a is not None:
            a.close()


def cadastrarTitulos(arq, titulo, ano):
    try: 
        a = open(arq, 'at')
    except:
        print("\033[1;31mHouve um erro na abertura do arquivo\033[0m")
    else:
        try:
            a.write(f"{titulo}:{ano}\n")
        except:
            print("\033[1;31mHouve um erro no registro\033[0m")
        else:
            print(f"\033[1;32mNovo registro de {titulo} adicionado.\033[0m")
            a.close()


def cadastrarJogadores(arq, Nome, Posicao):
    try:
        a = open(arq, 'at')
    except:
        print("\033[1;31mHouve um erro no registro\033[0m")
    else:
        try:
            a.write(f"{Nome}:{Posicao}\n")
        except:
            print("\033[1;31mHouve um erro no registro\033[0m")
        else:
            print(f"\033[1;32m{Nome} adicionado - Posição: {Posicao}\033[0m")
            a.close()


def cadastrarIdolos(arq, Nome, Gols, Jogos, Posicao):
    try:
        a = open(arq, 'at')
    except:
        print("\033[1;31mHouve um erro no registro\033[0m")
    else: 
        try:
            a.write(f"{Nome}:{Gols} Gols :{Jogos} Jogos :{Posicao}\n")
        except:
            print("\033[1;31mHouve um erro no registro\033[0m")
        else:
            print(f"\033[1;32m{Nome} adicionado no Hall dos Ídolos!\033[0m")
            a.close()


def atualizarPosição(arq):
    try: 
        a = open(arq, 'w', encoding='utf-8')
    except:
        print("\033[1;31mHouve um erro na atualização\033[0m")
    else:
        try:
            for i in range(1, 21):
                time = str(input(f"Time da {i}º Posição: "))
                pontos = int(input(f"Pontos do {time}: "))
                a.write(f"{i}:{time}:{pontos}\n")
        except:
            print("\033[1;31mHouve um erro no registro!\033[0m")
        else:
            print("\033[1;32mTabela do Brasileirão atualizada\033[0m")
        finally:
            a.close()