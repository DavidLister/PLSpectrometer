# measurement.py
#
# Code for taking measurements and saving data with the thermistor temperature sensor
# Alistair Bevan
# June 2023
#

import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import datetime
import time
import random as rng
from PyQt5.QtCore import QThread, pyqtSignal

from temperature_calculator import therm_res_calc_ohms, temp_calc_K


# Create a thread for data acquisition
class MeasurementThread(QThread):
    measurement_ready = pyqtSignal(float, float, float, float)

    def __init__(self, interval):
        super().__init__()
        self.interval = interval
        self.stop_flag = False
        self.temperature_data = []  # Initialize temperature data as an instance variable
        self.voltage_data = []  # Initialize resistor voltage data as an instance variable

    def run(self):
        filename = f"C:/Users/mocvd/Documents/Temperature Sensor/Data/{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        header = "Elapsed Time (s)\tTemperature (°C)\tAverage Temperature (°C)\n"
        start_time = datetime.datetime.now()

        with nidaqmx.Task() as task_write, nidaqmx.Task() as task_read:
            task_write.ao_channels.add_ao_voltage_chan('Dev1/ao0', 'mychannel', min_val=0, max_val=5.0)
            task_read.ai_channels.add_ai_voltage_chan('Dev1/ai0', terminal_config=TerminalConfiguration.RSE, min_val=0, max_val=5)
            task_write.write(5.0)

            while not self.stop_flag:
                elapsed_time_s = round((datetime.datetime.now() - start_time).total_seconds(), 2)
                temperature_sum = 0.0
                voltage_sum = 0.0
                num_measurements = 0

                # Collect temperature measurements every second during the interval
                for _ in range(int(self.interval*10)):
                    voltage_V = round(task_read.read(), 5)  # rng.uniform(40, 42)  # For debugging
                    voltage_sum += voltage_V
                    
                    resistance_ohms = round(therm_res_calc_ohms(voltage_V), 5)
                    temperature_C = round(temp_calc_K(resistance_ohms), 3)
                    temperature_sum += temperature_C
                    num_measurements += 1

                    # Sleep for 1 second
                    time.sleep(0.085)

                # Calculate the average temperature and voltage
                average_voltage = voltage_sum / num_measurements
                self.voltage_data.append((average_voltage))  # Append temperature data to instance variable
                average_temperature = temperature_sum / num_measurements
                self.temperature_data.append((elapsed_time_s, average_temperature))  # Append temperature data to instance variable

                # Calculate the overall simple moving average
                if len(self.temperature_data) >= 5:
                    last_five_temperatures = [temp for _, temp in self.temperature_data[-5:]]
                    overall_average = sum(last_five_temperatures) / len(last_five_temperatures)
                else:
                    overall_average = temperature_C

                # Save temperature data to a text file
                with open(filename, "a") as file:
                    if file.tell() == 0:  # Check if the file is empty
                        file.write(header)  # Write the header only if the file is empty
                    file.write(f"{elapsed_time_s:.2f}\t{average_temperature:.2f}\t{overall_average:.2f}\n")  # Record elapsed time, temperature, and overall average with specified decimal places

                min_temperature = min(self.temperature_data, key=lambda x: x[1])[1]
                max_temperature = max(self.temperature_data, key=lambda x: x[1])[1]

                # Emit the temperature value
                self.measurement_ready.emit(average_temperature, min_temperature, max_temperature, average_voltage)

    def stop(self):
        self.stop_flag = True