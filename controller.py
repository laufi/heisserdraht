import gui,stopwatch
import RPi.GPIO as GPIO
class Controller (object):
	def __init__ (self):
		inputpin = 25;
		self.home()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(inputpin, GPIO.IN)
	def home (self):
		self.gui = gui.Gui()
	def newGame(self):
		self.gui.startGameScreen()
		uhr = stopwatch.Stopwatch()
		GPIO.add_event_detect(inputpin, GPIO.FALLING, callback = uhr.fehler(), bouncetime = 200)
		sleep (8)
		zeit = uhr.getTime()
		print(zeit)