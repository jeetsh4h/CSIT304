import matplotlib.pyplot as plt

# the two points that define the example line
point1 = (1, 1)
point2 = (8, 5)


""" My algorithm """
line_points = [point1]
while True:
    prev_point = line_points[-1]
    grad = (point2[1] - prev_point[1]) / (point2[0] - prev_point[0])

    if grad > 1:
        new_point = (prev_point[0], prev_point[1] + 1)
    elif grad == 1:
        new_point = (prev_point[0] + 1, prev_point[1] + 1)
    else:
        new_point = (prev_point[0] + 1, prev_point[1])

    line_points.append(new_point)

    if new_point == point2:
        break

print("My Algo points:")
print(line_points)
# plt.plot([point[0] for point in line_points], [point[1] for point in line_points])
# plt.plot([1, 8], [1, 5])
# plt.show()


""" Direct Line Drawing Algorithm """
grad = (point2[1] - point1[1]) / (point2[0] - point1[0])
intercept = point1[1] - grad * point1[0]

line_points = [point1]
for x_i in range(point1[0] + 1, point2[0] + 1):
    y_i = grad * x_i + intercept
    line_points.append((x_i, int(y_i)))

print("Direct Algo points:")
print(line_points)
# plt.plot([point[0] for point in line_points], [point[1] for point in line_points])
# plt.plot([1, 8], [1, 5])
# plt.show()


""" Direct Differential Algorithm """
grad = (point2[1] - point1[1]) / (point2[0] - point1[0])

line_points = [point1]
while True:
    prev_point = line_points[-1]
    new_point = (
        (prev_point[0] + (1 / grad), prev_point[1] + 1)
        if grad > 1
        else (prev_point[0] + 1, prev_point[1] + grad)
    )

    # we cannot round in the middle of the loop,
    # because it will introduce error in the next iteration

    line_points.append(new_point)
    if abs(new_point[0] - point2[0]) < 0.1 and abs(new_point[1] - point2[1]) < 0.1:
        break

print("DDA points:")
print([(round(x), round(y)) for x, y in line_points])   # rounding off here, closest integer
# plt.plot([point[0] for point in line_points], [point[1] for point in line_points])
# plt.plot([1, 8], [1, 5])
# plt.show()


""" Bresenham's Line Drawing Algorithm """

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

print("Bresenham's Algo points:")
print(line_points)
# plt.plot([point[0] for point in line_points], [point[1] for point in line_points])
# plt.plot([1, 8], [1, 5])
# plt.show()


#################### More graphics thingie #####################
def bresenham_points(point1, point2):
    """
    TODO: This one should be more akin to what is being spoken about 
    in class.
    """

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

def draw_triangle(point1, point2, point3):
    """
    This uses Bresenham's algorithm to draw a triangle
    """

    lines = [bresenham_points(point1, point2)]
    lines.append(bresenham_points(point2, point3))
    lines.append(bresenham_points(point3, point1))

    # print('\n', lines)

    for line_points in lines:
        plt.plot([point[0] for point in line_points], [point[1] for point in line_points])

    plt.show()



draw_triangle((1, 1), (8, 8), (4, 8))
draw_triangle((1, 1), (8, 5), (4, 8))
