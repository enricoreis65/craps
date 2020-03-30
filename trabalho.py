from random import randint
import time
base   = '+-------+         +-------+'
sep    = '         '
sem  = '|       |'
esquerda   = '| *     |'
meio = '|   *   |'
direita  = '|     * |'
osdois   = '| *   * |'

dice = [(sem, meio, sem),(esquerda,  sem,  direita),(esquerda,  meio, direita),(osdois,  sem,  osdois ),(osdois,  meio, osdois ),(osdois,  osdois,   osdois )]

def print_dice(a, b):
    print(base)
    print('\n'.join(a + sep + b for a, b in zip(dice[a-1], dice[b-1])))
    print(base)

fichas=100
rodada=("Come Out")

print("voce tem {0} fichas iniciais".format(fichas))
while fichas>0:
    status=input("voce quer jogar? ")
    if status=="s":       
        valor_da_aposta=int(input("quanto vc quer apostar? "))
        if valor_da_aposta<=fichas:
            tipo_de_aposta=input("voce quer apostar em: Pass Line Bet , Field , Any Craps ou Twelve?")
            if tipo_de_aposta=="Pass":
                if rodada==("Come Out"):                
                    d1=randint(1,6)
                    d2=randint(1,6)
                    print_dice(d1, d2)
                    soma = d1+d2
                    time.sleep(3)  
                    if soma==7 or soma==11:
                        fichas+=valor_da_aposta
                        print("voce ganhou")
                        print("voce tem {0} fichas".format(fichas))
                        time.sleep(3)
                    if soma==2 or soma==3 or soma==12:
                        fichas-=valor_da_aposta
                        print("voce perdeu")
                        print("voce tem {0} fichas".format(fichas))
                        time.sleep(3)
                    if soma==4 or soma==5 or soma==6 or soma==8 or soma==9 or soma==10:
                        print("voce entrou em point")
                        valor_do_point=soma
                        time.sleep(2)  
                        rodada=("Point")
                if rodada== ("Point"):
                    d1=randint(1,6)
                    d2=randint(1,6)
                    print_dice(d1, d2)
                    soma = d1+d2
                    time.sleep(3)  
                    if soma==7:
                        fichas-=valor_da_aposta
                        rodada=("Come Out")
                        print("voce perdeu")
                        print("voce tem {0} fichas".format(fichas))
                        print("entrou em come out")
                        time.sleep(3)  
                    if soma==valor_do_point:
                        fichas+=valor_da_aposta
                        rodada=("Come Out")
                        print("voce ganhou")
                        print("voce tem {0} fichas".format(fichas))
                        print("entrou em come out")
                        time.sleep(3)  
                    elif soma !=7 and soma!=valor_da_aposta:
                        print("naos aconteceu nada")  
                        time.sleep(3)               
            if tipo_de_aposta == "Field":    
                d1=randint(1,6)
                d2=randint(1,6)
                print_dice(d1, d2)
                soma = d1+d2
                time.sleep(3)  
                if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)  
                elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                    fichas += valor_da_aposta
                    print("voce ganhou")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)  
                elif soma == 2:
                    fichas += valor_da_aposta*2
                    print("voce ganhou")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)  
                else:
                    fichas += valor_da_aposta*3
                    print("voce ganhou")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)  
                        
            if tipo_de_aposta == "Any Craps":               
                d1=randint(1,6)
                d2=randint(1,6)
                print_dice(d1, d2)
                soma = d1+d2
                time.sleep(3)  
                if soma == 2 or soma == 3 or soma == 12:
                    fichas += valor_da_aposta*7
                    print("voce ganhou")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)  
                else:
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)   
                    
            if tipo_de_aposta == "Twelve":                
                d1=randint(1,6)
                d2=randint(1,6)
                print_dice(d1, d2)
                soma = d1+d2
                time.sleep(3)  
                if soma == 12:
                    fichas += valor_da_aposta*30
                    print("voce ganhou")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)  
                else:
                    fichas-=valor_da_aposta
                    print("voce perdeu")
                    print("voce tem {0} fichas".format(fichas))
                    time.sleep(3)    
        else:
            print("voce so tem {0} fichas para apostar".format(fichas))
            time.sleep(3)  
            

        
    elif status!="s":
        print("voce terminou com {0} fichas".format(fichas))
        fichas-=fichas






