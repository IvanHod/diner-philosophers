import numpy
from PyQt4.QtGui import (QTransform, QLabel, QPixmap)
from PyQt4.QtCore import (Qt)


class Furcula(QLabel):
	WIDTH = 15
	HEIGHT = 45

	def __init__(self, parent, i, mainSize, deskSize):
		QLabel.__init__(self, parent)

		picture = QPixmap('img/furcula.png')
		scaledPicture = picture.scaled(self.WIDTH, self.HEIGHT)

		transform = QTransform().rotate(i * (360 - 72))
		transformPicture = scaledPicture.transformed(transform, Qt.SmoothTransformation)

		self.setPixmap(transformPicture)

		center = mainSize / 2 - self.WIDTH
		dx = numpy.cos(numpy.radians(i * 72 - 90)) * (deskSize / 3)
		dy = numpy.sin(numpy.radians(i * 72 - 90)) * (deskSize / 3)
		self.move(center + dx, center - dy)


