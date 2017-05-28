import time
import random

class Man(object):
	"""docstring for Man"""
	def __init__(self, heartBeat, bloodSugar, bloodPressure):
		super(Man, self).__init__()
		self.heartBeat = heartBeat
		self.bloodSugar = bloodSugar
		self.bloodPressure = bloodPressure
	
	def getHeatBeat(self):
		while True:
			yield self.heartBeat+random.normal(scale=self.heartBeat*0.01)
			time.sleep(1000)
	def getBloodSugar(self):
		while True:
			yield self.bloodSugar+random.normal(scale=self.bloodSugar*0.01)
			time.sleep(1000)
	def getBloodPressure(self):
		while True:
			yield self.bloodPressure+random.normal(scale=self.bloodPressure*0.01)
			time.sleep(1000)
