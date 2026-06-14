from src.constants import constants
from src.point import Point
import grispy as gsp
import numpy as np

class Box:
    """
    The box of the all the points of the simulation
    """
    def __init__(self) -> None:
        self.dimensions = constants["boxDimensions"]  # Def as 0->L on both axis
        self.numberOfPoints = constants["numberOfPoints"]
        self.initiate()
        return

    # Start
    def initiate(self) -> None:
        """
        Adds the number of points to the box and runs a short equilibration
        """
        pointCoordinates = np.random.rand(self.numberOfPoints, 2) * self.dimensions  # Creates n points on the box
        self.points = [Point(coords) for coords in pointCoordinates]
        pass

    # Update
    def updateDirections(self) -> None:
        """
        Updates the direction of all the points on the box
        """
        pointCoordinates = self.getPointCoordinates()
        pointDirections = self.getPointDirections()
    
        distances, neighbourIndexes = self.findFixedRadiusNeighbours(pointCoordinates)
        for pointIndex, point in enumerate(self.points):
            neighbourDirections = [pointDirections[index] for index in neighbourIndexes[pointIndex] if index != pointIndex]
            point.updateDirection(neighbourDirections)
        pass
    
    def findFixedRadiusNeighbours(self, pointCoordinates: list[tuple[int, int]]):
        
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
        Updates the position of all the points on the box
        """
        for point in self.points:
            point.updatePosition()
        return
    
    # Get

    def getPointCoordinates(self):
        return np.array([point.getPosition() for point in self.points])
    
    def getPointDirections(self):
        return np.array([point.getDirection() for point in self.points])