import time
class Stopwatch (object):
	def __init__ (self):
		self.fehlerzahl = 0
	def start (self):
		self.beginningTime = time.time()
	def stop (self):
		self.endTime = time.time()
		self.time = self.endTime - self.beginningTime
	def fehler(self):
		self.fehlerzahl = self.fehlerzahl + 1;
	def getTime (self):
		return(self.time + self.fehlerzahl * 2)