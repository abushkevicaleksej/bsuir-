import enum
import matplotlib.pyplot as plt


class Mode(enum.Enum):
    none = "Не выбрано"
    cda = "ЦДА"
    brez = "Метод Брезенхема"
    wu = "Метод Ву"


def sign(d):
    if d > 0 or d < 0:
        return 1
    else:
        return 0

def cda(x_1, x_2, y_1, y_2):
    length = max(abs(x_2 - x_1), abs(y_2 - y_1))
    x_coords = []
    y_coords = []
    if abs(x_2 - x_1) > abs(y_2 - y_1):
        dx = 1
        dy = (y_2 - y_1) / length
    else:
        dy = 1
        dx = (x_2 - x_1) / length

    x = x_1 + 0.5 * sign(dx)
    y = y_1 + 0.5 * sign(dy)

    x_coords.append(x)
    y_coords.append(y)

    i = 0
    while i < length:

        x += dx
        y += dy
        x_coords.append(x)
        y_coords.append(y)
        i += 1

    plt.plot(x_coords, y_coords, 'b-')
    plt.grid(True)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))

    plt.show()

def br(x_1, x_2, y_1, y_2):
    x = x_1
    y = y_1
    del_x = x_2 - x_1
    del_y = y_2 - y_1
    e = 2 * del_y - del_x
    x_coords = []
    y_coords = []
    x_coords.append(x)
    y_coords.append(y)
    i = 1
    while i <= del_x:
        if e>=0:
            y += 1
            e -= 2 * del_x
        x += 1
        e += 2 * del_y

        x_coords.append(x)
        y_coords.append(y)
        i += 1

    plt.plot(x_coords, y_coords, 'b-')
    plt.grid(True)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
    plt.show()


def wu_line(x1, x2, y1, y2):
    # Ensure coordinates are integers
    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

    # Determine if line is steep (|m| > 1)
    steep = abs(y2 - y1) > abs(x2 - x1)

    # If line is steep, transpose coordinates
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # If line goes right to left, swap points
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    # Calculate differences and step
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        gradient = 1
    else:
        gradient = dy / dx

    # Handle first endpoint
    xend = round(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = 1 - ((x1 + 0.5) - int(x1))
    xpxl1 = xend
    ypxl1 = int(yend)

    if steep:
        plt.plot(ypxl1, xpxl1, 'ko', alpha=(1 - (yend - int(yend))) * xgap)
        plt.plot(ypxl1 + 1, xpxl1, 'ko', alpha=(yend - int(yend)) * xgap)
    else:
        plt.plot(xpxl1, ypxl1, 'ko', alpha=(1 - (yend - int(yend))) * xgap)
        plt.plot(xpxl1, ypxl1 + 1, 'ko', alpha=(yend - int(yend)) * xgap)

    intery = yend + gradient

    # Handle second endpoint
    xend = round(x2)
    yend = y2 + gradient * (xend - x2)
    xgap = (x2 + 0.5) - int(x2)
    xpxl2 = xend
    ypxl2 = int(yend)

    if steep:
        plt.plot(ypxl2, xpxl2, 'ko', alpha=(1 - (yend - int(yend))) * xgap)
        plt.plot(ypxl2 + 1, xpxl2, 'ko', alpha=(yend - int(yend)) * xgap)
    else:
        plt.plot(xpxl2, ypxl2, 'ko', alpha=(1 - (yend - int(yend))) * xgap)
        plt.plot(xpxl2, ypxl2 + 1, 'ko', alpha=(yend - int(yend)) * xgap)

    # Main loop
    if steep:
        for x in range(xpxl1 + 1, xpxl2):
            plt.plot(int(intery), x, 'ko', alpha=1 - (intery - int(intery)))
            plt.plot(int(intery) + 1, x, 'ko', alpha=intery - int(intery))
            intery += gradient
    else:
        for x in range(xpxl1 + 1, xpxl2):
            plt.plot(x, int(intery), 'ko', alpha=1 - (intery - int(intery)))
            plt.plot(x, int(intery) + 1, 'ko', alpha=intery - int(intery))
            intery += gradient

    # Set equal aspect ratio and display
    plt.axis('equal')
    plt.grid(True)
    plt.show()