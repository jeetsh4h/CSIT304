import matplotlib.pyplot as plt

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
# TODO: Clean it upCSIT3
grad = (point2[1] - point1[1]) / (point2[0] - point1[0])

line_points = [point1]
while True:
    prev_point = line_points[-1]
    new_point = (
        (prev_point[0] + (1 / grad), prev_point[1] + 1)
        if grad > 1
        else (prev_point[0] + 1, prev_point[1] + grad)
    )

    line_points.append(new_point)
    if new_point >= point2:
        break

print("DDA points:")
print([(round(x), round(y)) for x, y in line_points])
plt.plot([point[0] for point in line_points], [point[1] for point in line_points])
plt.plot([1, 8], [1, 5])
plt.show()



""" Bresenham's Line Drawing Algorithm """
