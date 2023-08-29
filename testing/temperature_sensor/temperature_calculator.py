# temperature_calculator.py
#
# Defines equations for determining thermistor resistance and temperature
# Alistair Bevan
# June 2023
#

import numpy as np


# Set known values
output_voltage_V = 5
resistor_resistance_ohms = 4700
resistance_ref_ohms = 8500

# Precompute constant terms
ABCD = [3.354016E-03, 2.569850E-04, 2.620131E-06, 6.383091E-08] # for ordered thermistor
# ABCD = [3.354016E-03, 2.569355E-04, 2.626311E-06, 6.75278E-06] # for testing thermistor

# Define vectorized function for determining resistance of thermistor
def therm_res_calc_ohms(thermistor_voltage_V):
    return (resistor_resistance_ohms * thermistor_voltage_V) / (output_voltage_V - thermistor_voltage_V)

# Define vectorized function for determining temperature
def temp_calc_K(resistance_ohms):
    return (ABCD[0] + ABCD[1] * np.log(resistance_ohms / resistance_ref_ohms) +
            ABCD[2] * (np.log(resistance_ohms / resistance_ref_ohms))**2 +
            ABCD[3] * (np.log(resistance_ohms / resistance_ref_ohms))**3)**(-1) - 273.15