import matplotlib.pyplot as plt

def plot(pointsCoordinates: list[tuple[int, int]]):
    fig, ax = plt.subplots()
    
    x = [coords[0] for coords in pointsCoordinates]
    y = [coords[1] for coords in pointsCoordinates]

    plt.scatter(x, y)
    plt.show()