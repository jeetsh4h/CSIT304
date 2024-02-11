import matplotlib.pyplot as plt


# TODO: Please go through the Breseham's algorithm and find the way
# that sir wanted us to implement it in. This one doesn't seem to be
# what was asked for. This does generalise well, if I write comments
# to explain everything maybe this will be okay


def bresenham_points(point1, point2):
    dx = abs(point2[0] - point1[0])
    dy = abs(point2[1] - point1[1])
    slope_error = dx - dy

    line_points = [point1]

    while True:
        double_error = slope_error * 2
        
        x, y = line_points[-1]

        if double_error > -dy:
            slope_error -= dy
            x += 1 if point2[0] > point1[0] else -1

        if double_error < dx:
            slope_error += dx
            y += 1 if point2[1] > point1[1] else -1

        new_point = (x, y)

        line_points.append(new_point)
        if abs(new_point[0] - point2[0]) < 0.1 and abs(new_point[1] - point2[1]) < 0.1:
            break

    return line_points

def draw_triangle(point1, point2, point3, verbose=False):
    """
    This uses Bresenham's algorithm to draw a triangle
    """

    lines = [bresenham_points(point1, point2)]
    lines.append(bresenham_points(point2, point3))
    lines.append(bresenham_points(point3, point1))

    if verbose:
        (print(line) for line in lines)

    for line_points in lines:
        plt.plot([point[0] for point in line_points], [point[1] for point in line_points])

    plt.show()


draw_triangle((1, 1), (8, 8), (4, 8))
draw_triangle((1, 1), (8, 5), (4, 8))

