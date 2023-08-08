# search.py
#
# Searches for and plots data (used in the search tab in the main GUI)
# Created by Elliot Wadge and Colton Lohn
# Edited by Alistair Bevan
# August 2023
#

import sys
import os
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class searchWorker(QObject):
    sample = pyqtSignal(str, str)
    finished = pyqtSignal()

    def __init__(self, name, year):
        super().__init__()
        self.name = name
        self.year = year

    def search(self):
        home_dir = os.path.expanduser('~')  # This is just C:\Users\user-name
        # absolute = os.path.join(home_dir, 'Documents', 'PL', 'Data')  # Searches in documents
        absolute = os.path.join(home_dir, 'Simon Fraser University (1sfu)', 'Simon Watkins - MOCVD-LAB', 'data', 'ZnO', 'PL', 'Data')  # Searches in OneDrive

        if self.name == '':
            self.finished.emit()
            return

        if self.year == '':
            print('Searching all...')
        else:
            print('Searching ' + self.year + '...')

        found = False

        for subdir, dirs, files in os.walk(absolute):
            if self.year in subdir:
                for file in files:
                    f = open(os.path.join(subdir, file))
                    try:
                        line = f.readline()
                        f.close()
                        if self.name in line or self.name in os.path.join(subdir, file):
                            found = True
                            self.sample.emit(os.path.join(subdir, file), line)  # Emits the file location and sample ID information

                    except UnicodeDecodeError:
                        continue
                    f.close()

        if not found:
            self.sample.emit("", "No match found.")

        self.finished.emit()
