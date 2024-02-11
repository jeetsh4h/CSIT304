import matplotlib.pyplot as plt


def sector_points(radius):
    sector_points = [(0, round(radius))]

    # There is a problem here, we do not know which state to start with
    # sometimes False will lead to a unterminating loop
    state = False
    # state = True => right
    # state = False => down
    while True:
        prev_point = sector_points[-1]
        new_point = (
            (prev_point[0] + 1, prev_point[1])
            if state
            else (prev_point[0] + 1, prev_point[1] - 1)
        )
        state = not state

        sector_points.append(new_point)
        if new_point[0] == new_point[1]:
            break

    return sector_points


def draw_circle(radius):
    # assuming center is at (0, 0)
    # that's because we can just translate the circle

    slice_points = sector_points(radius)
    slice_reflect_points = [(y, x) for (x, y) in slice_points]

    quarter_points = slice_points + slice_reflect_points
    quarter_reflect_points = [(-x, y) for (x, y) in quarter_points]

    half_points = quarter_points + quarter_reflect_points
    half_reflect_points = [(x, -y) for (x, y) in half_points]

    full_points = half_points + half_reflect_points

    # print(len(full_points), len(slice_points))

    plt.scatter(
        [point[0] for point in full_points], [point[1] for point in full_points]
    )
    plt.show()


# draw_circle(8)


################### Better implementation #####################

def circle_points(radius, center=(0, 0)):
    # assuming the circle is centered at (0, 0)
    sector_points = [(0, radius)]
    decision_param = 1.25 - radius

    while True:
        prev_point = sector_points[-1]

        if prev_point[0] >= prev_point[1]:
            break

        if decision_param < 0:
            sector_points.append((prev_point[0] + 1, prev_point[1]))
            decision_param += 2 * (prev_point[0] + 1) + 1
        else:
            sector_points.append((prev_point[0] + 1, prev_point[1] - 1))
            decision_param += 2 * (prev_point[0] + 1) + 1 - 2 * (prev_point[1] - 1)


    sector_reflect_points = [(y, x) for (x, y) in sector_points]
    quarter_points = sector_points + sector_reflect_points

    quarter_reflect_points = [(-x, y) for (x, y) in quarter_points]
    half_points = quarter_points + quarter_reflect_points

    half_reflect_points = [(x, -y) for (x, y) in half_points]
    full_points = half_points + half_reflect_points

    translated_points = [(x + center[0], y + center[1]) for (x, y) in full_points]
    return translated_points


center = (3, 2)
circle = circle_points(8, center)
plt.scatter(
    [point[0] for point in circle] + [center[0]],
    [point[1] for point in circle] + [center[1]],
)
plt.show()
