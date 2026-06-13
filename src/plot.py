import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from src.constants import constants

def plot(coordinates: list[tuple[int,int]], center: tuple[int, int], neighbours: list[tuple[int, int]]):
    fig, ax = plt.subplots()

    xCenter, yCenter = center

    xCoords = [coords[0] for coords in coordinates]
    yCoords = [coords[1] for coords in coordinates]

    xNeighbours = [coords[0] for coords in neighbours]
    yNeighbours = [coords[1] for coords in neighbours]
    
    plt.scatter(xCoords, yCoords, c="b")
    plt.scatter(xNeighbours, yNeighbours, c="r")
    ax.scatter([xCenter], [yCenter], c="g")

    circle = Circle((xCenter, yCenter), radius=constants["influenceRadius"],
                    fill=False, edgecolor="black", linewidth=2)
    ax.add_patch(circle)

    ax.set_aspect("equal")  # keep the circle circular
    plt.show()