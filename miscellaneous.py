# miscellaneous.py
#
# Defines functions for sleep, checking file names, making headers for files and calculating temperature
# Created by Elliot Wadge
# Edited by Alistair Bevan
# June 2023
#

import os
import time
from datetime import datetime
import numpy as np


# High precision sleep function (from testing on syzygy, accurate to about 1e-6)
def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()


# Checks if filename is available to avoid overwriting data (returns best name)
def available_name(filename):
    depth =  0

    while os.path.exists(filename):
        dot = filename.find('.')
        
        if dot == -1:  # If there is no dot, do this
            if depth == 0:
                filename = f"{filename} (1)"
            else:
                filename = f"{filename[:filename.rfind('(')+1]}{depth+1})"
                print(filename)
                
        else:  # If there is a dot, do this
            if depth == 0:
                filename = f"{filename[:dot]} ({depth+1}){filename[dot:]}"  # Add the brackets and number before the dot
            else:
                filename = f"{filename[:filename.rfind('(')+1]}{depth+1}{filename[filename.rfind(')'):]}"  # Replace the number

        depth += 1

    return filename


# Makes the file header, which takes f as in f = open(filename, 'w'), the sample ID and the count time
def make_header(f, sample_id, time_avg):
    f.write(f'Sample ID:\t\t{sample_id}\n')
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f.write(f'Start Time:\t\t{dt_string}\n')
    f.write(f'Averaging Time (s):\t\t{time_avg}\n\n')


# For finding the the minimum distance in cursors
def find_minimum(xdata, ydata, cmpr_x, cmpr_y):
    if len(xdata) == 0:
        return None
    minimum = cmpr_x**2 + cmpr_y**2  # Set a baseline minimum
    min_i = 0
    for i in range(len(xdata)):
        distance = (cmpr_x - xdata[i])**2 + (cmpr_y - ydata[i])**2
        if distance < minimum:
            minimum = distance
            min_i = i
    return min_i  # Returns the index that this happens at (not the value)


# Define equations for determining thermistor resistance and temperature

# Set known values
output_voltage_V = 5
resistor_resistance_ohms = 4700
resistance_ref_ohms = 8500

# Precompute constant terms
ABCD = [3.354016E-03, 2.569850E-04, 2.620131E-06, 6.383091E-08] # for ordered thermistor

# Vectorized function for determining resistance of thermistor
def therm_res_calc_ohms(thermistor_voltage_V):
    return (resistor_resistance_ohms * thermistor_voltage_V) / (output_voltage_V - thermistor_voltage_V)

# Vectorized function for determining temperature
def temp_calc_K(resistance_ohms):
    return (ABCD[0] + ABCD[1] * np.log(resistance_ohms / resistance_ref_ohms) +
            ABCD[2] * (np.log(resistance_ohms / resistance_ref_ohms))**2 +
            ABCD[3] * (np.log(resistance_ohms / resistance_ref_ohms))**3)**(-1) - 273.15
