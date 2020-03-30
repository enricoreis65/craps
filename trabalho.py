from random import randint

fichas=100
rodada="Come_Out"


while fichas>0:
    status=input("voce quer jogar? ")
    if status=="s":
       if rodada=="Come_Out":
           tipo_de_aposta=input("voce quer apostar em: Pass Line Bet , Field , Any Craps ou Twelve?")

           if tipo_de_aposta=="Pass":
               valor_da_aposta=int(input("quanto vc quer apostar? ")
               d1=randint(1,6)
               d2=randint(1,6)
                if d1+d2==7 or d1+d2==11:
                   fichas+=valor_da_aposta
                if d1+d2==2 or d1+d2==3 or d1+d2==12:
                    fichas-=valor_da_aposta
                if d1+d2==4 or d1+d2==5 or d1+d2==6 or d1+d2==8 or d1+d2==9 or d1+d2==10:
                    rodada="Point"



    else:
        
        fichas-=fichas






