from random import randrange

def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    print("+-------+-------+-------+")
    for fila in board.keys():
        print("|       |       |       |")
        for columna in board[fila]:
            print("|  ",columna,"  ",end="")
        print("|")
        print("|       |       |       |")
        print("+-------+-------+-------+")


    
def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    entrada = int(input("Ingresa tu movimiento: "))
    if entrada < 0 or entrada > 10:
        print("entrada invalida")
    else:
        for fila in board.keys():
            for i in range(3):
                if board[fila][i] == entrada:
                    board[fila][i] = "O"
                    break
    DisplayBoard(board)
    if VictoryFor(board, "O"):
        print("¡Has Ganado!")
        return "Win"

                

def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    board = {
        1:[1,2,3],
        2:[4,"X",6],
        3:[7,8,9]
    }
    return board


def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    #por fila
    for fila in board.keys():
        count = 0
        for i in range(3):
            if board[fila][i] == sign:
                count +=1
        if count == 3:
            print("por fila")
            return True
            
    #por columna 1
    count = 0   
    for fila in board.keys():    
        if board[fila][0] == sign:
            count +=1
    if count == 3:
        print("por columna 1")
        return True
    
    #por columna 2
    count = 0   
    for fila in board.keys():    
        if board[fila][1] == sign:
            count +=1
    if count == 3:
        print("por columna 2")
        return True
        
    #por columna 3
    count = 0   
    for fila in board.keys():    
        if board[fila][2] == sign:
            count +=1
    if count == 3:
        print("por columna 3")
        return True
        
    #por diagonal 1
    count = 0   
    if board[1][0] == sign:
        count +=1
    if board[2][1] == sign:
        count +=1
    if board[3][2] == sign:
        count +=1
    if count == 3:
        print("por diagonal 1")
        return True
    
    #por diagonal 2
    count = 0   
    if board[1][2] == sign:
        count +=1
    if board[2][1] == sign:
        count +=1
    if board[3][0] == sign:
        count +=1
    if count == 3:
        print("por diagonal 2")
        return True
        


def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    entro = False
    while entro == False:
        entrada = randrange(9)+1
        print("turno de la maquina :", entrada)
        for fila in board.keys():
            for i in range(3):
                if board[fila][i] == entrada:
                    entro = True
                    board[fila][i] = "X"
                    break
    DisplayBoard(board)
    if VictoryFor(board, "X"):
        print("¡Ha ganado la maquina!")
        return "Win"



board = MakeListOfFreeFields({})
DisplayBoard(board)
while True:
    if EnterMove(board) == "Win":
        break
    if DrawMove(board) == "Win":
        break