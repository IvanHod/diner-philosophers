class Furcula:

	ACCESS = True

	def __init__(self, view):
		self.view = view

	def isAccess(self):
		return self.ACCESS

	def setAccess(self, isAccess):
		self.ACCESS = isAccess
		if isAccess:
			self.view.show()
		else:
			self.view.hide()