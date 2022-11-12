import random
player = input('enter r(rock) or p(paper) or s(sicssors): ')
computer = random.choice(['r', 'p', 's'])
if player == 'r' and computer == 's' or player == 'p' and computer == 'r' or player == 's' and computer == 'p':
    print('player is winer')
elif player == 'r' and computer == 'r' or player == 'p' and computer == 'p' or player == 's' and computer == 's':
    print('equal')
elif player == 'r' and computer == 'p' or player == 'p' and computer == 's' or player == 's' and computer == 'r':
    print('computer is winer')