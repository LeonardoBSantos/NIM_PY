def computador_escolhe_jogada(n,m):#
        m1 = m
        while (n-m1)%(m+1)!=0:
                m1 = m1-1
        if m1<=0:
                m1 = m
        print("O computador tirou ",m1,"peças.")        
        return  m1 

def usuario_escolhe_jogada(n,m):
        j = int(input("Quantas peças você vai tirar ?\n"))
        if j< 1 or j>m:
                while (j<1 or j>m):
                    j = int(input("Informe uma jogada válida! ="))
        print("Você tirou",j,"peças")
        return j

def partida():
    a = 0
    e = 0
    
# ********************************** Partida *********************************
    print("você escolheu uma partida!\n") 
    n = int(input("Quantas peças ?"))
    m = int(input("Limite de peças por jogada ?\n"))
    if (n < m):
        while (n < m):
            print (" n é menor que m")
            n = int(input("Informe uma jogada válida para n = "))
            m = int(input("Informe uma jogada válida para m = "))     
    if n%(m+1)==0:  # Testa se n é multiplo de m+1
        print("Você começa\n")
        while (n!=0):
            a = usuario_escolhe_jogada(n,m)
            n = n-a
            print("Agora resta apenas",n,"peças no tabuleiro\n")
            a = computador_escolhe_jogada(n,m)
            n = n-a
            if (n!=0):
                print("Agora resta apenas",n,"peças no tabuleiro\n")
            else:
                print("Fim de jogo! O computador ganhou!")
    else:
        print("computador começa\n")
        while (n!=0):
            a = computador_escolhe_jogada(n,m)
            n = n-a
            if (n!=0):
                print("Agora resta apenas",n,"peças no tabuleiro\n")
            else:
                print("Fim de jogo! O computador ganhou!")
            if (n!=0):
                a = usuario_escolhe_jogada(n,m)
                n = n-a
                print("Agora resta apenas",n,"peças no tabuleiro\n")

 # ********************** campeonato ***************************************
def campeonato ():
     print("você escolheu um campeonato!\n")
     print ("********** Rodada 1 **********")
     partida()
     print ("********** Rodada 2 **********")
     partida()
     print ("********** Rodada 3 **********")
     partida()
    




def main():
    print("Bem vindo ao jogo NIM! escolha:\n")
    print("1 - para jogar uma partida isolada")
    e = int(input("2 - para um campeonato\n"))
    placar = 0
    if (e==1):
        partida()
        placar = 1
    else:
       campeonato()
       placar = 2
        
# ****************************** Final **************************************
    if(placar == 2):    
        print("******** Final de campeonato **********")
        print ("Placar: Você 0 x 3 Computador")

main()


