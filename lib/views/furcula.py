import numpy
from PyQt4.QtGui import (QWidget, QTransform, QLabel, QPixmap)
from PyQt4.QtCore import (Qt, pyqtSignal)


class Furcula(QLabel):
	WIDTH = 15
	HEIGHT = 45

	toggleFurcula = pyqtSignal(bool, QWidget)

	def __init__(self, parent, i, mainSize, deskSize):
		QLabel.__init__(self, parent)
		self.index = i

		picture = QPixmap('img/furcula.png')
		scaledPicture = picture.scaled(self.WIDTH, self.HEIGHT)

		transform = QTransform().rotate(i * (360 + 72) + 145)
		self.picture = transformPicture = scaledPicture.transformed(transform, Qt.SmoothTransformation)

		self.setPixmap(transformPicture)

		center = mainSize / 2 - self.WIDTH
		dx = numpy.cos(numpy.radians(128 - i * 72)) * (deskSize / 3)
		dy = numpy.sin(numpy.radians(128 - i * 72)) * (deskSize / 3)
		self.move(center + dx, center - dy)


