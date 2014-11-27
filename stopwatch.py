import time
class Stopwatch (object):
	def start (self):
		self.fehleranzahl = 0
		self.beginningTime = time.time()
	def stop (self):
		self.endTime = time.time()
		self.time = self.endTime - self.beginningTime
		self.fehleranzahl = self.fehleranzahl + 1;
	def fehler(self):
		return(self.time + self.fehleranzahl * 2)
	def getTime (self):