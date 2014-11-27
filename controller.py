import gui,stopwatch
import RPi.GPIO as GPIO
def fehler ():
	fehlerzahl = fehlerzahl + 1
def newGame():
	gui.startGameScreen()
	uhr = stopwatch.Stopwatch()
	fehlerzahl = 0
	GPIO.add_event_detect(inputpin, GPIO.FALLING, callback = fehler(), bouncetime = 200)
	sleep (8)
	zeit = uhr.getTime() + fehlerzahl * 2
	print(zeit)
inputpin = 25;
gui = gui.Gui()
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputpin, GPIO.IN)
newGame()