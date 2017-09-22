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
		result &= not self.IS_EAT

		if result:
			thread = threading.Thread(target=self.eat)
			thread.start()

		return result

	def eat(self):
		self.toggleEatProcess(True)

		time.sleep(4)

		self.toggleEatProcess(False)

	def toggleEatProcess(self, isEat):
		self.view.toggleState.emit(isEat, self.view)
		self.IS_EAT = isEat
		self.leftFurcula.setAccess(not isEat)
		self.rightFurcula.setAccess(not isEat)
