import gui,stopwatch
import RPi.GPIO as GPIO
class Controller (object):
	inputpin = 25;
	def __init__ (self):
		self.home()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(inputpin, GPIO.in)
	def home (self):
		self.gui = gui.Gui()
	def newGame(self):
		self.gui.startGameScreen()
		uhr = stopwatch.Stopwatch()
		GPIO.add_event_detect(inputpin, GPIO.FALLING, callback = uhr.fehler(), bouncetime = 200)
		sleep (8)
		zeit = uhr.getTime()
		print(zeit)