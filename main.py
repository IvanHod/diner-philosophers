# coding=utf-8
from PyQt4 import QtGui

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import sys
from philosopher import Philosopher
from furcula import Furcula

class MainApp(QWidget):

	SIZE = 600
	DESK_SIZE = 300

	def __init__(self):
		super(MainApp, self).__init__()

		self.createMainWindow()

		self.addDesk()

		self.addPhilosophers()

		self.show()

	# Создать главное окно
	def createMainWindow(self):
		self.resize(self.SIZE, self.SIZE)
		self.center()

		self.setWindowTitle(u'Dinner philosophers')
		self.setWindowIcon(QIcon('icon.png'))

		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.white)
		self.setPalette(p)

	# Выровнять окно приложения по центру
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def addDesk(self):
		image = QPixmap('img/table.png')
		scaledImage = image.scaled(self.DESK_SIZE, self.DESK_SIZE)

		label = QLabel('', self)
		label.setPixmap(scaledImage)
		offset = self.SIZE / 2 - self.DESK_SIZE / 2
		label.move(offset, offset)

	def addPhilosophers(self):
		for i in range(0, 5):
			Philosopher(self, i, self.SIZE, self.DESK_SIZE)
			Furcula(self, i, self.SIZE, self.DESK_SIZE)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainApp()
	sys.exit(app.exec_())
