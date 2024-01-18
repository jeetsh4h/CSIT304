import matplotlib.pyplot as plt


def ellipse_points(radius_x, radius_y, center=(0, 0)):
    # assuming the ellipse is centered at (0, 0)
    quarter_points = [(0, radius_y)]

    # decision parameter for region 1
    d_param_1 = (
        (radius_y * radius_y)
        - (radius_x * radius_x * radius_y)
        + (0.25 * radius_x * radius_x)
    )

    # calculate region 1 points
    while True:
        prev_point = quarter_points[-1]

        if radius_y * radius_y * prev_point[0] >= radius_x * radius_x * prev_point[1]:
            break

        if d_param_1 < 0:
            quarter_points.append((prev_point[0] + 1, prev_point[1]))
            d_param_1 += (
                2 * (radius_y * radius_y) * (prev_point[0] + 1) + radius_y * radius_y
            )
        else:
            quarter_points.append((prev_point[0] + 1, prev_point[1] - 1))
            d_param_1 += (
                2 * (radius_y * radius_y) * (prev_point[0] + 1)
                - 2 * (radius_x * radius_x) * (prev_point[1] - 1)
                + (radius_y * radius_y)
            )

    # decision parameter for region 2
    d_param_2 = (
        ((radius_y * radius_y) * ((prev_point[0] + 0.5) * (prev_point[0] + 0.5)))
        + (
            ((radius_x * radius_x) * (radius_x * radius_x))
            * ((prev_point[1] - 1) * (prev_point[1] - 1))
        )
        - (radius_x * radius_x * radius_y * radius_y)
    )

    # calculate region 2 points
    while True:
        prev_point = quarter_points[-1]

        if prev_point[1] <= 0:
            break

        if d_param_2 < 0:
            quarter_points.append((prev_point[0] + 1, prev_point[1] - 1))
            d_param_2 += (
                2 * (radius_y * radius_y) * (prev_point[0] + 1)
                - 2 * (radius_x * radius_x) * (prev_point[1] - 1)
                + (radius_x * radius_x)
            )
        else:
            quarter_points.append((prev_point[0], prev_point[1] - 1))
            d_param_2 += (
                -2 * (radius_x * radius_x) * (prev_point[1] - 1)
                + (radius_x * radius_x)
            )

    
    quarter_reflect_points = [(-x, y) for (x, y) in quarter_points]
    half_points = quarter_points + quarter_reflect_points

    half_reflect_points = [(x, -y) for (x, y) in half_points]
    full_points = half_points + half_reflect_points

    translated_points = [(x + center[0], y + center[1]) for (x, y) in full_points]
    return translated_points


center = (0, 0)
ellipse = ellipse_points(8, 6, center)
plt.scatter(
    [point[0] for point in ellipse] + [center[0]],
    [point[1] for point in ellipse] + [center[1]],
)
plt.show()