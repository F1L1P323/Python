# Fazer um jogo da velha para dois jogadores

# Importando bibliotecas
import random

# Função para imprimir o tabuleiro
def imprimeTabuleiro(tabuleiro):
    print(' ' + tabuleiro[1] + ' | ' + tabuleiro[2] + ' | ' + tabuleiro[3])
    print('-----------')
    print(' ' + tabuleiro[4] + ' | ' + tabuleiro[5] + ' | ' + tabuleiro[6])
    print('-----------')
    print(' ' + tabuleiro[7] + ' | ' + tabuleiro[8] + ' | ' + tabuleiro[9])


# Função para escolher o símbolo do jogador
def escolheSimbolo():
    simbolo = ''
    while not (simbolo == 'X' or simbolo == 'O'):
        print('Você quer ser X ou O?')
        simbolo = input().upper()
    if simbolo == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    

# Função para escolher quem começa
def quemComeca():
    if random.randint(0, 1) == 0:
        return 'Computador'
    else:
        return 'Jogador'
    

# Função para verificar se a posição está livre
def verificaPosicao(tabuleiro, posicao):
    return tabuleiro[posicao] == ' '

# Função para verificar se o tabuleiro está cheio
def verificaTabuleiroCheio(tabuleiro):
    for i in range(1, 10):
        if verificaPosicao(tabuleiro, i):
            return False
    return True

# Função para verificar se o jogador ganhou

def verificaGanhador(tabuleiro, simbolo):


    return ((tabuleiro[7] == simbolo and tabuleiro[8] == simbolo and tabuleiro[9] == simbolo) or # linha de cima
    (tabuleiro[4] == simbolo and tabuleiro[5] == simbolo and tabuleiro[6] == simbolo) or # linha do meio
    (tabuleiro[1] == simbolo and tabuleiro[2] == simbolo and tabuleiro[3] == simbolo) or # linha de baixo
    (tabuleiro[7] == simbolo and tabuleiro[4] == simbolo and tabuleiro[1] == simbolo) or # coluna da esquerda
    (tabuleiro[8] == simbolo and tabuleiro[5] == simbolo and tabuleiro[2] == simbolo) or # coluna do meio
    (tabuleiro[9] == simbolo and tabuleiro[6] == simbolo and tabuleiro[3] == simbolo) or # coluna da direita
    (tabuleiro[7] == simbolo and tabuleiro[5] == simbolo and tabuleiro[3] == simbolo) or # diagonal
    (tabuleiro[9] == simbolo and tabuleiro[5] == simbolo and tabuleiro[1] == simbolo)) # diagonal

# Função para fazer a jogada do jogador
def fazJogada(tabuleiro, simbolo, posicao):
    tabuleiro[posicao] = simbolo


# Função para escolher uma posição aleatória
def escolhePosicaoAleatoria(tabuleiro, listaPosicoes):
    possiveisJogadas = []
    for i in listaPosicoes:
        if verificaPosicao(tabuleiro, i):
            possiveisJogadas.append(i)
    if len(possiveisJogadas) != 0:
        return random.choice(possiveisJogadas)
    else:
        return None
    

# Função para fazer a jogada do computador
def fazJogadaComputador(tabuleiro, simboloComputador):
    if simboloComputador == 'X':
        simboloJogador = 'O'
    else:
        simboloJogador = 'X'
    
    # Verifica se o computador pode ganhar na próxima jogada
    for i in range(1, 10):
        copiaTabuleiro = tabuleiro[:]
        if verificaPosicao(copiaTabuleiro, i):
            fazJogada(copiaTabuleiro, simboloComputador, i)
            if verificaGanhador(copiaTabuleiro, simboloComputador):
                return i
    
    # Verifica se o jogador pode ganhar na próxima jogada e bloqueia
    for i in range(1, 10):
        copiaTabuleiro = tabuleiro[:]
        if verificaPosicao(copiaTabuleiro, i):
            fazJogada(copiaTabuleiro, simboloJogador, i)
            if verificaGanhador(copiaTabuleiro, simboloJogador):
                return i
    
    # Tenta ocupar um dos cantos
    posicao = escolhePosicaoAleatoria(tabuleiro, [1, 3, 7, 9])
    if posicao != None:
        return posicao
    
    # Tenta ocupar o centro
    if verificaPosicao(tabuleiro, 5):
        return 5
    
    # Ocupa um dos lados
    return escolhePosicaoAleatoria(tabuleiro, [2, 4, 6, 8])


# Função para verificar se o jogador quer jogar novamente
def jogarNovamente():
    print('Você quer jogar novamente? (sim ou não)')
    return input().lower().startswith('s')


# Função principal

print('Jogo da Velha')

while True:


    # Reseta o tabuleiro
    tabuleiro = [' '] * 10
    simboloJogador, simboloComputador = escolheSimbolo()
    turno = quemComeca()
    print('O ' + turno + ' começa.')
    jogoEmAndamento = True

    while jogoEmAndamento:
        if turno == 'Jogador':
            # Vez do jogador
            imprimeTabuleiro(tabuleiro)
            posicao = int(input("Insira uma posição:" ))
            while not verificaPosicao(tabuleiro, posicao):
                print('Qual é a sua jogada? (1-9)')
                posicao = int(input())
            fazJogada(tabuleiro, simboloJogador, posicao)

            if verificaGanhador(tabuleiro, simboloJogador):
                imprimeTabuleiro(tabuleiro)
                print('Você ganhou!')
                jogoEmAndamento = False
            else:
                if verificaTabuleiroCheio(tabuleiro):
                    imprimeTabuleiro(tabuleiro)
                    print('Deu velha!')
                    break
                else:
                    turno = 'Computador'

        else:
            # Vez do computador
            posicao = fazJogadaComputador(tabuleiro, simboloComputador)
            fazJogada(tabuleiro, simboloComputador, posicao)

            if verificaGanhador(tabuleiro, simboloComputador):
                imprimeTabuleiro(tabuleiro)
                print('O computador ganhou!')
                jogoEmAndamento = False
            else:
                if verificaTabuleiroCheio(tabuleiro):
                    imprimeTabuleiro(tabuleiro)
                    print('Deu velha!')
                    break
                else:
                    turno = 'Jogador'

    if not jogarNovamente():
        break






