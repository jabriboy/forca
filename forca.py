from random import choice
from forca_functions import *
from time import sleep
from forca_data_base import *

dificuldade = easy.copy()
dificuldade_name = 'easy'
menu = True
while menu:
    escolha_menu = escolher_menu(dificuldade_name)

    if escolha_menu == 1:
        if dificuldade_name == 'english':  # INGLÊS
            sys('cls')
            nome = input('TYPE YOUR NAME: ').title()
            fase = 0
            palavras = 0
            vidas = 6
            letras_escolhidas = []

            sys('cls')
            print(f'WELCOME TO THE HANGMAN GAME {nome}\nTHINK CAREFULY, IF YOU MESS UP 6 TIMES IT WILL BE GAME OVER!\n')
        else:  # PORTUGÊS
            sys('cls')
            nome = input('DIGITE SEU NOME: ').title()
            fase = 0
            palavras = 0
            vidas = 6
            letras_escolhidas = []

            sys('cls')
            print(f'SEJA MUITO BEM VINDO AO JOGO DA FORCA {nome}\nPENSE COM CUIDADO, PORQUE SE VACILAR 6 VEZES SERÁ GAME OVER!\n')

        jogo = True
        if dificuldade_name == 'english':  # INGLÊS
            while jogo:
                palavra_escolhida = choice(dificuldade)
                dificuldade.remove(palavra_escolhida)
                palavra_escolhida = remover_acentos(palavra_escolhida).lower()
                
                fase += 1
                vidas = 6
                tam_palavra = len(palavra_escolhida)
                escolha_letra = ''
                contador = 0

                continuar = input('\nPRESS ANY KEY TO CONTINUE\n--->')

                sys('cls')
                while True:
                    if len(dificuldade) < 0:
                        print(f'\t\tCONGRATULATIONS, YOU GOT ALL WORD CORRECTLY!')
                        print(f'\n\nTRY A DIFFERENT DIFICULTY YOU HAVE NOT COMPLETED YET')
                        continuar = input('PRESS ANY KEY TO CONTINUE\n--->')
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break

                    if vidas == 0:
                        sys('cls')
                        print(f'GAME OVER\nTHE WORD WAS {palavra_escolhida.upper()}')
                        sleep(1)
                        print(f'GAME OVER\nYOU GOT TO LEVEL: {fase}')
                        continuar = input('PRESS ANY KEY TO CONTINUE\n--->')
                        jogo = False
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break
                    
                    print(f'LIFES: {vidas}\t\tLEVEL: {fase}\t\tDIFICULTY: {dificuldade_name}\n')
                    print(f'letters chosen: {letras_escolhidas}')

                    print('chosen word: ', end='')
                    contador = 0
                    for i in palavra_escolhida:
                        if i in letras_escolhidas:
                            print(i, end=' ')
                            contador += 1
                        else:
                            print('_', end=' ')
                
                    if contador == len(palavra_escolhida):
                        print('\n')
                        sys('cls')
                        print(f'CONGRATULATIONS, YOU GOT IT RIGHT\nTHE WORD WAS {palavra_escolhida.upper()}')
                        letras_escolhidas.clear()
                        break

                    else:
                        print('\n')
                        print('choose letter', end=' ')
                        escolha_letra = input('--->').lower()

                        if escolha_letra == palavra_escolhida:
                            sys('cls')
                            print(f'CONGRATULATIONS, YOU GOT IT RIGHT\nTHE WORD WAS {palavra_escolhida.upper()}')
                            letras_escolhidas.clear()
                            break

                        elif len(escolha_letra) == 1 and escolha_letra not in letras_escolhidas and escolha_letra.isnumeric() == False:
                            letras_escolhidas.append(escolha_letra)
                            sys('cls')
                            if escolha_letra not in palavra_escolhida:
                                sys('cls')
                                print(f'THIS WORD DOES NOT HAVE THE LETTER {escolha_letra}, TRY AGAIN\n{vidas - 1} LIFES LEFT')
                                vidas -= 1
                                sleep(1)
                                sys('cls')
                        elif escolha_letra != palavra_escolhida and len(escolha_letra) == len(palavra_escolhida):
                            sys('cls')
                            print(f'THIS WORD IS NOT {escolha_letra}, TRY AGAIN\n{vidas - 1} LIFES LEFT')
                            vidas -= 1
                            sleep(1)
                            sys('cls')
                        else:
                            sys('cls')
                            print(f'"{escolha_letra}" INVALID INPUT, TRY AGAIN')
        else:  # PORTUGUÊS
            while jogo:
                palavra_escolhida = choice(dificuldade)
                dificuldade.remove(palavra_escolhida)
                palavra_escolhida = remover_acentos(palavra_escolhida).lower()
                
                fase += 1
                vidas = 6
                tam_palavra = len(palavra_escolhida)
                escolha_letra = ''
                contador = 0

                continuar = input('\nPRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->')

                sys('cls')
                while True:
                    if len(dificuldade) < 0:
                        print(f'\t\tPARABÉN, VOCÊ ACERTOU TODAS AS PALAVARS!')
                        print(f'\n\nTENTE UMA DIFICULDADE DIFERENTE QUE VOCE NÃO TENHA COMPLETADO AINDA')
                        continuar = input('PRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->')
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break

                    if vidas == 0:
                        sys('cls')
                        print(f'GAME OVER\nA PALAVRA ERA {palavra_escolhida.upper()}')
                        sleep(1)
                        print(f'GAME OVER\nVOCÊ CHEGOU ATÉ A FASE: {fase}')
                        continuar = input('PRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->')
                        jogo = False
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break
                    
                    print(f'VIDAS: {vidas}\t\tFASE: {fase}\t\tNÍVEL: {dificuldade_name}\n')
                    print(f'letras escolhidas: {letras_escolhidas}')

                    print('palavra escolhida: ', end='')
                    contador = 0
                    for i in palavra_escolhida:
                        if i in letras_escolhidas:
                            print(i, end=' ')
                            contador += 1
                        else:
                            print('_', end=' ')
                
                    if contador == len(palavra_escolhida):
                        print('\n')
                        sys('cls')
                        print(f'PARABÉNS, VOCÊ ACEROU!\nA PALAVRA ERA {palavra_escolhida.upper()}')
                        letras_escolhidas.clear()
                        break

                    else:
                        print('\n')
                        print('escolha letra', end=' ')
                        escolha_letra = input('--->').lower()

                        if escolha_letra == palavra_escolhida:
                            sys('cls')
                            print(f'PARABÉNS, VOCÊ ACEROU!\nA PALAVRA ERA {palavra_escolhida.upper()}')
                            letras_escolhidas.clear()
                            break

                        elif len(escolha_letra) == 1 and escolha_letra not in letras_escolhidas and escolha_letra.isnumeric() == False:
                            letras_escolhidas.append(escolha_letra)
                            sys('cls')
                            if escolha_letra not in palavra_escolhida:
                                sys('cls')
                                print(f'ESSA PALAVRA NÃO POSSUI A LETRA {escolha_letra}, TENTE NOVAMENTE\n{vidas - 1} VIDAS RESTANTES')
                                vidas -= 1
                                sleep(1)
                                sys('cls')
                        elif escolha_letra != palavra_escolhida and len(escolha_letra) == len(palavra_escolhida):
                            sys('cls')
                            print(f'ESSA PALAVRA NÃO É {escolha_letra}, TENTE NOVAMENTE\n{vidas - 1} VIDAS RESTANTES')
                            vidas -= 1
                            sleep(1)
                            sys('cls')
                        else:
                            sys('cls')
                            print(f'"{escolha_letra}" INPUT INVÁLIDO, TENTE NOVAMENTE')

    elif escolha_menu == 2:
        dificuldade, dificuldade_name = escolher_dificuldade(dificuldade, dificuldade_name)

    elif escolha_menu == 3:
        regras(dificuldade_name)

    elif escolha_menu == 4:
        ranking_list = get_all()
        ranking(ranking_list, dificuldade_name)

    elif escolha_menu == 5:
        if dificuldade_name == 'english':  #INGLÊS
            sys('cls')
            print('THANKS TO PLAY!')
            menu = False
            
        else:  # PORTUGÊS
            sys('cls')
            print('OBRIGADO POR JOGAR!')
            menu = False
