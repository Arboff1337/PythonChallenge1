#variables

player1score = 0
player2score = 0


def game():

    player1 = int(input('player one number: '))
    player2 = int(input('\nplayer two number: '))
    
    
    
    
    print("Player one choose: "+ str(player1) + "\nPlayer two choose: " + str(player2))
    
    if int(player1) > int(player2):
        global player1score
        player1score += 1
    elif int(player1) < int(player2):
        global player2score
        player2score += 1
    elif int(player1) == int(player2):
        print("Numbers are equal, no score added")
    else:
        print("something went wrong.")
        
        
    print("Player1 score is: " + str(player1score) + "\nPlayer2 score is: " + str(player2score))
    
    
    if player1score == 5:
        print("Player One won with 5pts!")
        input("Press any key to restart the game...")
        global player1score
        global player2score
        player1score = 0
        player2score = 0
        game()
    elif player2score == 5:
        print("Player Two won with 5pts!")
        input("Press any key to restart the game...")
        global player1score
        global player2score
        player1score = 0
        player2score = 0
        game()
    else:
        game()

game()
    
