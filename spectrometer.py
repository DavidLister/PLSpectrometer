# spectrometer.py
#
# Defines double and single spectrometer classes
# Created by Elliot Wadge
# Edited by Alistair Bevan
# July 2023
#

import nidaqmx
import math
import time
from nidaqmx.constants import AcquisitionType
from miscellaneous import sleep


class Double():

    '''The spectrometer class is where the signals are sent to and from the daq, and it
    also tracks the position of the spectrometer'''

    def __init__(self,device, shutter_prt = '/port1/line1', direction_prt = '/port1/line3'):
        # Open file where last position is stored (not necessarily in the PLSpectrometer folder, it could be under the user)
        try:
            f = open(device + '_last_position.txt', 'r')
            self._position = float(f.readline())
            f.close()
        except:
            print("There was an error trying to load the data from last_position.txt")
            self._position = 0.0
        else:
            print(self.position)
            print(f'Successfully loaded last position for {device}\n')

        # Makes testing easier since trying to access a channel that doesn't exist
        # or is in use will cause the program to crash
        try:
            self.shutter = nidaqmx.Task() # Task to control the shutter
            self.shutter.do_channels.add_do_chan(device + shutter_prt)
            self.shutter.start()

            self.direction = nidaqmx.Task()
            self.direction.do_channels.add_do_chan(device + direction_prt)
            self.direction.start()

        except:
            print(f'The device or channel name you entered for {device} may be incorrect or you may have an unclosed window running')
            print(f'You will be unable to send commands to this daq: {device}\n')

        self.name = device
        self.frequency = 2000 # Frequency of pulses generated

    # Getter method which allows us to sanitize the inputs while keeping the syntax neat
    # Google @property for reasoning
    @property
    def position(self):
        return self._position

    # Setter method related to @property
    # IMPORTANT TO UNDERSTAND WHAT THIS DOES
    @position.setter
    def position(self, wavelength):
        # Check these conditons before accepting a value when assigning a value to position
        if isinstance(wavelength, float) and wavelength >= 0 and wavelength < 1040:
            self._position = wavelength
        else: # Will crash the program thus stopping the scan (can't stop a move)
            raise ValueError("Spectrometer position must be between 0 and 1040.")
        return

    def open_shutter(self):
        # Set voltage to zero
        self.shutter.write(False)

    def close_shutter(self):
        # Set voltage to 5
        self.shutter.write(True)

    # Sets the direction of the move to be called before the move
    def set_direction(self, direction):
        if direction > 0:
            self.direction.write(True)
        else:
            self.direction.write(False)

    # Save the last position to a file
    def save(self):
        try:
            f = open(self.name + '_last_position.txt', 'w')
            f.write(str(self.position))
            f.close()
        except:
            print(f'There was an error writing to {self.name}_last_position.txt')
        else:
            print(self.position)
            print(f'Position of {self.name} saved')

    def move(self, distance, **kwargs):
        # Passing zero pulses to the channnel will cause an error
        if distance == 0:
            return
        # Calculate the amount of pulses given 4 pulses equal 0.001 nm of movement
        pulse_count = int(distance * 4000)
        print(pulse_count)
        # Ensures that the task is closed properly when done
        with nidaqmx.Task() as task:
            # Can't have two counter channels at once (co or ci), so important that this is closed
            task.co_channels.add_co_pulse_chan_time(self.name + "/ctr0", **kwargs)
            # AcquisitionType.FINITE changes the mode to send a set number of pulses
            # Samps per chan is the number of pulses to send
            task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE, samps_per_chan=pulse_count)
            task.start()
            task.wait_until_done(timeout = math.inf) # Need to wait until done before continuing
        print('Done')

    def read(self, count_time):
        with nidaqmx.Task() as task:
             task.ci_channels.add_ci_count_edges_chan(self.name +"/ctr0") # Start a count channel
             task.ci_channels[0].ci_count_edges_term = '/'+self.name+'/PFI0' # Set the terminal
             task.start() # Start counting
             sleep(count_time) # Wait the count time
             data = task.read() # Read the counts
        return data/count_time # Return the average count/s

    # Changes the stored position
    def recalibrate(self, wavelength):
        self.position = wavelength

    # Closes the tasks properly upon closing the application
    def close_channels(self):
        try:
            # Sets the voltages to zero, since if not done daq will continue to ouput
            # This could be desirable, Elliot wasn't sure
            self.shutter.write(False)
            self.direction.write(False)
            self.shutter.stop()
            self.shutter.close()
            self.direction.stop()
            self.direction.close()
        except:
            print('There was an error when closing the tasks')
        else:
            print('Spectrometer closed')


