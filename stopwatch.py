import time
class Stopwatch (object):
	def start (self):
		self.beginningTime = time.time()
	def stop (self):
		self.endTime = time.time()
		self.time = self.endTime - self.beginningTime
	def getTime (self):
		return(self.time)