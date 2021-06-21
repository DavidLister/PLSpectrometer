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

        # current value for Planck's constant converted to eV.s
        eV_J = 1.602176634e-19
        h_Js = 6.626070153e-34
        h_eVs = h_Js/eV_J

        # photon energy in eV/nm
        eVnm = h_eVs*299792458*1e9

        file = self.filepath

        if file == '':
            print('No input.')
            print()
            sys.exit()

        data = np.genfromtxt(file,skip_header=4,delimiter = '\t')


        fig = make_subplots(rows=2,cols=1)

        fig.add_trace(go.Scatter(x=data[:,0],y=data[:,1],mode='markers',name='(nm)'),row=1,col=1)
        fig.add_trace(go.Scatter(x=eVnm/data[:,0]*1e3,y=data[:,1],mode='markers',name='(meV)'),row=2,col=1)

        fig.update_xaxes(title_text='Wavelength (nm)',row=1,col=1)
        fig.update_xaxes(title_text='Energy (meV)',row=2,col=1)

        fig.update_yaxes(title_text='Intensity (counts/s)',row=1,col=1)
        fig.update_yaxes(title_text='Intensity (counts/s)',type="log",row=2,col=1)

        fig.update_layout(title_text=open(file).readline(),showlegend=False)

        fig.write_html('tmp.html',auto_open=True)

        print()
        self.finished.emit()
