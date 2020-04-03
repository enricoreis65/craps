# importando bibliotecas
from random import randint
import time

# fazendo o desenho do dado
base   = '+-------+         +-------+'
sep    = '         '
sem  = '|       |'
esquerda   = '| *     |'
meio = '|   *   |'
direita  = '|     * |'
osdois   = '| *   * |'

dado = [(sem, meio, sem),(esquerda,  sem,  direita),(esquerda,  meio, direita),(osdois,  sem,  osdois ),(osdois,  meio, osdois ),(osdois,  osdois,   osdois )]

# criando uma função para representar o dado
def print_dado(a, b):
    print(base)
    print('\n'.join(a + sep + b for a, b in zip(dado[a-1], dado[b-1])))
    print(base)

# condições iniciais
fichas=100
rodada=("Come Out")

# bem vindo
print('Bem vindo ao jogo Craps!')


# Imprime a qtd de fichas que o jogador tem para apostar no inicio
print("voce tem {0} fichas iniciais".format(fichas))

# Loop principal
while fichas>0:
    if rodada == "Come Out":
        status=input("voce quer jogar?(s/n) ")
    # inicia o jogo se o jogador digitou sim
    if status=="s":
        if rodada=='Come Out':
        # pergunta quanto o jogador quer apostar
            print('saldo atual é {0}'.format(fichas))
            valor_da_aposta=int(input("quanto vc quer apostar? "))
            # valor da aposta tem que ser menor do que as fichas disponíveis
            if valor_da_aposta>fichas:
                print('esta esta muito pobre para fazer essa aposta, ate fiquei ofendido, va embora com as suas {0}'.format(fichas))
                break
            elif valor_da_aposta<=fichas:
                # pergunta que aposta o jogador quer fazer
                tipo_de_aposta =input("voce quer apostar em: Pass Line Bet , Field , Any Craps ou Twelve? ")
                # aposta Pass
        if rodada==("Come Out"):
            if tipo_de_aposta=="Pass":
                # sorteia os dados
                d1=randint(1,6)
                d2=randint(1,6)
                print_dado(d1, d2)
                # armazena o valor da soma dos dados
                soma = d1+d2
                #espera 3 segundos
                time.sleep(3)
                # jogada caso valores dos dados iguais a 7 ou 11
                if soma==7 or soma==11:
                    # ganha o valor que o jogador tiver apostado
                    fichas+=valor_da_aposta
                    print("voce ganhou")
                    # imprime a qtd de fichas restantes
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3)
                # jogada caso valores dos dados iguais a 2,3 ou 12
                if soma==2 or soma==3 or soma==12:
                    # perde o valor que tiver apostado
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    # imprime a qtd de fichas restantes
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)
                #jogada caso soma dos dados para 4,5,6,8,9, ou 10
                if soma==4 or soma==5 or soma==6 or soma==8 or soma==9 or soma==10:
                    # jogador entra em Point
                    print("voce entrou em point")
                    # valor q entrou no point vai ser igual a soma dos dados
                    valor_do_point=soma
                    # espera 2s
                    time.sleep(2)  
                    rodada = "Point"
       

            # aposta Field
            if tipo_de_aposta == "Field":
                # sorteia o numero dos dados
                d1=randint(1,6)
                d2=randint(1,6)
                print_dado(d1, d2)
                # armazena a soma do valor dos dados sorteados
                soma = d1+d2
                # espera 3s
                time.sleep(3)
                # jogada caso valor da soma dos dados for 5,6,7 ou 8 
                if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                    # perde o valor que apostou
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3)
                # jogada caso valor da soma dos dados for 3,4,9,10 ou 11
                elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                    # ganha o valor que apostou
                    fichas += valor_da_aposta
                    print("voce ganhou")
                    # imprime quantas fichas o jogador tem
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3)
                # jogada caso a soma dos dados for 2
                elif soma == 2:
                    # ganha o valor que apostou dobrado 
                    fichas += valor_da_aposta*2
                    print("voce ganhou")
                    # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3) 
                # jogada restante caso não tenham ocorrido nenhum dos eventos anteriores
                else:
                    # ganha o triplo do valor que apostou
                    fichas += valor_da_aposta*3
                    print("voce ganhou")
                    # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3)  


            # aposta Any Craps            
            elif tipo_de_aposta == "Any Craps":
                # sorteia o valor dos dados
                d1=randint(1,6)
                d2=randint(1,6)
                print_dado(d1, d2)
                # armazena o valor da soma dos dados
                soma = d1+d2
                # espera 3s
                time.sleep(3)
                # jogada caso soma dos dados for 2,3 ou 12
                if soma == 2 or soma == 3 or soma == 12:
                    # ganha 7 vezes o que apostou
                    fichas += valor_da_aposta*7
                    print("voce ganhou")
                    # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3) 
                # jogada restante caso não tenham ocorrido nenhum dos eventos anteriores    
                else:
                    # perde o que apostou
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3)  


            # aposta Twelve        
            elif tipo_de_aposta == "Twelve":
                # sorteia valores dos dados                
                d1=randint(1,6)
                d2=randint(1,6)
                print_dado(d1, d2)
                # armazena o valor da soma dos dados
                soma = d1+d2
                # espera 3s
                time.sleep(3)
                # jogada caso o valor da soma dos dados for 12
                if soma == 12:
                    # ganha 30 vezes o valor que apostou
                    fichas += valor_da_aposta*30
                    print("voce ganhou")
                    # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3)
                # jogada restante caso não tenham ocorrido nenhum dos eventos anteriores    
                else:
                    # perde o que apostou
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    # espera 3s
                    time.sleep(3) 
         # Entra no loop do Point
        else:
            tentativa = 1
            while rodada == ("Point"):
                print('Tentativa {0}'.format(tentativa))
                # sorteia os dados
                d1=randint(1,6)
                d2=randint(1,6)
                print_dado(d1, d2)
                # armazenando a soma dos dados
                soma = d1+d2
                # espera 3s
                time.sleep(3)
                print('A soma dos dados foi {0}'.format(soma))
                # testa a soma dos dados se for igual a 7 
                if soma==7:
                    # perde o valor que apostou
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    # Imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    print("entrou em come out")
                    rodada=("Come Out")
                    # espera 3s
                    time.sleep(3)
                # jogada caso a soma for igual o valor q entrou no point
                elif soma==valor_do_point:
                    # ganha o valor que apostou
                    fichas+=valor_da_aposta
                    print("voce ganhou")
                # imprime a qtd de fichas
                    print("voce tem {0} fichas".format(fichas))
                    print("entrou em come out")
                    rodada=("Come Out")
                    # espera 3s
                    time.sleep(3)
                # jogada caso a soma for diferente de 7 e for diferente do que jogador apostou
                else:
                    tentativa += 1
                    prox_tentativa = input("Não aconteceu nada, (aperte enter p/ a prox tentativa) ")
                   
                    
                
    # caso o jogador digite que não quer mais jogar
    else:
        # imprime o numero final de fichas
        print("voce terminou com {0} fichas".format(fichas))
        fichas-=fichas

