# optimize.py
#
# Defines the optimize function
# Created by Elliot Wadge
# Edited by Alistair Bevan
# July 2023
#

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
        # If you're not hearing sound print the url value and make sure it's what you expect
        # This file is a tone that goes from 800Hz to 400Hz over 60 seconds
        url = qtc.QUrl(qtc.QDir.currentPath()+'/Documents/PLSpectrometer/workers/chirp.wav')
        print(url)
        self.player.setVolume(70)
        self.set_file(url)
        self.spectrometer = spectrometer


    # Set the target file for our audio
    def set_file(self, url):
        if url.scheme() == '':
            url.setScheme('file')
        content = qtmm.QMediaContent(url)
        self.playlist = qtmm.QMediaPlaylist()
        self.playlist.addMedia(content)
        self.playlist.setCurrentIndex(1)
        self.player.setPlaylist(self.playlist)


    def optimize(self):
        rate_ma = 0
        rate_IIR_factor = 0.1
        maximum = 100
        changeScale = True
        counts = 1
        interval = 0.15
        self.player.play()
        # Keep running until abort is hit
        while not self.abort:
            # Set the play position in the file in order to change the tone
            playStart = int(60*1000*(counts/maximum))  # Higher counts equal higher frequency
            self.player.setPosition(playStart)
            self.player.play()
            counts = self.spectrometer.read(interval)  # Read the counts for 0.15 of a second
            rate = counts/interval
            rate_ma = rate*rate_IIR_factor + rate_ma*(1 - rate_IIR_factor)
            print(rate)
            self.player.pause()
            self.bar_update.emit(counts)  # Update the displayed value
            # Update the scale of our sound
            changeScale = True
            while changeScale:
                if counts >= maximum:
                    maximum *= 10

                elif counts < maximum/10:
                    maximum /= 10

                if (counts < maximum and counts >= maximum/10) or counts == 0:
                    changeScale = False
        # Stop the player
        self.player.stop()
        self.player.setPosition(0)
        self.finished.emit()



# Dummy class for testing (uses random number generator)
class spectrometer():


    def __init__(self,start,end):
        self.x = 5
        self.start = start
        self.end = end
        pass


    def read(self,duration):
        time.sleep(duration)
        return random.randint(self.start,self.end)  # Generate 


# Test
if __name__ == '__main__':
    spec = spectrometer(0,1000)
    opt = optimizeWorker(spec)
    opt.optimize()
    # time.sleep(3)
    # spec2 = spectrometer(100,200)
    # opt2 = optimizeWorker(spec2)
    # opt2.optimize()
