import gui,stopwatch
import RPi.GPIO as GPIO
class Controller (object):
	def __init__ (self):
		self.inputpin = 25;
		self.home()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.inputpin, GPIO.IN)
	def newGame(self):
		self.gui.startGameScreen()
		uhr = stopwatch.Stopwatch()
		fehlerzahl = 0
		def callback(channel):
			fehlerzahl = fehlerzahl + 1
		GPIO.add_event_detect(self.inputpin, GPIO.FALLING, callback = fehler(), bouncetime = 200)
		sleep (8)
		zeit = uhr.getTime() + fehlerzahl * 2
		print(zeit)