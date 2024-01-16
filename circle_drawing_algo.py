import matplotlib.pyplot as plt
# TODO: implement this algorithm

def sector_points(radius):
    sector_points = [(0, round(radius))]

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
    plt.plot([point[0] for point in slice_points], [point[1] for point in slice_points])
    plt.show()


draw_circle(8)