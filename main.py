# coding=utf-8
import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import *

from lib.views.furcula import Furcula as ViewFurcula
from lib.views.philosopher import Philosopher as ViewPhilosopher
from lib.models.furcula import Furcula
from lib.models.philosopher import Philosopher


class MainApp(QWidget):
	SIZE = 600
	DESK_SIZE = 300

	philosophers = []

	def __init__(self):
		super(MainApp, self).__init__()

		self.createMainWindow()

		self.addDesk()

		self.addObjects()

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

	# Добавить стол
	def addDesk(self):
		image = QPixmap('img/table.png')
		scaledImage = image.scaled(self.DESK_SIZE, self.DESK_SIZE)

		label = QLabel('', self)
		label.setPixmap(scaledImage)
		offset = self.SIZE / 2 - self.DESK_SIZE / 2
		label.move(offset, offset)

	# добавить объекты игры
	def addObjects(self):
		for i in range(0, 5):
			ViewPhilosopher(self, i, self.SIZE, self.DESK_SIZE)
			ViewFurcula(self, i, self.SIZE, self.DESK_SIZE)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainApp()
	sys.exit(app.exec_())
