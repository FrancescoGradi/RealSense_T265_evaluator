import sys
import glob
import subprocess


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

from mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.fileList = []

        self.currentTime = QtCore.QTime(0, 0, 0)
        self.lcdNumber.display(self.currentTime.toString('hh:mm:ss'))
        self.timer = QtCore.QTimer(self)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

        for file in glob.glob('../tests/*.py'):
            self.listWidget.addItem(file[5:])
            self.fileList.append(file)

    def start(self):
        current_file = self.listWidget.currentRow()
        self.my_file = self.fileList[current_file]
        print('START ' + str(self.my_file))
        self.timerId = self.startTimer(1000)

        #os.system('python ' + str(my_file))
        self.my_process = subprocess.Popen(['python3', str(self.my_file), 'arg1', 'arg2'])

    def stop(self):
        print('STOP ' + str(self.my_file))
        self.my_process.terminate()
        self.killTimer(self.timerId)
        QMessageBox.about(self, "Time", "Execution time: " + str(self.currentTime.toString('hh:mm:ss')))
        self.currentTime = QtCore.QTime(0, 0, 0)
        self.lcdNumber.display(self.currentTime.toString('00:00:00'))

    def timerEvent(self, e):
        if not e.timerId() == self.timerId: return

        self.currentTime = self.currentTime.addSecs(1)
        self.lcdNumber.display(self.currentTime.toString('hh:mm:ss'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

