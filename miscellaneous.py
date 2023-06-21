# miscellaneous.py
#
# Defines functions for sleep, checking file names, and making headers for files
# Created by Elliot Wadge
# Edited by Alistair Bevan
# June 2023
#

import time
import os
from datetime import datetime


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
