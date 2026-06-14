from src.constants import constants
from src.miscFunctions import randomDirection

import numpy as np
from math import cos, sin, pi


class Point:
    """
    position: (int, int),
    velocity: int,
    direction: int (angle)
    """
    def __init__(self, position: tuple[float, float]) -> None:
        self.x, self.y = position
        self.velocity = constants["velocity"]
        self.direction = randomDirection()
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

        self.x = (self.x + deltaX) % constants["boxDimensions"]
        self.y = (self.y + deltaY) % constants["boxDimensions"]
        return
    
    def updateDirection(self, neighbourDirections: list[int]) -> None:
        if not neighbourDirections:  # No neighbours
            self.direction = (self.direction + constants["noiseAmplitude"] * randomDirection()) % (2*pi)
        else:
            xNeighbourUnitVector = np.mean([np.cos(neighbourDirection) for neighbourDirection in neighbourDirections])
            yNeighbourUnitVector = np.mean([np.sin(neighbourDirection) for neighbourDirection in neighbourDirections])

            neighbourDirection = np.atan2(yNeighbourUnitVector, xNeighbourUnitVector)
            self.direction = (neighbourDirection + constants["noiseAmplitude"] * randomDirection()) % (2*pi)
        pass

    