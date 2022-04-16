
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptext():
	recognizer=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening.....")
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		try:
			print("recognizing...")
			data = recognizer.recognize_google(audio)
			print(data)
			return data
		except sr.UnknownValueError:
			print("Not  understand ")

def speechtx(x):
	engine = pyttsx3.init()
	vioces = engine.getProperty('voices')
	engine.setProperty('voice',vioces[0].id)
	rate = engine.getProperty('rate')
	engine.setProperty('rate',150)
	engine.say(x)
	engine.runAndWait()

# speechtx("it's another day to win, an opportunity to become better than i was yesterday")


if __name__ == '__main__':

	# if sptext().lower() == 'Hey peter':
	data1 = sptext().lower()

	if "your name" in data1:
		name = " my name is peter "
		speechx(name)

	elif "old are you" in data1:
		age= "i am two years old"
		speechtx(age)



	# else:
	# 	print("thanks")





