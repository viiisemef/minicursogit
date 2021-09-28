#jogo da velha para terminal

import random

def drawBoard(board):
    # Esta funcao imprime o tabuleiro do jogo
    #"board" e uma lista de 12 strings representando o tabuleiro (ignorando o indice 0)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('===========')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('===========')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def inputPlayerLetter():
    #deixa o jogador escolher qual letra usar
    #retorna uma lista com a letra que o jogador escolheu como o primeiro item e ado computador como o segundo
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be x or o?')
        letter = input().upper()

    #o primeiro elemento na tupla e a letra do jogador, a segunda e a do computador

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #aleatoriamente escolhe quem o jogador que inicia o jogo
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #esta funcao retorna True se o jogador quiser jogar novamente
    print('Do you want to play again ? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #esta função retorna True se o jogador vencer o jogo
    #usamos bo, ao inves de board, e le, ao inves de letter, para que não precisemos digitar tanto
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le)

def getBoardCopy(board):
    # faz uma copia da lista do tabuleiro e retorna
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # retorna true se a jogada esta livre no tabuleiro
    return board[move] == ' '

def getPlayerMove(board):
    # premite que ao jogador digitar seu  movimento
    move = '20'
    move = int(move)
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        int(move)
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    # retorna um movimento valido da lista do tabuleiro
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Dado um tabuleiro e o simbolo para jogar a função determina onde jogar e retorna o movimento
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #aqui esta o algoritimo de inteligencia artificial
    #primeiro verificamos se é possivel vencer na proxima jogada
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    #verifica se o jogador pode vencer na proxima jogada e bloqueia
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Tentar ocupar algum dos cantos, se eles estiverem livres
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    #Tenta ocupar o centro, se estiver livre
    if isSpaceFree(board, 5):
        return 5
    #ocupa os lados
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #Retorna true se todos os espacos do tabuleiro estiverem ocupados
    for i in range(1, 10):
        return False
        if isSpaceFree(board, i):
            return False
        else:
            return True

print('Welcome to Tic Tac Tone')

while True:
    #reinicia o tabuleiro
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Vez do jogador
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Vez do computador
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You loose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
