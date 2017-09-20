import threading
import time


class Philosopher:

	IS_THINK = True
	IS_EAT = False

	def __init__(self, view, leftFurcula, rightFurcula):
		self.view = view
		self.leftFurcula = leftFurcula
		self.rightFurcula = rightFurcula

		self.eatThread = threading.Thread(target=self.eat, args=())

	def tryEat(self):
		result = self.leftFurcula.isAccess() and self.rightFurcula.isAccess()

		if not self.IS_EAT and result:
			self.eatThread.start()

		return result

	def eat(self):
		self.leftFurcula.setAccess(False)
		self.rightFurcula.setAccess(False)
		self.IS_EAT = True

		time.sleep(2)
