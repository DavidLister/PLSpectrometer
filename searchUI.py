# searchUI.py
#
# Used as search and plotting tab in the main GUI
# Created by Elliot Wadge and Colton Lohn
# Edited by Alistair Bevan
# August 2023
#

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import QThread
from workers.search import searchWorker
from workers.plot import plotWorker
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QScrollArea,
    QHBoxLayout,
    QProgressBar,
    QTextBrowser
)


class SearchUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Plotting Spectra')
        self.resize(600, 600)

        # This is the outer most widget which will contain the other widgets
        outerLayout = QVBoxLayout()

        # The top layout which contains the search related inputs and buttons
        self.searchLayout = QFormLayout()
        self.sampleNameInput = QLineEdit()
        self.sampleYearInput = QLineEdit()
        self.searchBtn = QPushButton('Search')
        self.searchLayout.addRow('Sample Name:', self.sampleNameInput)
        self.searchLayout.addRow('Sample Year:', self.sampleYearInput)
        self.searchLayout.addRow(self.searchBtn)

        # self.scroll = QScrollArea()  # This seems to be unnecessary
        self.fileDisplay = QTextBrowser()
        self.fileDisplay.setOpenLinks(False)

        # The botton Layout
        self.plotLayout = QFormLayout()
        self.filePathInput = QLineEdit()
        self.plotBtn = QPushButton('Plot')
        self.plotLayout.addRow('Enter Path:', self.filePathInput)
        self.plotLayout.addRow(self.plotBtn)

        outerLayout.addLayout(self.searchLayout)
        outerLayout.addWidget(self.fileDisplay)
        outerLayout.addLayout(self.plotLayout)

        self.setLayout(outerLayout)
        self.connect_btns()

    def connect_btns(self):
        self.searchBtn.clicked.connect(self.search)
        self.plotBtn.clicked.connect(self.plot)
        self.fileDisplay.anchorClicked.connect(self.plot)

    def search(self):
        # Get the sample name and year from the input boxes
        sampleName = self.sampleNameInput.text()
        year = self.sampleYearInput.text()
        self.fileDisplay.setPlainText('')
        # Set up the thread
        self.thread = QThread()
        self.searchWorker = searchWorker(sampleName,year)
        self.searchWorker.moveToThread(self.thread)
        self.thread.started.connect(self.searchWorker.search)
        self.searchWorker.finished.connect(self.thread.quit)
        self.searchWorker.finished.connect(self.searchWorker.deleteLater)
        self.searchWorker.sample.connect(self.display)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.doneSearch)
        # Start the thread
        self.searchBtn.setText('Searching...')
        self.thread.start()

    def display(self, path, id):
        self.fileDisplay.append("<a href=" + path.replace(" ", "%20") + ">" + path + "</a>")
        self.fileDisplay.append("<p>" + id + "</p><br>")

    def doneSearch(self):
        self.searchBtn.setText('Search')

    def donePlot(self):
        self.plotBtn.setText('Plot')

    def plot(self, path):
        filepath = path.path()
        self.thread = QThread()
        self.plotWorker = plotWorker(filepath)
        self.plotWorker.moveToThread(self.thread)
        self.thread.started.connect(self.plotWorker.plot)
        self.plotWorker.finished.connect(self.thread.quit)
        self.plotWorker.finished.connect(self.plotWorker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.donePlot)
        self.plotBtn.setText('Plotting...')
        self.thread.start()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = SearchUI()
    window.show()
    sys.exit(app.exec())
