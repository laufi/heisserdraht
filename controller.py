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
	def newGame(self):
		self.gui.startGameScreen()
		uhr = stopwatch.Stopwatch()
		fehlerzahl = 0
		GPIO.add_event_detect(self.inputpin, GPIO.FALLING, callback = fehlerzahl++, bouncetime = 200)
		sleep (8)
		zeit = uhr.getTime() + fehlerzahl * 2
		print(zeit)