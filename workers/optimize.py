import time
import random
from PyQt5 import QtMultimedia as qtmm
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
import sys

class optimizeWorker(QObject):

    bar_update = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self,spectrometer):
        super().__init__()
        self.abort = False
        self.player = qtmm.QMediaPlayer()
        # Volume
        #current path is the dir containing the file being run so the 'GUI' file in our case
        #if you're not hearing sound print this value and make sure its what you expect
        url = qtc.QUrl(qtc.QDir.currentPath()+'/workers/chirp.wav')
        print(url)
        self.player.setVolume(70)
        self.set_file(url)
        self.spectrometer = spectrometer

    def set_file(self, url):
        if url.scheme() == '':
            url.setScheme('file')
        content = qtmm.QMediaContent(url)
        self.playlist = qtmm.QMediaPlaylist()
        self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(1)
        self.player.setPlaylist(self.playlist)

    def optimize(self):

        counts = []
        maximum = 100
        changeScale = True


        while not self.abort:

            counts = 0

            while changeScale:
                if counts >= maximum:
                    maximum *= 10

                elif counts < maximum/10:
                    maximum /= 10

                if (counts < maximum and counts >= maximum/10) or counts == 0:
                    changeScale = False
            print(maximum)
            self.bar_update.emit(counts)
            playStart = int(60*1000*(counts/maximum))
            print(playStart)
            self.player.setPosition(playStart)
            self.player.play()
            self.spectrometer.read(0.2)
            self.player.stop()

        self.finished.emit()

class spectrometer():

    def __init__(self):
        self.x = 5
        pass

    def read(self):
        return 100

if __name__ == '__main__':
    spec = spectrometer()
    ans = spec.read()
    print(ans)
    opt = optimizeWorker(spec)
    opt.optimize()
