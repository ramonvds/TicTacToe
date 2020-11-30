import os
import random
import numpy as np

jogadas = 0
turno = 2  # 1=Computador, 2=Jogador
block = 0
l = int(input("Informe a quantidade de linhas do tabuleiro: "))
c = int(input("Informe a quantidade de colunas do tabuleiro: "))
tabuleiro = np.full((l, c), " ")
vetorPontoX = []
vetorPontoO = []

while block < 2:
    print("Bloquear casa " + str(block))
    l = int(input("Informe a linha do tabuleiro: "))
    c = int(input("Informe a coluna do tabuleiro: "))
    tabuleiro[l][c] = "#"
    block += 1


def tela():
    global tabuleiro
    global jogadas
    print("-------------------------")
    print("Placar: X-" + str(len(vetorPontoX)) + " O-" + str(len(vetorPontoO)))
    print(tabuleiro)
    print(f"Jogadas: {str(jogadas)} \n")
    print("-------------------------")


def turnoJogador():

    # global jogadas
    # global turno
    # if turno==2:
    #     try:
    #         l=int(input("Linha  : "))
    #         c=int(input("Coluna : "))
    #         while tabuleiro[l][c]!=" ":
    #             l=int(input("Linha  : "))
    #             c=int(input("Coluna : "))
    #         tabuleiro[l][c]="X"
    #         turno=1
    #         jogadas+=1
    #     except:
    #         print("Jogada inválida")
    #         os.system('pause')
  
    global tabuleiro
    tabuleiro_linha, tabuleiro_coluna = tabuleiro.shape
    global jogadas
    global turno
    if turno == 2:
        l = random.randrange(0, tabuleiro_linha)
        c = random.randrange(0, tabuleiro_coluna)
        while tabuleiro[l][c] != " ":
            l = random.randrange(0, tabuleiro_linha)
            c = random.randrange(0, tabuleiro_coluna)
        tabuleiro[l][c] = "X"
        jogadas += 1
        turno = 1


def turnoComputador():
    global tabuleiro
    tabuleiro_linha, tabuleiro_coluna = tabuleiro.shape
    global jogadas
    global turno
    if turno == 1:
        l = random.randrange(0, tabuleiro_linha)
        c = random.randrange(0, tabuleiro_coluna)
        while tabuleiro[l][c] != " ":
            l = random.randrange(0, tabuleiro_linha)
            c = random.randrange(0, tabuleiro_coluna)
        tabuleiro[l][c] = "O"
        jogadas += 1
        turno = 2


def verificaLinha(jogador):
    global tabuleiro
    global vetorPontoX
    global vetorPontoO
    tabuleiro_linha, tabuleiro_coluna = tabuleiro.shape
    indiceLinha = 0
    vetorPontuacao = []

    while indiceLinha < tabuleiro_linha:
        indiceColuna = 0
        vetorPontuacao.clear()
        while indiceColuna < tabuleiro_coluna:
            eh_x_ou_o = tabuleiro[indiceLinha][indiceColuna]
            jogador_eh_igual = eh_x_ou_o == jogador
            # print(f'[{indiceLinha}][{indiceColuna}]: {eh_x_ou_o} - {jogador}')
            if jogador_eh_igual:
                vetorPontuacao.append(str(indiceLinha) + str(indiceColuna))
                if len(vetorPontuacao) >= 3:
                  print(f"Deve ganhar ponto Linha: {len(vetorPontuacao)} {vetorPontuacao}")
                  break
            elif not jogador_eh_igual or len(vetorPontuacao) < 3:
                # print(f'limpou o vetor len(vetorPontuacao): {len(vetorPontuacao)}, [{indiceLinha}][{indiceColuna}]')
                vetorPontuacao.clear()
            indiceColuna += 1
        
        if len(vetorPontuacao)>=3:
          print(f"jogador deve ganhar pontuacao {len(vetorPontuacao)}")

        if (len(vetorPontuacao) > 3):
            if (jogador == "X"):
                if (comparaVetor(vetorPontoX, vetorPontuacao) == False):
                    vetorPontoX.append(list(vetorPontuacao))
                    vetorPontoX.append(list(vetorPontuacao))
                    print("Jogador X - 2pt LINHA")
            if (jogador == "O"):
                if (comparaVetor(vetorPontoO, vetorPontuacao) == False):
                    vetorPontoO.append(list(vetorPontuacao))
                    vetorPontoO.append(list(vetorPontuacao))
                    print("Jogador O - 2pt LINHA")

        if (len(vetorPontuacao) == 3):
            if (jogador == "X"):
                if (comparaVetor(vetorPontoX, vetorPontuacao) == False):
                    vetorPontoX.append(list(vetorPontuacao))
                    print("Jogador X - 1pt LINHA")
            if (jogador == "O"):
                if (comparaVetor(vetorPontoO, vetorPontuacao) == False):
                    vetorPontoO.append(list(vetorPontuacao))
                    print("Jogador O - 1pt LINHA")
        indiceLinha += 1


def verificaColuna(jogador):
    global tabuleiro
    global vetorPontoX
    global vetorPontoO
    tabuleiro_linha, tabuleiro_coluna = tabuleiro.shape
    indiceColuna = 0
    vetorPontuacao = []

    while indiceColuna < tabuleiro_coluna:
        indiceLinha = 0
        vetorPontuacao.clear()
        while indiceLinha < tabuleiro_linha:
            if (tabuleiro[indiceLinha][indiceColuna] == jogador):
                vetorPontuacao.append(str(indiceLinha) + str(indiceColuna))
                if len(vetorPontuacao) >= 3:
                  print(f"Deve ganhar ponto Coluna: {len(vetorPontuacao)} {vetorPontuacao}")
                  break
            elif tabuleiro[indiceLinha][indiceColuna] != jogador or len(vetorPontuacao) < 3:
                vetorPontuacao.clear()

            indiceLinha += 1

        if (len(vetorPontuacao) > 3):
            if (jogador == "X"):
                if (comparaVetor(vetorPontoX, vetorPontuacao) == False):
                    vetorPontoX.append(list(vetorPontuacao))
                    vetorPontoX.append(list(vetorPontuacao))
                    print("Jogador X - 2pt COLUNA")
            if (jogador == "O"):
                if (comparaVetor(vetorPontoO, vetorPontuacao) == False):
                    vetorPontoO.append(list(vetorPontuacao))
                    vetorPontoO.append(list(vetorPontuacao))
                    print("Jogador O - 2pt COLUNA")

        if (len(vetorPontuacao) == 3):
            if (jogador == "X"):
                if (comparaVetor(vetorPontoX, vetorPontuacao) == False):
                    vetorPontoX.append(list(vetorPontuacao))
                    print("Jogador X - 1pt COLUNA")
            if (jogador == "O"):
                if (comparaVetor(vetorPontoO, vetorPontuacao) == False):
                    vetorPontoO.append(list(vetorPontuacao))
                    print("Jogador O - 1pt COLUNA")
        indiceColuna += 1


def comparaVetor(vetorPai, vetorFilho):
    for x in vetorPai:
        if x == vetorFilho:
            return True
    return False


def verificaVencedor():
    global vetorPontoX
    global vetorPontoO
    if len(vetorPontoX) >= 2 or len(vetorPontoO) >= 2:
      tela()
      return True


while True:
    tela()
    turnoJogador()
    verificaLinha("X")
    verificaColuna("X")
    if verificaVencedor():
        break
    turnoComputador()
    verificaLinha("O")
    verificaColuna("O")
    if verificaVencedor():
        break