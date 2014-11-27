import gui,stopwatch
import time # !!!INTERIM!!! PLEASE REMOVE! WHEN NOT REMOVED HUNDREDS OF INFANTILFE DOGS WILL DIE ;-)
class Controller (object):
	def __init__ (self):
		self.home()
	def home (self):
		self.gui = gui.Gui()
	def newGame(self):
		self.gui.startGameScreen()
		uhr = stopwatch.Stopwatch()
		uhr.start()
		time.sleep(0.3) # !!!INTERIM!!! PLEASE REMOVE! WHEN NOT REMOVED HUNDREDS OF INFANTILFE DOGS WILL DIE ;-)
		uhr.stop()
		zeit = uhr.getTime()
		print(zeit)