from forca_words import *
from os import system as sys
from unicodedata import normalize

def remover_acentos(text):
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def escolher_menu(dificuldade_name):
    sys('cls')
    if dificuldade_name == 'english':
        while True:
            try:
                print(f'\t\tHANGMAN\n\n\t[1] PLAY\n\t[2] SELECT DIFICULTY (current - {dificuldade_name.upper()})\n\t[3] GAME RULES\n\t[4] QUIT\n')
                escolha_menu = int(input('--->'))
                break
            except ValueError:
                sys('cls')
                print('typed input must be integer, try again')
    else:
        while True:
            try:
                print(f'\t\tJOGO DA FORCA\n\n\t[1] INICIAR JOGO\n\t[2] SELECIONAR DIFICULDADE (atual - {dificuldade_name.upper()})\n\t[3] REGRAS DO JOGO\n\t[4] QUIT\n')
                escolha_menu = int(input('--->'))
                break
            except ValueError:
                sys('cls')
                print('Valor digitado deve ser inteiro, tente novamente')
        
    return escolha_menu

def escolher_dificuldade(dificuldade, dificuldade_name):
    sys('cls')
    if dificuldade_name == 'english':
        while True:
            try:
                print(f'\t\tIN WITCH DIFICULTY YOU WANT TO PLAY?\n\n\tcurrent dificulty - {dificuldade_name.upper()}\n\t[1] EAZY\n\t[2] MEDIUM\n\t[3] HARD\n\t[4] ENGLISH\n\n\t[5] MAIN MENU\n')
                escolha_dificuldade = int(input('--->'))
                break
            except ValueError:
                sys('cls')
                print('typed input must be integer, try again')
    else:
        while True:
            try:
                print(f'\t\tEM QUAL DIFICULDADE DESEJA JOGAR?\n\n\tdificuldade atual - {dificuldade_name.upper()}\n\t[1] EAZY\n\t[2] MEDIUM\n\t[3] HARD\n\t[4] ENGLISH\n\n\t[5] VOLTAR\n')
                escolha_dificuldade = int(input('--->'))
                break
            except ValueError:
                sys('cls')
                print('Valor digitado deve ser inteiro, tente novamente')
        

    if escolha_dificuldade == 1:
        dificuldade = easy.copy()
        dificuldade_name = 'easy'
    elif escolha_dificuldade == 2:
        dificuldade = medium.copy()
        dificuldade_name = 'medium'
    elif escolha_dificuldade == 3:
        dificuldade = medium.copy()
        dificuldade_name = 'hard'
    elif escolha_dificuldade == 4:
        dificuldade = english.copy()
        dificuldade_name = 'english'

    return dificuldade, dificuldade_name

def regras(dificuldade_name):
    if dificuldade_name == 'english':
        sys('cls')
        print(f'\t\tTHE RULES OF HANGMAN:\n')
        print(f'\tA RANDOM WORD WILL BE SELECTED, AND FOR EACTH LETTER WILL BE DRAWN A LINE (_)')
        print(f'\tTHE PLAYER WILL GUESS ONE LETTER AT A TIME, AND IF THIS LETTER IN IN THE WORD IT WILL APPEAR IN POSITION\n\tIF THE PLAYER MISS THE LETTER 1 LIFE WILL BE TAKEN AWAY')
        print(f'\tWHEN ALL 6 LIFES IS LOST THE GAME WILL END')
        print(f'\tIF THE PLAYER GUESS ALL THE LETTERS IN THE WORD, THE NEXT WORD WILL BE SELECTED, AND THE LIFES WILL BE RESET')
        print(f'\n\tYOU CAN GUESS LETTER BY LETTER OR TRY TO GUESS THE WHOLE WORD, IF WRONG, THE SAME AMOUT OF LIFES WILL BE LOST')
        print(f'\tTRY TO CORRECTLY GUESS EVERY WORD IN EVERY LEVEL, AND YOU WILL BE A TRULLY WORD MASTER')
        print('\n\n--->PRESS ANY KEY TO GO BACK TO MAIN MENU<---\n')
        sair = input('--->')

    else:
        sys('cls')
        print(f'\t\tREGRAS DO JOGO DA FORCA:\n')
        print(f'\tUMA PALAVRA ALEATÓRIA VAI SER ESCOLHIDA E PARA CADA LETRA VAI SER DESENHADA UMA LINHA (_)')
        print(f'\tO JOGADOR IRA ADIVINHAR UMA LETRA POR VEZ, E SE CORRETO A LETRA IRÁ APARECER NO LUGAR ADEQUADO\n\tSE O JOGADOR ERRAR A LETRA 1 VIDA SERA PERDIDA')
        print(f'\tQUANDO TODAS AS 6 VIDAS FOREM PERDIDAS O JOGO IRÁ ACABAR')
        print(f'\tSE O JOGADOR ADIVINHAR TODAS AS LETRAS DA PALAVRA, UMA PRÓXIMA PALAVRA SERA ESCOLHIDA, E AS VIDAS SERÃO RESETADAS')
        print(f'\n\tVOCE PODE ADIVINHAR LETRA POR LETRA OU TENTAR ADIVINHAR A PALAVRA INTEIRA, SE ERRAR A MESMA QUANTIDADE DE VIDAS SERÁ PERDIDA')
        print(f'\tTENTE ACERTAR TODAS AS PALAVRAS DE TODOS OS NÍVEIS, E VOCÊ SERÁ UM VERDADEIRO MESTRE DAS PALAVARS')
        print('\n\n--->PRECIONE QULQUER TECLA PARA VOLTAR AO MENU PRINCIPAL<---\n')
        sair = input('--->')
