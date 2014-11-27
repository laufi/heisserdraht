import time
class Stopwatch (object):
	def start (self):
		self.beginningTime = time.time()
		self.fehleranzahl = 0
	def stop (self):
		self.endTime = time.time()
		self.time = self.endTime - self.beginningTime
	def fehler(self):
		self.fehleranzahl = self.fehleranzahl + 1;
	def getTime (self):
		return(self.time)