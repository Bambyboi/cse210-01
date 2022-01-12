#Tic-tac-toe..................................................................................


Board_numbers = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []


for key in Board_numbers:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(Board_numbers)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if Board_numbers[move] == ' ':
            Board_numbers[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if Board_numbers['7'] == Board_numbers['8'] == Board_numbers['9'] != ' ': # across the top
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif Board_numbers['4'] == Board_numbers['5'] == Board_numbers['6'] != ' ': # across the middle
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board_numbers['1'] == Board_numbers['2'] == Board_numbers['3'] != ' ': # across the bottom
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board_numbers['1'] == Board_numbers['4'] == Board_numbers['7'] != ' ': # down the left side
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board_numbers['2'] == Board_numbers['5'] == Board_numbers['8'] != ' ': # down the middle
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board_numbers['3'] == Board_numbers['6'] == Board_numbers['9'] != ' ': # down the right side
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif Board_numbers['7'] == Board_numbers['5'] == Board_numbers['3'] != ' ': # diagonal
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board_numbers['1'] == Board_numbers['5'] == Board_numbers['9'] != ' ': # diagonal
                printBoard(Board_numbers)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie game!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Play Again?(yes or no)")
    if restart == "yes" or restart == "no":  
        for key in board_keys:
            Board_numbers[key] = " "

        game()

if __name__ == "__main__":
    game()
