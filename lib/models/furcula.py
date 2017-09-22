from PyQt4.QtCore import SIGNAL


class Furcula:

	ACCESS = True

	def __init__(self, view, i):
		self.view = view
		self.number = i

	def isAccess(self):
		return self.ACCESS

	def setAccess(self, isAccess):
		self.ACCESS = isAccess
		self.view.toggleFurcula.emit(isAccess, self.view)
