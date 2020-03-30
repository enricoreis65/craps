dinheiro_final=0
fichas=100
rodada="Come_Out"

while fichas>0:
    status=input("voce quer jogar? ")
    if status=="s":
       if rodada=="Come_Out":
           tipo_de_aposta=input("voce quer apostar em: Pass Line Bet , Field , Any Craps ou Twelve?)

    else:
        dinheiro_final=fichas
        fichas-=fichas
print(dinheiro_final)






