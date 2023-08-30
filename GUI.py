# GUI.py
#
# Main user interface (UI) file, which feeds inputs to the spectrometer
# Edit spectrometer.py to change the spectrometer behaviour
# Edit this file or the QtDesigner file in QtDesigner and compile to a python file to 
# change the way the data is inputed through the UI
# Created by Elliot Wadge
# Edited by Alistair Bevan
# August 2023
#

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
from workers.temperature import TemperatureSensor
from PyQt5.QtCore import QObject, QThread, pyqtSignal


# The main window class that will be made (it inherits from the widget MainWindow)
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Run the init method of the parent class (MainWindow)
        self.ui = Ui_MainWindow()  # Initiate an instance of the compiled qt designer class
        self.ui.setupUi(self)  # Run the setup method to create the window
        self.connect_buttons()  # Connect all the buttons
        self.make_tabs()  # Add the plots to the UI
        self.temperature_sensor = TemperatureSensor('Dev1')  # Initialize the temperature sensor
        self.double = Double('Dev2')  # Initialize the double spectrometer
        self.single = Single('Dev3')  # Initialize the single spectrometer
        self.add_optimize_bar()  # Add optimize bar graph to the UI
        self.ui.current_wavelength_lbl.setText('Position (nm): ' + str(self.double.position))  # Display the current position
        self.autoscale_lbls()  # Autoscale the labels so they don't cut off
        print('Done init')

    # Method for adjusting the labels so they are consistent between machines (this might be unnecessary)
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

    # Connect all the buttons to their functions
    def connect_buttons(self):
        self.ui.recalibrate_button.clicked.connect(self.recalibrate)
        self.ui.scan_button.clicked.connect(self.scan)
        self.ui.move_button.clicked.connect(self.move)
        self.ui.radioButton.setChecked(True)  # Default to the double spectrometer
        self.ui.abort_button.clicked.connect(self.abort)
        self.ui.shutter_btn.clicked.connect(self.shutter)
        self.ui.radioButton.toggled.connect(self.switch_spectrometer)
        self.ui.optimize_btn.clicked.connect(self.optimize)
        self.ui.optimize_stp_btn.clicked.connect(self.abort)

    # Makes and positions the optimize bar
    def add_optimize_bar(self):
        self.count_display = BarChartView(self.ui.centralwidget)
        self.count_display.setGeometry(310, 810, 75, 130)
        self.count_display.refresh_stats(1030)

    # Constructs and positions the tabs
    def make_tabs(self):
        tabs = qtw.QTabWidget(self.ui.centralwidget)
        # First tab creation
        self.wavelength_frame = qtw.QFrame()
        layout = qtw.QVBoxLayout()
        self.wavelength_plot = View(name = 'Wavelength')
        layout.addWidget(self.wavelength_plot)
        self.wavelength_plot_log = View(name = 'Log', log = True)
        layout.addWidget(self.wavelength_plot_log)
        self.wavelength_frame.setLayout(layout)
        tabs.addTab(self.wavelength_frame, 'Wavelength')
        # Second tab creation
        self.energy_frame = qtw.QFrame()
        layout = qtw.QVBoxLayout()
        self.energy_plot = View(name = 'Energy')
        layout.addWidget(self.energy_plot)
        self.energy_plot_log = View(name = 'Log', log = True)
        layout.addWidget(self.energy_plot_log)
        self.energy_frame.setLayout(layout)
        tabs.addTab(self.energy_frame, 'Energy')
        # Third tab creation (SearchUI)
        tabs.addTab(SearchUI(),'Search')
        # Set size and shape
        tabs.setGeometry(400, 0, 1000, 1000)

    # Update the 4 UI plots with data
    def update_plots(self, data):
        wavelength = data[0]
        counts = data[1]  # This is technically the count rate (in counts/s)
        self.wavelength_plot.refresh_stats(wavelength, counts)
        self.wavelength_plot_log.refresh_stats(wavelength, counts)

        energy_x = 1239841.984/(1.000289*wavelength)  # In meV and includes index of refraction correction (1.000289)
        self.energy_plot.refresh_stats(energy_x, counts)
        self.energy_plot_log.refresh_stats(energy_x, counts)

    def switch_spectrometer(self):
        if self.ui.radioButton.isChecked():
            self.ui.current_wavelength_lbl.setText('Position (nm): ' + str(self.double.position))
            self.autoscale_lbls()
        else:
            self.ui.current_wavelength_lbl.setText('Position (nm): ' + str(self.single.position))
            self.autoscale_lbls()

    # Update the spectrometer position and display (double)
    def update_position_dbl(self, position):
        position = round(position, 3)
        self.double.position = position
        if self.ui.radioButton.isChecked():  # Only update the display with double if double is selected
            current = self.ui.current_wavelength_lbl.text()
            keep = current[:current.find(':')+2]
            new_string = keep + str(position)
            self.ui.current_wavelength_lbl.setText(new_string)
            self.ui.current_wavelength_lbl.adjustSize()

    # Update the spectrometer position and display (single)
    def update_position_sngl(self, position):
        position = round(position, 3)
        self.single.position = position
        if not self.ui.radioButton.isChecked():  # Only update the display with single if single is selected
            current = self.ui.current_wavelength_lbl.text()
            keep = current[:current.find(':')+2]
            new_string = keep + str(position)
            self.ui.current_wavelength_lbl.setText(new_string)
            self.ui.current_wavelength_lbl.adjustSize()

    # Changes the status displayed in the top left corner
    def change_status(self, status = 'Idle'):
        self.ui.status_lbl.setText('Status: ' + status)

    # Sets buttons to enabled, which is called after
    # a scan or a move (connected to the finished of the Thread)
    def enable_buttons(self):
        self.ui.recalibrate_button.setEnabled(True)
        self.ui.move_button.setEnabled(True)
        self.ui.scan_button.setEnabled(True)
        self.ui.optimize_btn.setEnabled(True)
        self.ui.optimize_stp_btn.setEnabled(True)

    # Sets buttons to disabled
    def disable_buttons(self):
        self.ui.recalibrate_button.setEnabled(False)
        self.ui.move_button.setEnabled(False)
        self.ui.scan_button.setEnabled(False)
        self.ui.optimize_btn.setEnabled(False)
        self.ui.optimize_stp_btn.setEnabled(False)

    # Open and closes double spectrometer shutter
    def shutter(self):
        if self.ui.shutter_btn.isChecked():
            self.double.close_shutter()
            self.ui.shutter_btn.setText('Shutter Closed')
        else:
            self.double.open_shutter()
            self.ui.shutter_btn.setText('Shutter Opened')

    # Repeats the scan if repeat is checked
    def check_repeat(self):
        if self.ui.repeat_btn.isChecked():
            self.scan()

    def scan(self):
        # Step 1: Read data from the input boxes
        try:
            start = float(self.ui.scan_start_input.text())
            end = float(self.ui.scan_end_input.text())
            step_input = float(self.ui.scan_step_input.text())
            step = round(step_input, 3)  # Rounded to 0.001 nm to avoid systematic rounding error with pulse counts
            time = float(self.ui.count_time_input.text())
            filename = self.ui.file_name_input.text()
            sample_id = self.ui.sample_ID_input.text()
        except:
            print('Scan did not recieve valid inputs')
            return

        # Step 2: Set the range and clear the data from plots
        self.wavelength_plot.set_xlim(start, end)
        self.wavelength_plot_log.set_xlim(start, end)
        energy_start = 1239841.984/(1.000289 * end)  # In meV and includes index of refraction correction (1.000289)
        energy_end = 1239841.984/(1.000289 * start)
        print(energy_start)
        print(energy_end)
        self.energy_plot.set_xlim(energy_start, energy_end)
        self.energy_plot_log.set_xlim(energy_start, energy_end)
        self.wavelength_plot.cla()
        self.energy_plot.cla()
        self.wavelength_plot_log.cla()
        self.energy_plot_log.cla()

        # Step 3: Create a QThread object
        self.scan_thread = QThread()

        # Step 4: Create a worker object
        if self.ui.radioButton.isChecked():  # If double is selected
            if abs(end - self.double.position) > 100:  # Safety measure
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = scanWorker(self.double, start, end, step, time, filename, sample_id)  # Input double
            self.worker.position.connect(self.update_position_dbl)

        else:  # If single is selected
            if abs(end - self.single.position) > 100:
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = scanWorker(self.single, start, end, step, time, filename, sample_id)  # Input single
            self.worker.position.connect(self.update_position_sngl)

        self.disable_buttons()  # Disable the buttons to prevent crashing
        self.change_status('Scanning')

        # # Step 5: Move worker to the thread
        self.worker.moveToThread(self.scan_thread)  # This makes the scan_thread method be executed by the thread

        # # Step 6: Connect signals and slots
        self.scan_thread.started.connect(self.worker.scan)  # Connect to the scan method
        self.worker.data.connect(self.update_plots)  # Update the plots as we take data
        self.worker.finished.connect(self.scan_thread.quit)  # Quit when done
        self.worker.finished.connect(self.worker.deleteLater)  # Delete when done
        self.worker.finished.connect(self.enable_buttons)  # Enable buttons when done
        self.worker.finished.connect(self.change_status)
        self.scan_thread.finished.connect(self.scan_thread.deleteLater)  # Delete the thread when done
        self.scan_thread.finished.connect(self.check_repeat)

        # Start the thread
        self.scan_thread.start()

    def move(self):
        # Step 1: Read data from the input box
        try:
            destination_input = float(self.ui.move_input.text())
            destination = round(destination_input, 3)
        except:
            print('Move recieved invalid input')
            return

        print('Starting move to', destination)

        # Step 2: Create a QThread object
        self.thread = QThread()

        # Step 3: Create a worker object
        if self.ui.radioButton.isChecked():  # If double is selected
            if abs(destination - self.double.position) > 100:  # Safety measure
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = moveWorker(self.double,destination)  # Input double
            self.worker.position.connect(self.update_position_dbl)

        else:  # If single is selected
            if abs(destination - self.single.position) > 100:
                intent = self.check_intent()
                if not intent:
                    return
            self.worker = moveWorker(self.single,destination)  # Input single
            self.worker.position.connect(self.update_position_sngl)

        self.disable_buttons()  # Disable the buttons to prevent crashing
        self.change_status('Moving')

        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)

        # Step 5: Connect signals and slots (see scan for detailed documentation)
        self.thread.started.connect(self.worker.move)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enable_buttons)
        self.worker.finished.connect(self.change_status)
        self.thread.finished.connect(self.thread.deleteLater)

        # # Step 6: Start the thread
        self.thread.start()

    def optimize(self):
        # Step 1: Create a QThread object
        self.thread = QThread()
        self.worker = optimizeWorker(self.double)  # Input double
        self.disable_buttons()  # Disable the buttons to prevent crashing
        self.ui.optimize_stp_btn.setEnabled(True)

        # Step 2: Move worker to the thread
        self.worker.moveToThread(self.thread)

        # Step 3: Connect signals and slots (see scan for detailed documentation)
        self.thread.started.connect(self.worker.optimize)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enable_buttons)
        self.worker.finished.connect(self.change_status)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.bar_update.connect(self.count_display.refresh_stats)

        # Step 6: Start the thread
        self.thread.start()

    def recalibrate(self):  # Includes calculation for determining difference between expected ("literature") and actual position
        # Check for valid inputs
        try:
            literature = float(self.ui.literature_value_input.text())
            measured = float(self.ui.measured_value_input.text())
            current_position = float(self.ui.current_position_input.text())
            offset = round(measured - literature, 3)
            corrected_position = round(current_position - offset, 3)
        except:
            print('The recalibrate input was invalid')
            error_message = "Recalibration cannot be performed due to invalid inputs. Please ensure there are numbers in each of the three input boxes."
            QMessageBox.critical(self, "Error", error_message, QMessageBox.Ok)
            return

        if self.ui.radioButton.isChecked():
            self.double.recalibrate(corrected_position)
        else:
            self.single.recalibrate(corrected_position)

        # Update offset and new position labels
        self.ui.offset_lbl.setText("Offset (nm): " + f"{offset}")
        self.ui.corrected_lbl.setText("Position After Correction (nm): " + f"{corrected_position}")
        self.ui.offset_lbl.adjustSize()
        self.ui.corrected_lbl.adjustSize()

        # Update current wavelength label
        current = self.ui.current_wavelength_lbl.text()
        keep = current[:current.find(':')+2]
        new_string = keep + str(corrected_position)
        self.ui.current_wavelength_lbl.setText(new_string)
        self.ui.current_wavelength_lbl.adjustSize()

        print('Succesfully recalibrated')

    # Message box that pops up when requestion a move of over 100
    def check_intent(self):
        check = QMessageBox()
        check.setText("You have requested to move over 100 nm. Is this correct?")
        check.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        check.setIcon(QMessageBox.Warning)
        check = check.exec()

        if check == QMessageBox.Yes:
            return True
        else:
            return False

    # This overwrites the close button of the UI
    def closeEvent(self,event):
        close = QMessageBox()
        close.setWindowTitle("Confirm Exit")
        close.setText("Are you sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            # Do the close procedure
            self.double.save()
            self.single.save()
            self.double.close_channels()
            self.single.close_channels()
            event.accept()
        else:
            event.ignore()


    def abort(self):
        # Changes the abort flag inside the worker to be true which will trigger
        # abort on next scan step (cannot currently abort a move)
        self.worker.abort = True



# Run the UI
if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv)  # Makes the app
    win = MainWindow()  # Makes our UI
    win.show()  # Displays our UI
    sys.exit(app.exec_())  # Executes the app
