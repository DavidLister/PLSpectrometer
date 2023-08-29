# temperature.py
#
# Code for taking measurements with the thermistor temperature sensor
# Alistair Bevan
# August 2023
#

import nidaqmx
from nidaqmx.constants import TerminalConfiguration
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
import time

from miscellaneous import therm_res_calc_ohms, temp_calc_K


# Create a class for temperature sensor
class TemperatureSensor:
    def __init__(self, device):
        self.device = device
        self.name = device
        
        super().__init__()
        try:
            with nidaqmx.Task() as task_check:
                task_check.ai_channels.add_ai_voltage_chan('Dev1/ai0', terminal_config=TerminalConfiguration.RSE, min_val=0, max_val=5)

        except:
            print(f'The device or channel name you entered for {device} may be incorrect or you may have an unclosed window running')
            print(f'You will be unable to send commands to this daq: {device}\n')
            return
        

    # Function for measuring temperature
    def read_temperature(self):
        try:
            with nidaqmx.Task() as task_read:
                task_read.ai_channels.add_ai_voltage_chan('Dev1/ai0', terminal_config=TerminalConfiguration.RSE, min_val=0, max_val=5)
        except:
            average_temperature = "N/A"
            return average_temperature

        with nidaqmx.Task() as task_write, nidaqmx.Task() as task_read:
            task_write.ao_channels.add_ao_voltage_chan('Dev1/ao0', 'mychannel', min_val=0, max_val=5.0)
            task_read.ai_channels.add_ai_voltage_chan('Dev1/ai0', terminal_config=TerminalConfiguration.RSE, min_val=0, max_val=5)
            task_write.write(5.0)

            temperature_sum = 0.0
            num_measurements = 0

            # Collect temperature measurements for averaging
            for _ in range(10):
                voltage_V = round(task_read.read(), 5)
        
                # Calculate temperature
                resistance_ohms = round(therm_res_calc_ohms(voltage_V), 5)
                temperature_C = round(temp_calc_K(resistance_ohms), 3)
                temperature_sum += temperature_C
                num_measurements += 1

                # Sleep for a short duration between measurements
                time.sleep(0.05)

            # Calculate the average temperature
            average_temperature = temperature_sum / num_measurements
            return average_temperature  # Return the calculated average temperature