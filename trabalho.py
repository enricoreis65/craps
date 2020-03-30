from random import randint

fichas=100
rodada=("Come Out")

print(fichas)
while fichas>0:
    status=input("voce quer jogar? ")
    if status=="s":       
        tipo_de_aposta=input("voce quer apostar em: Pass Line Bet , Field , Any Craps ou Twelve?")
        valor_da_aposta=int(input("quanto vc quer apostar? "))
        if tipo_de_aposta=="Pass":
            if rodada==("Come Out"):                
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
                    print("voce entrou em point")
                    valor_do_point=soma
                    rodada=("Point")  
            if rodada== ("Point"):
                d1=randint(1,6)
                d2=randint(1,6)
                soma = d1+d2
                if soma==7:
                    fichas-=valor_da_aposta
                    rodada=("Come Out")
                    print("voce perdeu")
                    print(fichas)
                    print("entrou em come out")
                if soma==valor_do_point:
                    fichas+=valor_da_aposta
                    rodada=("Come Out")
                    print("voce ganhou")
                    print(fichas)
                    print("entrou em come out")
                elif soma !=7 and soma!=valor_da_aposta:
                    print("naos aconteceu nada")               
        if tipo_de_aposta == "Field":    
            d1=randint(1,6)
            d2=randint(1,6)
            soma = d1+d2
            if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                fichas-=valor_da_aposta
                print(fichas)
            elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                fichas += valor_da_aposta
                print(fichas)
            elif soma == 2:
                fichas += valor_da_aposta*2
                print(fichas)
            else:
                fichas += valor_da_aposta*3
                print(fichas)
                    
            if tipo_de_aposta == "Any Craps":               
                d1=randint(1,6)
                d2=randint(1,6)
                soma = d1+d2
                if soma == 2 or soma == 3 or soma == 12:
                    fichas += valor_da_aposta*7
                    print(fichas)
                else:
                    fichas-=valor_da_aposta
                    print(fichas)  
                
            if tipo_de_aposta == "Twelve":                
                d1=randint(1,6)
                d2=randint(1,6)
                soma = d1+d2
                if soma == 12:
                    fichas += valor_da_aposta*30
                    print(fichas)
                else:
                    fichas-=valor_da_aposta
                    print(fichas)  

        
    elif status!="s":
        print(fichas)
        fichas-=fichas






