from random import randint
ask='yes'
while(ask=='yes'):


	print('Text: Rock / Papper / Scissors')
	player=input('Your turn: ')
	player=player.lower()
	computer=randint(0,2)


	if computer==0:
		computer='rock'
	if computer==1:
		computer='scissors'
	else:
		computer='papper'

	print('---')
	print('Computer choose: ' +computer)
	print('---')

	if computer==player:
		print('Draw')
	else:
		if player=='rock':		
			if computer=='papper':
				print('You lose!')
			else:
				print('You win!')
		if player =='papper':
			if computer =='rock':
				print('You win!')
			else:
				print('You lose!')
		if player=='scissors':
			if computer=='papper':
				print('You win!')
			else:
				print('You lose')
	print('Do u want to continue playing?( Yes or No) ')
	ask=input()
	ask=ask.lower()

