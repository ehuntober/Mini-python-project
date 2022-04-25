
import random
hidden = random.randrange(1,21)

print('the hidden values is ' , hidden)

user_input = input('please enter your guess: ')
print(user_input)

guess = int(user_input)

if guess == hidden:
    print('Hit!')
elif guess < hidden:
    print('your guess is too low')
else:
    print('your guess is too hight')
    # Write your code here :-)
