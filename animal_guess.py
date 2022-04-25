'''

Animal guess game 

'''

score = 0
# print('Guess the Animal')
# guess1 = input("What bear lives at the North pole? ")




# guess = input('Which one of these is a fish?\n \
# A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
# Type A, B, C, or D ')

def check_guess(guess, answer):
	global score
	still_guessing = True
	attempt = 0

	while still_guessing and attempt < 3:
		
		if guess.lower() == answer.lower():
			print('Correct answer')
			score = score + 3 - attempt
			still_guessing = False
		else:
			if attempt < 2:
				guess = input('Sorry wrong answer. Try again. ') 
				attempt = attempt + 1
	if attempt == 3:
		print('The correct answer is ' + answer)



# check_guess(guess, 'C')
# guess2 = input('Which is the fastest land animal? ')
# check_guess(guess2, 'cheetah')
# guess3 = input('Which is the largest animal? ')
# check_guess(guess3, 'blue whale')

# print('Your score is ' + str(score))

def print_seconds_per_day():
	hours = 24
	minutes = hours * 60
	seconds = minutes * 60
	print(seconds)

print_seconds_per_day()
