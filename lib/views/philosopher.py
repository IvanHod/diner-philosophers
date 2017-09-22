import numpy
from PyQt4.QtGui import (QWidget, QLabel, QTransform, QPixmap)
from PyQt4.QtCore import (Qt, pyqtSignal)

class Philosopher(QLabel):
	SIZE = 100

	toggleState = pyqtSignal(bool, QWidget)

	def __init__(self, parent, i, mainSize, deskSize):
		QLabel.__init__(self, '', parent)
		self.index = i
		picture = QPixmap('img/philosopher.png')

		if i < 3:
			transform = QTransform().scale(-1, 1)
			picture = picture.transformed(transform, Qt.SmoothTransformation)

		self.setPixmap(picture)

		center = mainSize / 2 - self.SIZE / 2
		dx = numpy.cos(numpy.radians(90 - i * 72)) * (deskSize / 2 + self.SIZE / 2)
		dy = numpy.sin(numpy.radians(90 - i * 72)) * (deskSize / 2 + self.SIZE / 2)
		self.move(center + dx, center - dy)

	def setState(self, isEat):
		self.setAutoFillBackground(isEat)
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.green)
		self.setPalette(p)