# The single spectrometer class is the same but simpler
# Channels are different and directions are reversed
class Single():

    PMT_channel = 'Dev2/ctr0'
    PMT_terminal = '/Dev2/PFI0'

    def __init__(self,device, direction_prt = '/port2/line6'):
        # Open file where we will store the last position
        try:
            f = open(device + '_last_position.txt', 'r')
            self._position = float(f.readline())
            print(self.position)
            f.close()
        except:
            print("There was an error trying to load the data from last_position.txt")
            self._position = 0.0
        else:
            print(f'Successfully loaded last position for {device}\n')

        # Makes testing easier since trying to access a channel that doesn't exist
        # or is in use will cause the program to crash
        try:
            self.direction = nidaqmx.Task()
            self.direction.do_channels.add_do_chan(device + direction_prt)
            self.direction.start()

        except:
            print(f'The device or channel name you entered for {device} may be incorrect or you may have an unclosed window running')
            print(f'You will be unable to send commands to this daq: {device}\n')

        self.name = device
        self.frequency = 2000 # Frequency of pulses generated

    # Getter method which allows us to sanitize the inputs while keeping the syntax neat
    # Google @property for reasoning
    @property
    def position(self):
        return self._position

    # Setter method related to @property
    # IMPORTANT TO UNDERSTAND WHAT THIS DOES
    @position.setter
    def position(self, wavelength):
        # Check these conditons before accepting a value when assigning a value to position
        if isinstance(wavelength, float) and wavelength >= 0 and wavelength < 1550:
            self._position = wavelength
        else: # Will crash the program thus stopping the scan (can't stop a move)
            raise ValueError("Spectrometer position must be between 0 and 1550.")
        return

    # Sets the direction of the move to be called before the move
    def set_direction(self, direction):
        if direction > 0:
            self.direction.write(True)
        else:
            self.direction.write(False)

    def move(self, distance, **kwargs):
        # Passing zero pulses to the channnel will cause an error
        if distance == 0:
            return
        # Calculate the amount of pulses given 4 pulses equal 0.001 nm of movement
        pulse_count = int(distance * 4000)
        print(pulse_count)
        # Ensures that the task is closed properly when done
        with nidaqmx.Task() as task:
            # Can't have two counter channels at once (co or ci), so important that this is closed
            task.co_channels.add_co_pulse_chan_time(self.name + "/ctr0",**kwargs)
            # AcquisitionType.FINITE changes the mode to send a set number of pulses
            # Samps per chan is the number of pulses to send
            task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.FINITE, samps_per_chan=pulse_count)
            task.start()
            task.wait_until_done(timeout = math.inf) # Need to wait until done before continuing
        print('Done')

    # Needs to have a read function for the scan
    def read(self, count_time):
        with nidaqmx.Task() as task:
             task.ci_channels.add_ci_count_edges_chan(self.PMT_channel) # Start a count channel
             task.ci_channels[0].ci_count_edges_term = self.PMT_terminal # Set the terminal
             task.start() # Start counting
             sleep(count_time) # Wait the count time
             data = task.read() # Read the counts
        return data/count_time # Return the average count/s

    # Changes the stored position
    def recalibrate(self, wavelength):
        self.position = wavelength

    # Saves the last position
    def save(self):
        try:
            f = open(self.name + '_last_position.txt', 'w')
            f.write(str(self.position))
            f.close()
        except:
            print(f'There was an error writing to {self.name}_last_position.txt')
        else:
            print(self.position)
            print(f'Position of {self.name} saved')

    # Closes the tasks properly upon closing the application
    def close_channels(self):
        try:
            # Sets the voltages to zero, since if not done daq will continue to ouput
            # This could be desirable, Elliot wasn't sure
            self.direction.write(False)
            self.direction.stop()
            self.direction.close()
        except:
            print('There was an error when closing the tasks')
        else:
            print('Spectrometer closed')


if __name__ == '__main__':
    test = Spectrometer('Dev1')
    time.sleep(20)
