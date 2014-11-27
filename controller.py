import gui,stopwatch
import RPi.GPIO as GPIO
fehlerzahl = 0
inputpin = 25;
gui = gui.Gui()
def fehler ():
	fehlerzahl = fehlerzahl + 1
def newGame():
	gui.startGameScreen()
	uhr = stopwatch.Stopwatch()
	GPIO.add_event_detect(inputpin, GPIO.FALLING, callback = fehler(), bouncetime = 200)
	sleep (8)
	zeit = uhr.getTime() + fehlerzahl * 2
	print(zeit)
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputpin, GPIO.IN)
newGame()