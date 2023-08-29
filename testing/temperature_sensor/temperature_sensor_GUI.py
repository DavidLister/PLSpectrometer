# temperature_sensor_GUI.py
#
# Thermistor temperature sensor GUI
# Alistair Bevan
# June 2023
#

from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QMessageBox
import nidaqmx
from nidaqmx.constants import TerminalConfiguration

from qtdesigner_temperature_sensor import Ui_TemperatureSensor
from measurement import MeasurementThread


# Create Application
class MainWindow(qtw.QMainWindow):
    interval = 1  # Default interval value, in seconds

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_TemperatureSensor()
        self.ui.setupUi(self)
        self.connect_buttons()  # Connect all buttons
        self.measurement_thread = None

    # Connect all the buttons
    def connect_buttons(self):
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.stop_button.clicked.connect(self.stop_button_clicked)
        self.ui.refresh_button.clicked.connect(self.refresh_button_clicked)

    # Start temperature measurements
    def start_button_clicked(self):
        try:
            with nidaqmx.Task() as task_check:
                task_check.ai_channels.add_ai_voltage_chan('Dev1/ai0', terminal_config=TerminalConfiguration.RSE, min_val=0, max_val=5)
        except nidaqmx.errors.DaqError as e:
            error_message = "DAQ device not detected or configured properly."
            QMessageBox.critical(self, "Error", error_message, QMessageBox.Ok)
            return
    
        interval = self.interval
        self.measurement_thread = MeasurementThread(interval)
        self.measurement_thread.measurement_ready.connect(self.update_temperature)
        print("Measurement thread created")
        self.measurement_thread.start()
        print("Measurement thread started")
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.ui.refresh_button.setEnabled(False)

    # Stop temperature measurements
    def stop_button_clicked(self):
        print("Stop button clicked")
        if self.measurement_thread is not None:
            self.measurement_thread.stop()
            self.measurement_thread.wait()
            self.measurement_thread = None
            self.ui.start_button.setEnabled(True)
            self.ui.stop_button.setEnabled(False)
            self.ui.refresh_button.setEnabled(True)
            print("Measurement thread stopped")
        else:
            print("No measurement thread is running")

    # Refresh the interval
    def refresh_button_clicked(self):
        interval_str = self.ui.interval_input.text()
        self.ui.temperature_output.setText(" ")
        self.ui.range_output.setText(" ")

        try:
            interval = float(interval_str)
            if not 1 <= interval <= 10 or not interval.is_integer() or interval <= 0:
                raise ValueError("Interval value must be a positive whole number between 1 and 10 seconds.")
            print("Interval refreshed:", interval)
            self.interval = int(interval)  # Update the class attribute as an integer
        except ValueError:
            error_message = "Please enter a positive whole number between 1 and 10 seconds."
            QMessageBox.critical(self, "Error", error_message, QMessageBox.Ok)
            self.ui.interval_input.setText(str(self.interval))  # Reset the input box to the previous value

        # Update the GUI with the most recent temperature values
    def update_temperature(self, temperature, min_temperature, max_temperature, voltage):
        self.ui.temperature_output.setText(f"{temperature:.2f}")
        self.ui.range_output.setText(f"{min_temperature:.2f} - {max_temperature:.2f}")
        self.ui.voltage_output.setText(f"{voltage:.3f}")


if __name__ == "__main__":
    app = qtw.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()