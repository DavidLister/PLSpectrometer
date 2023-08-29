# move.py
#
# Move worker which does all the moving
# Created by Elliot Wadge
# Edited by Alistair Bevan
# August 2023
#

import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class moveWorker(QObject):

    # These are the signals that are connected to functions in GUI.py
    position = pyqtSignal(float)
    finished = pyqtSignal()

    # To initialize we need to take the spectrometer that is being moveToThread
    def __init__(self, spectrometer, end):
        super().__init__()  # This just calls the parent init method and is always required if making a worker
        self.spectrometer = spectrometer  # Will be either single or double
        self.end = end  # The desination
        self.abort = False

    def move(self):
        start = self.spectrometer.position  # Get the current position
        end = self.end  # Get the end position
        distance = round(abs(end - start), 3)

        if end < start:
            direction = -1
        elif end > start:
            direction = 1
        else:
            self.finished.emit()
            return

        high = 1/(2*self.spectrometer.frequency)
        low = high
        # Set the direction voltage
        self.spectrometer.set_direction(direction)  # See spectrometer.py for the method

        if direction < 0:  # If the direction is backwards
            self.spectrometer.move(distance + 20, high_time = high, low_time = low)  # First move to 20 nm back from start
            direction = 1
            self.spectrometer.set_direction(direction)  # Change directions
            self.spectrometer.move(19.97, high_time = high, low_time = low)  # Move to within 0.03 nm of the positin
            self.spectrometer.move(0.03, high_time = high, low_time = 0.25)  # Do the last 0.03 nm with 1s in between each step (4 pulses a step)

        elif direction >= 0:  # Otherwise just move forwards within 0.03 and then slow down
            if distance < 0.03:
                self.spectrometer.move(distance, high_time = high, low_time = 0.25)
            else:
                self.spectrometer.move(distance - 0.03, high_time = high, low_time = low)
                self.spectrometer.move(0.03, high_time = high, low_time = 0.25)

        self.position.emit(end)
        self.finished.emit()  # Emit that we're done

    def check_abort(self):
        if self.abort:
            self.finished.emit()
            return
