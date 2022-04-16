from instabot import Bot

bot = Bot()
bot.login(username='etoer', password="****************")
bot.follow('ehuntober')
bot.upload_photo('c:/Users/ehuntober/Desktop/min-python/game.png',caption="I love python")
bot.unfollow('ehuntober')

bot.send_message('python is cool', ['ehuntobers','wissdww'])

followers = bot.get_user_followers('ehuntober')

for follower in followers:
	print(bot.get_user_info(followers))

following = bot.get_user_following('ehuntober')
for Following in following:
	print(bot.get_user_info(Following))
