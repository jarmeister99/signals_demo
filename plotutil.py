from util import FLOAT_EPSILON


def constrain_points(points, num_points, timestep):
    return None


def add_head_and_tail(points, timestep, minval, maxval, already_sorted=False):
    if not already_sorted:
        points.sort()
    head = []
    tail = []
    head.append((minval, 0))
    if points[0][0] - timestep > minval:
        head.append((points[0][0] - timestep, 0))
    if points[-1][0] + timestep < maxval:
        tail.append((points[-1][0] + timestep, 0))
    tail.append((maxval, 0))
    return [point for point in head + points + tail if minval <= point[0] <= maxval]
