import gui,stopwatch
import RPi.GPIO as GPIO
class Controller (object):
	def __init__ (self):
		self.inputpin = 25;
		self.home()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.inputpin, GPIO.IN)
	def home (self):
		self.gui = gui.Gui()
	def fehler (self, channel):
		self.uhr.fehler()
	def newGame(self):
		self.gui.startGameScreen()
		self.uhr = stopwatch.Stopwatch()
		GPIO.add_event_detect(self.inputpin, GPIO.FALLING, callback = self.fehler(), bouncetime = 200)
		sleep (8)
		zeit = self.uhr.getTime()
		print(zeit)