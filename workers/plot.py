# plot.py
#
# Used by the searchUI tab (not for the main GUI plots)
# Created by Elliot Wadge and Colton Lohn
# Edited by Alistair Bevan
# August 2023
#

import sys
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class plotWorker(QObject):
    """docstring for plotWorker."""

    finished = pyqtSignal()

    def __init__(self,filepath):
        super().__init__()
        self.filepath = filepath

    def plot(self):

        # Current value for Planck's constant converted to eV s
        eV_J = 1.602176634e-19
        h_Js = 6.626070153e-34
        h_eVs = h_Js/eV_J

        # Photon energy in eV/nm
        eVnm = h_eVs*299792458*1e9

        # Index of refraction correction
        z = 1.000289

        file = self.filepath

        if file == '':
            print('No input.')
            print()
            sys.exit()

        # Get the file name and first line for graph title
        file_name = file.split('\\')[-1]
        with open(file, 'r') as f:
            first_line = f.readline().strip()

        # Import data
        data = np.genfromtxt(file, skip_header=4, delimiter = '\t')

        # Create the figures
        fig = make_subplots(rows=2, cols=1)

        fig.add_trace(go.Scatter(x=data[:,0], y=data[:,1], mode='markers', name='(nm)'), row=1, col=1)
        fig.add_trace(go.Scatter(x=eVnm/(data[:,0]*z)*1e3, y=data[:,1], mode='markers', name='(meV)'), row=2, col=1)

        fig.update_xaxes(title_text='Wavelength (nm)', row=1, col=1)
        fig.update_xaxes(title_text='Energy (meV)', row=2, col=1)

        fig.update_yaxes(title_text='Intensity (counts/s)', type="log", row=1, col=1)
        fig.update_yaxes(title_text='Intensity (counts/s)', type="log", row=2, col=1)

        fig.update_layout(title_text=f"{file_name}<br>{first_line}", showlegend=False)

        fig.write_html('tmp.html', auto_open=True)

        print()
        self.finished.emit()
