from constants import constants
from point import Point

class Canvas:
    """
    The canvas of the all the points of the simulation
    """
    def __init__(self) -> None:
        self.dimensions = constants["canvasDimensions"]
        self.numberOfPoints = constants["numberOfPoints"]
        self.points: list[Point] = []
        return

    # Start
    def initiate(self) -> None:
        """
        Adds the number of points to the canvas and runs a short equilibration
        """
        pass

    # Update
    def updateDirections(self) -> None:
        """
        Updates the direction of all the points on the canvas
        """
        self.assignPointsToBoxes()
        pass

    def assignPointsToBoxes(self) -> None:
        """
        The board is divided in boxes of 1x1 and the points are assigned to the box they're in
        """
        self.boxes: dict[int, list[Point]] = {}
        for point in self.points:
            x,y = point.getPosition()
            boxID: int = round(x + y*self.dimensions)
            self.addPointToBox(point, boxID)
        return
    
    def addPointToBox(self, point: Point, boxID: int) -> None:
        """
        Adds the point to the box corresponding to their boxID
        """
        if self.boxes[boxID]:
            self.boxes[boxID].append(point)
        else:
            self.boxes[boxID] = [point]
        return

    def updatePositions(self) -> None:
        """
        Updates the position of all the points on the canvas
        """
        for point in self.points:
            point.updatePosition()
        return
