from time import *

import random as r 

print(time())


def mistake(partest, usertest):

	error = 0
	for i in range(len(partest)):
		try:
			if partest[i] != usertest[i]:
				error = error + 1
		except:
			erroor = error + 1
	return error


def speed_time(time_s, time_e, userinput):
	time_delay = time_e - time_s
	time_R = round(time_delay, 2)
	speed = len(userinput) / time_R
	return round(speed)

if __name__ == '__main__':
	while True:
		ck = input(" ready to test: yes /no :")
		if ck == "yes":
			test = [" As anyone who has built a website knows,", " there is much more to think \
			about than just the content. Design," "color, navigation, and appropriate ",
			"technology are all important aspects of a good site. ", "welcome to my coding life"]

			test1 = r.choice(test)

			print("******** Typing speed **********")
			print(test1)
			print()
			print()
			time_1 = time()
			test_input = input('Enter : ')
			time_2 = time()

			print('speed: ', speed_time(time_1, time_2, test_input), "w/sec")
			print('Error: ', mistake(test1,test_input))
		elif ck == 'no':
			print(" thank you ")
			break

		else:
			print(" wrong input ")

