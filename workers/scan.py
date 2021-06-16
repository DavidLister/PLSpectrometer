import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from miscellaneous import available_name, make_header

#this is the scan worker he does the scanning
class scanWorker(QObject):

    #this is all the information we will be sending to UI while we run
    data = pyqtSignal(float)
    position = pyqtSignal(float)
    finished = pyqtSignal()

    #needs to take a spectrometer, start, end, step, and time
    def __init__(self,spectrometer,start,end,step,time,filename,sample_id):
        super().__init__()
        self.spectrometer = spectrometer
        self.start = start
        self.end = end
        self.step = step
        self.time = time
        self.abort = False
        self.filename = available_name(filename)
        self.sample_id = sample_id




    def scan(self):

        #first copy the move function to get into position
        start = self.spectrometer.position
        end = self.start#we want to move to the start point
        distance = abs(end - start)

        try:
            direction = int((end - start)/distance)#catch divide by zero error
        except:
            direction = 1

        high = 1/(2*self.spectrometer.frequency)
        low = high
        #set the direction voltage
        self.spectrometer.set_direction(direction)#see spectrometer.py for the method

        if direction < 0:
            self.spectrometer.move(distance + 10, high_time = high, low_time = low)#first move to ten nm back
            direction = 1
            self.spectrometer.set_direction(direction) #change directions
            self.spectrometer.move(9.97, high_time = high, low_time = low) #move to 0.03 nm of the position
            self.spectrometer.move(0.03, high_time = high, low_time = 0.25) #do the last 0.03 nm with 1s in between each pulse

        elif direction >= 0:
            if distance < 0.03:#if distance is less than ten we need to go backwards
                self.spectrometer.move(distance, high_time = high, low_time = 0.25)
            else:#otherwise just move forwards within 0.03 and then slow down
                self.spectrometer.move(distance - 0.03, high_time = high, low_time = low)
                self.spectrometer.move(0.03, high_time = high, low_time = 0.25)

        self.position.emit(end)

        #prepare for the scan
        start = self.start
        end = self.end
        distance = abs(end - start)
        direction = 1
        f = open(self.filename, 'w')
        make_header(f,self.sample_id,self.time)
        f.close()
        number_of_steps = int(distance/self.step)
        print(number_of_steps)
        #start the scanning process
        for i in range(number_of_steps + 1):

            if self.abort:
                self.finished.emit()
                return

            counts = self.spectrometer.read(self.time)
            self.data.emit(counts)#send data to be plotted
            print(counts)
            #opening and closing in loop means in case of a crash we keep the data
            f = open(self.filename, 'a')
            f.write(str(self.spectrometer.position) + '\t' + str(counts) + '\n')
            f.close()
            #we need to take one extra data point at the last point and not step forward
            if i != number_of_steps:
                self.spectrometer.move(self.step, high_time = high, low_time = low)
                self.position.emit(self.spectrometer.position + self.step)


        self.finished.emit()#emit that we're done
