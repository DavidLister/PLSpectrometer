# search.py
#
# Searches for and plots data
# Created by Elliot Wadge
# Edited by Alistair Bevan
# August 2023
#

import sys
import os
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class searchWorker(QObject):
    sample = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, name, year):
        super().__init__()
        self.name = name
        self.year = year

    def search(self):
        home_dir = os.path.expanduser('~')  # This is just C:\Users\user-name
        # absolute = os.path.join(home_dir, 'Documents', 'PL', 'Data')  # Searches in documents
        absolute = os.path.join(home_dir, 'Simon Fraser University (1sfu)', 'Simon Watkins - MOCVD-LAB', 'data', 'ZnO', 'PL', 'Data')  # Searches in OneDrive

        i = self.name
        j = self.year

        if i == '':
            self.finished.emit()
            return

        if j == '':
            print('Searching all...')
        else:
            print('Searching ' + j + '...')

        found = False

        for subdir, dirs, files in os.walk(absolute):
            if j in subdir:
                for file in files:
                    f = open(os.path.join(subdir, file))
                    try:
                        line = f.readline()
                        f.close()
                        if i in line or i in os.path.join(subdir, file):
                            found = True
                            self.sample.emit(os.path.join(subdir, file) + '\n' + line)

                    except UnicodeDecodeError:
                        continue

        if not found:
            self.sample.emit('No match found')

        f.close()
        self.finished.emit()
