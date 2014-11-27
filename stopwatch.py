import time
class Stopwatch (object):
	def start (self):
		self.beginningTime = time.time()
		self.fehlerzahl = 1
	def stop (self):
		self.endTime = time.time()
		self.time = self.endTime - self.beginningTime
	def fehler(self):
		self.fehlerzahl = self.fehlerzahl + 1;
	def getTime (self):
		return(self.time + self.fehlerzahl * 2)