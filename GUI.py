#THIS IS THE UI FILE IT FEEDS THE INPUTS TO THE SPECTROMETER
#IF YOU WISH TO CHANGE THE BEHAVIOUR OF THE SPECTROMETER EDIT 'spectrometer.py'
#IF YOU WISH TO CHANGE THE WAY DATA IS INPUTED THROUGH THE UI EDIT HERE OR USE
#'spectrometer.ui' WITH QTDESIGNER AND COMPILE THE UI TO 'qt_designer.py'

from qt_designer_new import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from spectrometer import Double, Single
import time
from graphing import BarChartView, View
from searchUI import SearchUI
from workers.move import moveWorker
from workers.scan import scanWorker
from workers.optimize import optimizeWorker
from PyQt5.QtCore import QObject, QThread, pyqtSignal




#the main windowclass that will be made it inherits from the widget MainWindow
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #run the init mathod of the parent class (MainWindow)
        self.ui = Ui_MainWindow() #initiate an instance of the compiled qt designer class
        self.ui.setupUi(self) #run the setup method to create the window
        self.connect_buttons() #connect all the buttons
        self.make_tabs() #add the plots to the UI
        self.double = Double('Dev2') #initialize the double spectrometer
        self.single = Single('Dev3') #initialize the single spectrometer
        self.add_optimize_bar()
        self.ui.current_wavelength_lbl.setText('Position (nm): '+str(self.double.position))#display the current position
        self.autoscale_lbls() #autoscale the labels so they don't cut off
        print('done init')



    #method for adjusting the labels so they are consistent between machines
    #I think this might be uneccesary
    def autoscale_lbls(self):
        self.ui.position_lbl.adjustSize()
        self.ui.current_wavelength_lbl.adjustSize()
        self.ui.literature_value_lbl.adjustSize()
        self.ui.measured_value_lbl.adjustSize()
        self.ui.current_position_lbl.adjustSize()
        self.ui.offset_lbl.adjustSize()
        self.ui.corrected_lbl.adjustSize()
        self.ui.move_spectrometer_lbl.adjustSize()
        self.ui.go_to_lbl.adjustSize()
        self.ui.scan_start_lbl.adjustSize()
        self.ui.scan_end_lbl.adjustSize()
        self.ui.perform_scan_lbl.adjustSize()
        self.ui.scan_step_lbl.adjustSize()
        self.ui.file_name_lbl.adjustSize()
        self.ui.sample_id_lbl.adjustSize()
        self.ui.count_time_lbl.adjustSize()
        self.ui.spect_select_lbl.adjustSize()

    # connect all the buttons to their functions
    def connect_buttons(self):
        self.ui.recalibrate_button.clicked.connect(self.recalibrate)
        self.ui.scan_button.clicked.connect(self.scan)
        self.ui.move_button.clicked.connect(self.move)
        self.ui.radioButton.setChecked(True)#default to the double spectrometer
        self.ui.abort_button.clicked.connect(self.abort)
        self.ui.shutter_btn.clicked.connect(self.shutter)
        self.ui.radioButton.toggled.connect(self.switch_spectrometer)
        self.ui.optimize_btn.clicked.connect(self.optimize)
        self.ui.optimize_stp_btn.clicked.connect(self.abort)

    #makes and positions the optimize bar
    def add_optimize_bar(self):
        self.count_display = BarChartView(self.ui.centralwidget)
        self.count_display.setGeometry(310,810,75,130)
        self.count_display.refresh_stats(1030)

    #constructs and positions the tabs
    def make_tabs(self):
        tabs = qtw.QTabWidget(self.ui.centralwidget)
        #first tab creation
        self.wavelength_frame = qtw.QFrame()
        layout = qtw.QVBoxLayout()
        self.wavelength_plot = View(name = 'Wavelength')
        layout.addWidget(self.wavelength_plot)
        self.wavelength_plot_log = View(name = 'Log', log = True)
        layout.addWidget(self.wavelength_plot_log)
        self.wavelength_frame.setLayout(layout)
        tabs.addTab(self.wavelength_frame, 'Wavelength')
        #second tab creation
        self.energy_frame = qtw.QFrame()
        layout = qtw.QVBoxLayout()
        self.energy_plot = View(name = 'Energy')
        layout.addWidget(self.energy_plot)
        self.energy_plot_log = View(name = 'Log', log = True)
        layout.addWidget(self.energy_plot_log)
        self.energy_frame.setLayout(layout)
        tabs.addTab(self.energy_frame, 'Energy')
        #adding the SearchUI
        tabs.addTab(SearchUI(),'Search')
        #set size and shape
        tabs.setGeometry(400,0,1000,1000)

    #update the 4 plots with data
    def update_plots(self,data):
        wavelength = data[0]
        counts = data[1]
        self.wavelength_plot.refresh_stats(wavelength,counts)
        self.wavelength_plot_log.refresh_stats(wavelength,counts)

        energy_x = 1239841.984/(1.000289*wavelength)
        self.energy_plot.refresh_stats(energy_x,counts)
        self.energy_plot_log.refresh_stats(energy_x,counts)

    def switch_spectrometer(self):
        if self.ui.radioButton.isChecked():
            self.ui.current_wavelength_lbl.setText('Position (nm): '+str(self.double.position))
            self.autoscale_lbls()
        else:
            self.ui.current_wavelength_lbl.setText('Position (nm): '+str(self.single.position))
            self.autoscale_lbls()

    #update the spectrometer position and display
    def update_position_dbl(self,position):
        position = round(position, 3)
        self.double.position = position
        if self.ui.radioButton.isChecked():#only update the display with double if double is selected
            current = self.ui.current_wavelength_lbl.text()
            keep = current[:current.find(':')+2]
            new_string = keep + str(position)
            self.ui.current_wavelength_lbl.setText(new_string)
            self.ui.current_wavelength_lbl.adjustSize()

    #update the spectrometer position and display
    def update_position_sngl(self,position):
        position = round(position, 3)
        self.single.position = position
        if not self.ui.radioButton.isChecked():#only update the display with double if single is selected
            current = self.ui.current_wavelength_lbl.text()
            keep = current[:current.find(':')+2]
            new_string = keep + str(position)
            self.ui.current_wavelength_lbl.setText(new_string)
            self.ui.current_wavelength_lbl.adjustSize()

    #changes the status displayed in the top left corner
    def change_status(self, status = 'Idle'):
        self.ui.status_lbl.setText('Status: ' + status)

    #function that sets the buttons to enabled, to be called after
    #a scan or a move (connected to the finished of the Thread)
    def enable_buttons(self):
        self.ui.recalibrate_button.setEnabled(True)
        self.ui.move_button.setEnabled(True)
        self.ui.scan_button.setEnabled(True)
        self.ui.optimize_btn.setEnabled(True)
        self.ui.optimize_stp_btn.setEnabled(True)

    #disable buttons
    def disable_buttons(self):
        self.ui.recalibrate_button.setEnabled(False)
        self.ui.move_button.setEnabled(False)
        self.ui.scan_button.setEnabled(False)
        self.ui.optimize_btn.setEnabled(False)
        self.ui.optimize_stp_btn.setEnabled(False)

    #shutter function
    def shutter(self):
        if self.ui.shutter_btn.isChecked():
            self.double.close_shutter()
            self.ui.shutter_btn.setText('Shutter Closed')
        else:
            self.double.open_shutter()
            self.ui.shutter_btn.setText('Shutter Opened')

    #repeats the scan if repeat is checked
    def check_repeat(self):
        if self.ui.repeat_btn.isChecked():
            self.scan()

    def scan(self):
        try:
            #read data from the input boxes
            start = float(self.ui.scan_start_input.text())
            end = float(self.ui.scan_end_input.text())
            step_input = float(self.ui.scan_step_input.text())
            step = round(step_input, 3) # Rounded to 0.001 nm to avoid systematic rounding error with pulse counts
            time = float(self.ui.count_time_input.text())
            filename = self.ui.file_name_input.text()
            sample_id = self.ui.sample_ID_input.text()
        except:
            print('scan did not recieve valid inputs')
            return




        #set the range and clear the data from plots
        self.wavelength_plot.set_xlim(start,end)
        self.wavelength_plot_log.set_xlim(start,end)
        energy_start = 1239841.984/(1.000289 * end)
        energy_end = 1239841.984/(1.000289 * start)
        print(energy_start)
        print(energy_end)
        self.energy_plot.set_xlim(energy_start,energy_end)
        self.energy_plot_log.set_xlim(energy_start,energy_end)
        self.wavelength_plot.cla()
        self.energy_plot.cla()
        self.wavelength_plot_log.cla()
        self.energy_plot_log.cla()

        # Step 2: Create a QThread object
        self.scan_thread = QThread()
        # Step 3: Create a worker object
        if self.ui.radioButton.isChecked():#if we have double selected
            if abs(end - self.double.position) > 100:#safety measure
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = scanWorker(self.double,start,end,step,time,filename,sample_id)#input double
            self.worker.position.connect(self.update_position_dbl)


        else:#if single is selected
            if abs(end - self.single.position) > 100:
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = scanWorker(self.single,start,end,step,time,filename,sample_id)#input single
            self.worker.position.connect(self.update_position_sngl)

        #disable the buttons to prevent crashing
        self.disable_buttons()
        self.change_status('Scanning')

        # # Step 4: Move worker to the thread
        self.worker.moveToThread(self.scan_thread)#this makes the scan_thread methos be executed by the thread
        # # Step 5: Connect signals and slots
        self.scan_thread.started.connect(self.worker.scan)#connect to the scan method
        self.worker.data.connect(self.update_plots)#update the plots as we take data
        self.worker.finished.connect(self.scan_thread.quit)#quit when done
        self.worker.finished.connect(self.worker.deleteLater)#delete when done
        self.worker.finished.connect(self.enable_buttons)#enable buttons when done
        self.worker.finished.connect(self.change_status)
        self.scan_thread.finished.connect(self.scan_thread.deleteLater)#delete the thread when done
        self.scan_thread.finished.connect(self.check_repeat)


        #start the thread
        self.scan_thread.start()



    def move(self):
        try:
            destination = float(self.ui.move_input.text())
        except:
            print('move recieved invalid input')
            return

        print('starting move to',destination)

        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        if self.ui.radioButton.isChecked():#if we have double selected
            if abs(destination - self.double.position) > 100:#safety measure
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = moveWorker(self.double,destination)#input double
            self.worker.position.connect(self.update_position_dbl)

        else:#if single is selected
            if abs(destination - self.single.position) > 100:
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = moveWorker(self.single,destination)#input single
            self.worker.position.connect(self.update_position_sngl)

        #disable the buttons to prevent crashing
        self.disable_buttons()
        self.change_status('Moving')
        # # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # # Step 5: Connect signals and slots see scan fordetailed documentation
        self.thread.started.connect(self.worker.move)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enable_buttons)
        self.worker.finished.connect(self.change_status)
        self.thread.finished.connect(self.thread.deleteLater)
        # # Step 6: Start the thread
        self.thread.start()

    def optimize(self):

        self.thread = QThread()
        self.worker = optimizeWorker(self.double)#input single
        #disable the buttons to prevent crashing
        self.disable_buttons()
        self.ui.optimize_stp_btn.setEnabled(True)
        # # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # # Step 5: Connect signals and slots see scan fordetailed documentation
        self.thread.started.connect(self.worker.optimize)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enable_buttons)
        self.worker.finished.connect(self.change_status)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.bar_update.connect(self.count_display.refresh_stats)
        # # Step 6: Start the thread
        self.thread.start()

    def recalibrate(self):
        try:
            literature = float(self.ui.literature_value_input.text())
            measured = float(self.ui.measured_value_input.text())
            current_position = float(self.ui.current_position_input.text())
            offset = round(-(measured - literature), 3)
            corrected_position = current_position + offset
        except:
            print('the recalibrate input was invalid')
            return

        if self.ui.radioButton.isChecked():
            self.double.recalibrate(corrected_position)
        else:
            self.single.recalibrate(corrected_position)

        self.ui.offset_lbl.setText("Offset (nm): " + f"{offset}")
        self.ui.corrected_lbl.setText("Corrected Position (nm): " + f"{corrected_position}")
        self.ui.offset_lbl.adjustSize()
        self.ui.corrected_lbl.adjustSize()

        current = self.ui.current_wavelength_lbl.text()
        keep = current[:current.find(':')+2]
        new_string = keep + str(corrected_position)
        self.ui.current_wavelength_lbl.setText(new_string)
        self.ui.current_wavelength_lbl.adjustSize()

        print('succesfully recalibrated')

    #the message box that pops up when requestion a move of over 100
    def check_intent(self):
        check = QMessageBox()
        check.setText("you have requested to move over 100nm is this correct")
        check.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        check.setIcon(QMessageBox.Warning)
        check = check.exec()

        if check == QMessageBox.Yes:
            return True
        else:
            return False

    #this overwrites the close button of the UI
    def closeEvent(self,event):
        close = QMessageBox()
        close.setText("Are you sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            #do the close procedure
            self.double.save()
            self.single.save()
            self.double.close_channels()
            self.single.close_channels()
            event.accept()
        else:
            event.ignore()


    def abort(self):
        #changes the abort flag inside the worker to be true which will trigger
        #abort on next scan step, cannot currently abort a move
        self.worker.abort = True




#run the UI
if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv) #makes the app
    win = MainWindow() #make our UI
    win.show() #display our UI
    sys.exit(app.exec_()) #executes the app
