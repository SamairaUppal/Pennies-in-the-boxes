print('Enter the number of boxes:')
n = int(input())
print('Enter pennies in each box:')
things = input().split(' ')
pennies= []
for i in things:
    penny = int(i)
    pennies.append(penny)
cur_player = 1
player1_score = 0
player2_score = 0
while True:
    print()
    print('Boxes:')
    for i in pennies:
        print(i, end = ' ')
    print()
    print('Player 1 score:',player1_score)
    print('Player 2 score:',player2_score)
    print('Enter player',cur_player,'move (1 for leftmost,2 for rightmost):')
    move = int(input())
    if move == 1:
        if cur_player == 1:
            player1_score +=pennies[0]
        elif cur_player == 2:
            player2_score +=pennies[0]
        pennies.pop(0)
        cur_player = 3-cur_player
    elif move == 2:
        if cur_player == 1:
            player1_score +=pennies[len(pennies)-1]
        elif cur_player == 2:
            player2_score +=pennies[len(pennies)-1]
        pennies.pop()
        cur_player = 3-cur_player
    else:
        print('Invalid move!')
        continue
    if pennies == []:
        print('Player 1 score:',player1_score)
        print('Player 2 score:',player2_score)
        if player1_score>player2_score:
            print('Player 1 won!')
        elif player2_score>player1_score:
            print('Player 2 won!')
        else:
            print('It\'s a tie!')
        break
    else:
        continue
        
