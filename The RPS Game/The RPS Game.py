import random, sys

print ('Rock, Paper, Scissors')

#These variables keep track of the number of wins, loses, and ties

wins = 0 
losses = 0
ties = 0

while True:
    print('%s Wins, %s losses, %s Ties' % (wins, losses, ties))
    while True: #The player input loop
     print('Enter your move : (R)ock (P)aper (S)cissors or (Q)uit')
     player_move = input ('>')
     if player_move == 'q':
         sys.exit() #To quit the programme
     if player_move == 'r' or player_move == 'p' or player_move == 's':
        break #Break out of the player input loop
     print ('type one of r, p, s, or q')
    #Display what the player choose
    if player_move == 'r' :
        print('Rock versus...')
    elif player_move == 'p' :
        print('Paper versus...')
    elif player_move == 's':
        print('Scissors versus...')
        
        #Display what the cumputer choose
    move_number = random.randint(1,3)
    if move_number == 1 :
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2 :
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3 :
        computer_move = 's'
        print('SCISSORS')
        
    #display and record the win/loss/tie:
    
    if player_move == computer_move:
        print('It is a tie !')
        ties = ties + 1 
    elif player_move == 'r' and computer_move == 's':
        print('You win !')
        wins = wins + 1 
    elif player_move == 'p' and computer_move == 'r' :
        print('You win !')
        wins = wins + 1 
    elif player_move == 's' and computer_move == 'p':
        print('You win !')
        wins = wins + 1 
    elif player_move == 'r' and computer_move == 'p':
        print ('You lose !')
        losses = losses + 1 
    elif player_move == 'p' and computer_move == 's' :
        print('You loose !')
        losses = losses + 1 
    elif player_move == 's' and computer_move == 'r' :
        print ('You loose !')
        losses = losses + 1 
        
