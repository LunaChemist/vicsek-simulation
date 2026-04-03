from constants import constants

from math import cos, sin, pi
from random import randrange

class Point:
    """
    position: (int, int),
    velocity: int,
    direction: int (angle)
    """
    def __init__(self, position: tuple[float, float]) -> None:
        self.x, self.y = position
        self.velocity = constants["velocity"]
        self.direction = (randrange(-100, 100)/100)*pi  # [-pi, pi]
        return

    # Get properties
    def getPosition(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def getDirection(self) -> float:
        return self.direction
    
    # Update properties
    def updatePosition(self) -> None:
        """
        Moves the point one timestep forward, also accounts for periodic boundaries
        """
        deltaX = constants["timestep"]*self.velocity*cos(self.direction)
        deltaY = constants["timestep"]*self.velocity*sin(self.direction)

        self.x = (self.x + deltaX) % constants["canvasDimensions"]
        self.y = (self.x + deltaY) % constants["canvasDimensions"]
        return
    
    def updateDirection(self, direction: int) -> None:
        self.direction = direction
        return
    