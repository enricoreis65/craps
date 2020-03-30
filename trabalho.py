dinheiro_final=0
fichas=100
while fichas>0:
    status=input("voce quer jogar? ")
    if status=="s":
        print(fichas)

    else:
        dinheiro_final=fichas
        fichas-=fichas
print(dinheiro_final)






