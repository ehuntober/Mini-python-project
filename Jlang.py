# ####################### LUCKY SEVEN ########################################
"""
PROGRAM RULES : In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7,
the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible, a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so
on. A little mathematical analysis reveals that there are not enough ways to win
to make the game worthwhile; however, because many people’s eyes glaze over
at the first mention of mathematics, your challenge is to write a program that
demonstrates the futility of playing the game. Your program should take as input
the amount of money that the player wants to put into the pot, and play the game
until the pot is empty. At that point, the program should print the number of
rolls it took to break the player, as well as maximum amount of money in the pot.

AUTHOR: EZELU JOSEPH JOHN
LANGUAGE : PYTHON
DATE: 22ND JULY 2020
"""


from random import choice


def roll_dice():
    user_money = float(input("How much do you want to play with?\n> "))
    rolls = 0
    max_amount = user_money

    while True:
        selection = (choice(range(1, 7)), choice(range(1, 7)))
        rolls += 1

        if sum(selection) == 7:
            user_money += 4
            if user_money > max_amount:
                max_amount = user_money
            else:
                pass
        else:
            user_money -= 1
            if user_money < 1:
                print("Game over")
                print(f"You were bankrupt within {rolls} rolls")
                print(f"The maximum money in the pot was ${max_amount}")
                break
            else:
                pass


roll_dice()
