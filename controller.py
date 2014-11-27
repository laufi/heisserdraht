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
		self.fehlerzahl = self.fehlerzahl + 1
	def newGame(self):
		self.gui.startGameScreen()
		uhr = stopwatch.Stopwatch()
		self.fehlerzahl = 0
		GPIO.add_event_detect(self.inputpin, GPIO.FALLING, callback = self.fehler(), bouncetime = 200)
		sleep (8)
		zeit = uhr.getTime() + fehlerzahl * 2
		print(zeit)