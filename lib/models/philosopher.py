class Philosopher:

	IS_THINK = True
	IS_EAT = False

	def __init__(self, view, leftFurcula, rightFurcula):
		self.view = view
		self.leftFurcula = leftFurcula
		self.rightFurcula = rightFurcula

	def canEat(self):
		result = self.IS_EAT
		if not result:
			result = self.leftFurcula.isAccess() and self.rightFurcula.isAccess()
		return result
