from src.canvas import Canvas
from src.plot import plot

canvas = Canvas()
canvas.updateDirections()
plot(canvas.getPointCoordinates())