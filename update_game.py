import random
import sys
hidden = random.randrange(1,201)

while True:
    user_input= input("Please enter your guess[X]: ")
    print(user_input)

    if user_input == 'x':
        print('sad to see you leaving early')
        sys.exit()

    guess = int(user_input)
    if guess == hidden:
        print("Hit!")
        break
    if guess < hidden:
        print("your guess is too low")
    else:
        print("your guess is too hight")
        # Write your code here :-)
