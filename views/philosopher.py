import numpy
from PyQt4.QtGui import (QLabel, QPixmap)


class Philosopher(QLabel):
	SIZE = 100

	def __init__(self, label, parent, i, mainSize, deskSize):
		QLabel.__init__(self, label, parent)
		picture = QPixmap('img/philosopher.png')
		self.setPixmap(picture)

		center = mainSize / 2 - self.SIZE / 2
		dx = numpy.cos(numpy.radians(90 + i * 72)) * (deskSize / 2 + 50)
		dy = numpy.sin(numpy.radians(90 + i * 72)) * (deskSize / 2 + 50)
		self.move(center + dx, center - dy)

