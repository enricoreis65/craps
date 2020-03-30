from random import randint

fichas=100
rodada="Come_Out"


while fichas>0:
    status=input("voce quer jogar? ")
    if status=="s":
       if rodada=="Come_Out":
            tipo_de_aposta=input("voce quer apostar em: Pass Line Bet , Field , Any Craps ou Twelve?")
            if tipo_de_aposta=="Pass":
                valor_da_aposta=int(input("quanto vc quer apostar? "))
                d1=randint(1,6)
                d2=randint(1,6)
                soma = d1+d2
                if soma==7 or soma==11:
                    fichas+=valor_da_aposta
                    print(fichas)
                if soma==2 or soma==3 or soma==12:
                    fichas-=valor_da_aposta
                    print(fichas)
                if soma==4 or soma==5 or soma==6 or soma==8 or soma==9 or soma==10:
                    rodada="Point"
                    ptint("voce entrou em point")
                    valor_do_point=soma
                    
            if tipo_de_aposta == "Field":
                valor_da_aposta=int(input("quanto vc quer apostar? "))
                d1=randint(1,6)
                d2=randint(1,6)
                soma = d1+d2
                if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                    valor_da_aposta = 0
                elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                    fichas += valor_da_aposta
                elif soma == 2:
                    fichas += valor_da_aposta*2
                else:
                    fichas += valor_da_aposta*3 
                    
            if tipo_de_aposta == "Any Craps":
                valor_da_aposta=int(input("quanto vc quer apostar? "))
                d1=randint(1,6)
                d2=randint(1,6)
                soma = d1+d2
                if soma == 2 or soma == 3 or soma == 12:
                    fichas += valor_da_aposta*7
                else:
                    valor_da_aposta = 0
                
            if tipo_de_aposta == "Twelve":
                valor_da_aposta=int(input("quanto vc quer apostar? "))
                d1=randint(1,6)
                d2=randint(1,6)
                soma = d1+d2
                if soma == 12:
                    fichas += valor_da_aposta*30
                else:
                    valor_da_aposta = 0


    else:
        
        fichas-=fichas






