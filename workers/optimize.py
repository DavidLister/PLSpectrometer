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
        #this file is a tone that goes from 800Hz to 400Hz of 60 seconds
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
        counts = 1
        interval = 0.15
        self.player.play()
        while not self.abort:

            playStart = int(60*1000*(counts/maximum))
            #There's something really weird going on with the ordering of the two lines below
            self.player.setPosition(playStart)
            self.player.play()
            counts = self.spectrometer.read(interval)
            self.player.pause()
            self.bar_update.emit(counts)
            changeScale = True
            while changeScale:
                if counts >= maximum:
                    maximum *= 10

                elif counts < maximum/10:
                    maximum /= 10

                if (counts < maximum and counts >= maximum/10) or counts == 0:
                    changeScale = False

        self.player.stop()
        self.player.setPosition(0)
        self.finished.emit()



#dummy class for testing
class spectrometer():

    def __init__(self,start,end):
        self.x = 5
        self.start = start
        self.end = end
        pass

    def read(self,duration):
        time.sleep(duration)
        return random.randint(self.start,self.end)

#test
if __name__ == '__main__':
    spec = spectrometer(0,1000)
    opt = optimizeWorker(spec)
    opt.optimize()
    # time.sleep(3)
    # spec2 = spectrometer(100,200)
    # opt2 = optimizeWorker(spec2)
    # opt2.optimize()
