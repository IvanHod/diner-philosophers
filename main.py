from PyQt4 import QtCore
from PyQt4.QtGui import *
import os
import sys


class MainApp(QWidget):
	def __init__(self):
		super(MainApp, self).__init__()
		# set window title
		self.setWindowTitle(u'dinner philosophers')
		# set window settings
		self.left = 300
		self.width = 550
		self.top = 100
		self.height = 500
		self.setGeometry(self.left, self.top, self.width, self.height)

		# create window


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainApp()
	ex.show()
	sys.exit(app.exec_())
