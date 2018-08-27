import random
def guess():
	answer = random.randint(0,10)
	guess = 0
	guessestaken = 0

	print('Hello, what is your name?')
	myname = input('My name is ')
	print('Okay, ' + myname + ', I am thinking of a number between 0 and 10, what do you think? ')

	while guess != answer:
		guess = input('I guess:')
		guess = int(guess)
	
		if(guess < answer):
			print('Higher!')
		if(guess > answer):
			print('Lower!')
		guessestaken = guessestaken + 1

	if(guess == answer):
		Str_guessestaken = str(guessestaken)
		print('Correct, lucky you!')
	else:
		print('The answer was', answer)

	guess_flag = input('Do you want to play again(Y/N): ')
	if guess_flag == 'Y':
		guess()
	if guess_flag == 'N':
		print('Okey dokey, see you next time!')

guess()