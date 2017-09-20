import numpy
from PyQt4.QtGui import (QLabel, QTransform, QPixmap)
from PyQt4.QtCore import (Qt)

class Philosopher(QLabel):
	SIZE = 100

	def __init__(self, parent, i, mainSize, deskSize):
		QLabel.__init__(self, '', parent)
		picture = QPixmap('img/philosopher.png')

		if i < 3:
			transform = QTransform().scale(-1, 1)
			picture = picture.transformed(transform, Qt.SmoothTransformation)

		self.setPixmap(picture)

		center = mainSize / 2 - self.SIZE / 2
		dx = numpy.cos(numpy.radians(90 + i * 72)) * (deskSize / 2 + self.SIZE / 2)
		dy = numpy.sin(numpy.radians(90 + i * 72)) * (deskSize / 2 + self.SIZE / 2)
		self.move(center + dx, center - dy)

