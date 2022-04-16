from plyer import notification

import time

if __name__=='__main__':
	while True:
		notification.notify(title = "*** Take Rest",
				 message= " Today remember to code, you will soon become a pythonista world class",
				app_icon="C:/Users/ehuntober/Desktop/min-python/Mini-python-project/game.ico",
				timeout=5 )
		time.sleep(10)
