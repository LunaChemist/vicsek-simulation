from src.box import Box
from src.plot import Window

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

app = QApplication(sys.argv)


box = Box()
window = Window()
window.show()

def update():
    box.updateDirections()
    box.updatePositions()
    window.updatePlot(box.getPointCoordinates())

timer = QTimer()
timer.timeout.connect(update)
timer.start(16)
sys.exit(app.exec())