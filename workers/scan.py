# scan.py
#
# Scan worker which does the scanning
# Created by Elliot Wadge
# Edited by Alistair Bevan
# August 2023
#

import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from miscellaneous import available_name, make_header
from temperature import TemperatureSensor
from datetime import datetime
import os


class scanWorker(QObject):

    # This is all the information we will be sending to UI while we run
    data = pyqtSignal(list)
    position = pyqtSignal(float)
    finished = pyqtSignal()

    # Needs to take a spectrometer, start, end, step, and time
    def __init__(self, spectrometer, start, end, step, time, filename, sample_id):
        super().__init__()
        self.spectrometer = spectrometer
        self.start = start
        self.end = end
        self.step = step
        self.time = time
        self.abort = False
        
        # File path for saving data
        home_dir = os.path.expanduser('~')
        # absolute = os.path.join(home_dir, 'Documents', 'PL', 'Data')  # Saves to data folder in documents
        absolute = os.path.join(home_dir, 'Simon Fraser University (1sfu)', 'Simon Watkins - MOCVD-LAB', 'data', 'ZnO', 'PL', 'Data')  # Saves to OneDrive
        dt_string = datetime.now().strftime("%Y %m %d")
        directory = os.path.join(absolute, dt_string)
        os.makedirs(directory, exist_ok=True)
    
        filepath = os.path.join(directory, filename)
        print(filepath)
        self.filename = available_name(filepath)
        self.sample_id = sample_id

    def scan(self):
        # Step 1: Copy the move function to get into position
        start = self.spectrometer.position
        end = self.start  # We want to move to the start point
        distance = round(abs(end - start), 3)

        if end < start:
            direction = -1
        else:
            direction = 1

        high = 1/(2*self.spectrometer.frequency)
        low = high
        
        # Set the direction voltage
        self.spectrometer.set_direction(direction)  # See spectrometer.py for the method

        if direction < 0:
            self.spectrometer.move(distance + 20, high_time = high, low_time = low)  # First move to 20 nm back
            direction = 1
            self.spectrometer.set_direction(direction)  # Change directions
            self.spectrometer.move(19.97, high_time = high, low_time = low)  # Move to 0.03 nm of the position
            self.spectrometer.move(0.03, high_time = high, low_time = 0.25)  # Do the last 0.03 nm with 1 s in between each step

        elif direction >= 0:  # Move within 0.03 nm and then slow down
            if distance < 0.03:
                self.spectrometer.move(distance, high_time = high, low_time = 0.25)
            else:
                self.spectrometer.move(distance - 0.03, high_time = high, low_time = low)
                self.spectrometer.move(0.03, high_time = high, low_time = 0.25)

        self.position.emit(end)

        # Step 2: Prepare for the scan and create file
        start = self.start
        end = self.end
        print(start)
        print(end)
        distance = round(abs(end - start), 3)
        print(distance)
        direction = 1
        f = open(self.filename, 'a')
        make_header(f, self.sample_id, self.time)
        f.close()
        number_of_steps = int(distance/self.step)
        print(number_of_steps)

        # Step 3: Start the scanning process
        for i in range(number_of_steps + 1):

            if self.abort:  # End the scan if abort is pressed
                self.finished.emit()
                return

            # We need to take one extra data point at the start point and not step forward
            if i != 0:
                self.spectrometer.move(self.step, high_time=high, low_time=low)
                self.position.emit(self.spectrometer.position + self.step)

            counts = self.spectrometer.read(self.time)
            self.data.emit([self.spectrometer.position, counts])  # Send data to be plotted
            print(f"{counts} counts/s")

            temperature = self.temperature_sensor.read_temperature()
            print(f"{temperature}")

            # Opening and closing in loop means in case of a crash we keep the data
            f = open(self.filename, 'a')
            f.write(str(self.spectrometer.position) + '\t' + str(counts) + '\t' + str(temperature) + '\n')
            f.close()

        self.finished.emit()  # Emit that we're done
