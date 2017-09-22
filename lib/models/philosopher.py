import threading
import time


class Philosopher:

	IS_THINK = True
	IS_EAT = False

	def __init__(self, view, leftFurcula, rightFurcula):
		self.view = view
		self.leftFurcula = leftFurcula
		self.rightFurcula = rightFurcula

	def tryEat(self):
		result = self.leftFurcula.isAccess() and self.rightFurcula.isAccess()

		canEat = not self.IS_EAT and result
		if canEat:
			thread = threading.Thread(target=self.eat)
			thread.start()

		return result

	def eat(self):
		print 'eat'
		self.leftFurcula.setAccess(False)
		self.rightFurcula.setAccess(False)
		self.view.setEat(True)
		self.IS_EAT = True

		time.sleep(3)

		self.leftFurcula.setAccess(True)
		self.rightFurcula.setAccess(True)
		self.IS_EAT = False
		self.view.setEat(False)
