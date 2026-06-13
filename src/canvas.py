from src.constants import constants
from src.point import Point
import grispy as gsp
import numpy as np

class Canvas:
    """
    The canvas of the all the points of the simulation
    """
    def __init__(self) -> None:
        self.dimensions = constants["canvasDimensions"]  # Def as 0->L on both axis
        self.numberOfPoints = constants["numberOfPoints"]
        self.initiate()
        return

    # Start
    def initiate(self) -> None:
        """
        Adds the number of points to the canvas and runs a short equilibration
        """
        pointCoordinates = np.random.rand(self.numberOfPoints, 2) * self.dimensions  # Creates n points on the canvas
        self.points = [Point(coords) for coords in pointCoordinates]
        pass

    # Update
    def updateDirections(self) -> None:
        """
        Updates the direction of all the points on the canvas
        """
        distance, index = self.findFixedRadiusNeighbours()
        pass
    
    def findFixedRadiusNeighbours(self):
        pointCoordinates = np.array([(point.x, point.y) for point in self.points])
        periodicBoundaries = {
            0: (0, self.dimensions),  # X-axis
            1: (0, self.dimensions),  # Y-axis
        }

        grid = gsp.GriSPy(pointCoordinates, periodic=periodicBoundaries)
        distance, index = grid.bubble_neighbors(
            pointCoordinates, distance_upper_bound=constants["influenceRadius"]
        )
        return distance, index

    def updatePositions(self) -> None:
        """
        Updates the position of all the points on the canvas
        """
        for point in self.points:
            point.updatePosition()
        return
    
    # Get

    def getPointCoordinates(self):
        return [(point.x, point.y) for point in self.points]