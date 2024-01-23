import matplotlib.pyplot as plt

def bresenham_points_top_right_to_bottom_left(point1, point2):
    """
    this only works if abs(dy/dx) < 1
    """
    x1, y1 = point1
    x2, y2 = point2
    m = (y2 - y1) / (x2 - x1)
    print(f"Gradient: {m}")

    line_points = []
# Case 1
    if 0 < m <= 1:
        dx = x1 - x2
        dy = y1 - y2
        P = (2 * dy) - dx
        x = x1
        y = y1

        line_points.append((x, y))

        while x > x2:
            x -= 1
            if P < 0:
                P += (2 * dy)
            else:
                y -= 1
                P += 2 * (dy - dx)

            line_points.append((x, y))
# case 2:
    elif m > 1:
        dx = x1 - x2
        dy = y1 - y2
        P = (2 * dx) - dy
        x = x1
        y = y1

        line_points.append((x, y))

        while y > y2:
            y -= 1
            if P < 0:
                P += (2 * dx)
            else:
                x -= 1
                P += 2 * (dx - dy)

            line_points.append((x, y))

    return line_points

# blue line
points = bresenham_points_top_right_to_bottom_left((8, 8), (2, 3))
plt.plot([point[0] for point in points], [point[1] for point in points])
# plt.show()

# orange line
points = bresenham_points_top_right_to_bottom_left((8, 8), (6, 2))
plt.plot([point[0] for point in points], [point[1] for point in points])
# plt.show()

# green line
points = bresenham_points_top_right_to_bottom_left((8, 8), (2, 2))
plt.plot([point[0] for point in points], [point[1] for point in points])
plt.show()