from src.canvas import Canvas
from src.plot import plot

canvas = Canvas()
canvas.updateDirections()

coordinates = canvas.getPointCoordinates()
distances, indexes = canvas.findFixedRadiusNeighbours()
center = coordinates[0]
neighbourIndexes = [int(index) for index in indexes[0]]
neighbours = [coordinates[index] for index in neighbourIndexes]
plot(coordinates, center, neighbours)