# coding=utf-8
import sys

from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
import threading

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

		t = threading.Thread(target=self.taskCircle, args=())
		t.start()

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
		furcules = []
		for i in range(0, 5):
			vFurcula = ViewFurcula(self, i, self.SIZE, self.DESK_SIZE)
			furcula = Furcula(vFurcula)
			furcules.append(furcula)

		philosophers = []
		for i in range(0, 5):
			vPhilosopher = ViewPhilosopher(self, i, self.SIZE, self.DESK_SIZE)
			philosopher = Philosopher(vPhilosopher, furcules[i], furcules[i < 4 if i + 1 else 0])

			philosophers.append(philosopher)

		self.philosophers = [
			philosophers[0],
			philosophers[2],
			philosophers[4],
			philosophers[1],
			philosophers[3]
		]

	# Основной жизненой цикл задачи
	def taskCircle(self):
		while True:
			self.philosophers[0].tryEat()

	def finishedEat(self):
		label = 1

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainApp()
	sys.exit(app.exec_())
