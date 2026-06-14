import pyqtgraph as pg
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout

from src.constants import constants

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setBackground("w")
        self.setCentralWidget(self.plotWidget)

        self.plotWidget.setXRange(0, constants["boxDimensions"])
        self.plotWidget.setYRange(0, constants["boxDimensions"])

        self.scatter = self.plotWidget.plot(
            [], [],
            pen=None,
            symbol="o"
        )

    def updatePlot(self, pointCoordinates: list[tuple[int, int]]):
        xPoints = [point[0] for point in pointCoordinates]
        yPoints = [point[1] for point in pointCoordinates]
        self.scatter.setData(xPoints, yPoints)